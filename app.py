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

line_bot_api = LineBotApi('qYysKaw7iTbO04HF3h9/MjpUhRg8ZyfW1A0X47lhzg2hecsp/o16HokeOzAuQ3mCMhRqSZ1a8mt11L33ORHEa1CB/WLszH9y4iy3WSfgNDpt4DX95WDuf2gNSHMFgqU3dYLxTA7ziOYvl8N2cygdAQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('48fdbde5334c7765175200d8f35ac080')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()