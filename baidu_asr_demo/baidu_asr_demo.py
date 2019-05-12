#author: hanshiqiang365 （微信公众号：韩思工作室）
import requests
import json
import base64
import os
import logging
import speech_recognition as sr
import time

def get_token():
    logging.info('开始获取token...')
    #获取token
    baidu_server = "https://openapi.baidu.com/oauth/2.0/token?"
    grant_type = "client_credentials"
    client_id = "XXXXXX" #AppUD
    client_secret = "XXXXXXXXXXXXXX" #Secret Key

    #拼url
    url = f"{baidu_server}grant_type={grant_type}&client_id={client_id}&client_secret={client_secret}"
    res = requests.post(url)
    token = json.loads(res.text)["access_token"]
    return token


def baiduai_audio(filename):
    logging.info('开始识别语音文件...')
    with open(filename, "rb") as f:
        speech = base64.b64encode(f.read()).decode('utf-8')
    size = os.path.getsize(filename)
    token = get_token()
    headers = {'Content-Type': 'application/json'}
    url = "https://vop.baidu.com/server_api"
    data = {
        "format": "wav",
        "rate": "16000",
        "dev_pid": "1536",
        "speech": speech,
        "cuid": "hanshiqiang365",
        "len": size,
        "channel": 1,
        "token": token,
    }

    req = requests.post(url, json.dumps(data), headers)
    result = json.loads(req.text)

    if result["err_msg"] == "success.":
        print(result['result'])
        return result['result']
    else:
        print("内容获取失败，退出语音识别")
        return -1


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    final_text = ''

    wav_num = 0
    while True:
        r = sr.Recognizer()
        mic = sr.Microphone()
        logging.info('录音中...')
        with mic as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        with open(f"voices/000{wav_num}.wav", "wb") as f:
            f.write(audio.get_wav_data(convert_rate=16000))
        logging.info('录音结束，识别中...')
        target = baiduai_audio(f"voices/000{wav_num}.wav")
        if target == -1:
            break
        wav_num += 1
        final_text = final_text + str(target) + '\r\n'

    txt_file = time.strftime('%Y.%m.%d',time.localtime(time.time()))
    with open(f'voices/{txt_file}.txt', 'wb') as txt_f:
        txt_f.write(final_text.encode('utf-8'))

