#author: hanshiqiang365 （微信公众号：韩思工作室）

from PIL import Image 
import os.path 
import glob
import base64
import requests

def get_img_base64str(image):
    with open(image,'rb') as fp:
        imgbase64 = base64.b64encode(fp.read())
        return imgbase64.decode()

def get_access_token(APP_ID,API_KEY,SECRET_KEY):
    params     = {
        "grant_type":   "client_credentials",
        'client_id':    API_KEY,
        'client_secret':SECRET_KEY,}
    token_url = 'https://aip.baidubce.com/oauth/2.0/token'
    res = requests.get(token_url,params = params)
    try:
        data = res.json()
        return data['access_token']
    except:
        return ''

def enlarge_image(image_file,access_token):
    image       = get_img_base64str(image_file)
    data        = {"image":image}
    params       = {'access_token':access_token}
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/image_quality_enhance"
    res = requests.post(request_url,params = params,data = data)
    try:
        image_data = res.json()['image']
        img_bytes  = base64.b64decode(image_data)
        with open(image_file.replace('365','365_2'),'wb') as fp:
            fp.write(img_bytes)
        print ("Success！")
    except:
        print ("ERROR！")


if __name__ == '__main__':
    APP_ID     = 'XXXXXXXXXXXXXXX'
    API_KEY    = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'
    SECRET_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

    photofile = "hanshiqiang365.jpg"
    access_token = get_access_token(APP_ID,API_KEY,SECRET_KEY)
    enlarge_image(photofile,access_token)


