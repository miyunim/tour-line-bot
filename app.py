from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('xMcP0bVZRhm33RNqosj3u6ofrfvdEswVvpYZKc6DMoN3xKSKwa/2XG8zJymho3tSo47vP/oON0QLMuvuP/lLW7TdhC+HanD7zGYc6bo7xmneAN3d4wAdSIO/qD48nH31knswW0eGLhQtkB6ambLijAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('1c2ce372caa247af38ca4484dda7960d')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
