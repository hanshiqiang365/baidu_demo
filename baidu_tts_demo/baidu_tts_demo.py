#author: hanshiqiang365 （微信公众号：韩思工作室）

from aip import AipSpeech
import os
from playsound import playsound

APP_ID = 'XXXXX'
API_KEY = 'XXXXXX'
SECRET_KEY = 'XXXXXXXX'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

text = "绝句 作者：韩思先生。野蛮文明不束手，外星人变外星猴。宇宙万物皆泡酒，中华国粹玩个够。"
result  = client.synthesis(text, 'zh', 1, {'vol': 5,'per':4})

voicefile = 'voices\\auido.mp3'

if not isinstance(result, dict):
    with open(voicefile, 'wb') as f:
        f.write(result)

print(text)

playsound(voicefile)
