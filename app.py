from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage,
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
    msg = event.message.text
    r = '很抱歉，您說什麼'
    if '想說說話' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='4'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return
    elif '我好生氣' in msg:
        sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='2'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return
    elif '今天好開心' in msg:
         sticker_message = StickerSendMessage(
            package_id='1',
            sticker_id='14'
        )
        line_bot_api.reply_message(
        event.reply_token,
        sticker_message)
        return

    if msg in ['hi', 'Hi', '你好']:
        r = '嗨, 你好!\n很開心認識你唷!'
    elif msg == '你是誰':
        r = '我是機器人'
    elif '訂位' in msg:
        r = '您想訂位，是嗎?'
    elif msg == '今天心情不好':
        r = '可以跟我說說唷! \n我可以當你的聽眾'
    elif msg == '我們可以做朋友嗎?':
        r = '當然! 你是我最好的朋友'
    elif msg == '心情好煩':
        r ='怎麼了呢? 是誰讓你心煩，我去找他談談'
    elif msg == '你會做什麼呢?':
        r = '我未來會會的很多，\n但是目前還是有許多要學習的'


    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=r))


if __name__ == "__main__":
    app.run()