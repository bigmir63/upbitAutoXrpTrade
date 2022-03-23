import time
import datetime
import requests

myToken = "봇을 생성할 때 슬랙에서 주는 토큰 입력" 


def post_message(token, channel, text):
    """슬랙 메시지 전송"""
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

post_message(myToken,"#auto_stocktrade", "현재잔고 ")
