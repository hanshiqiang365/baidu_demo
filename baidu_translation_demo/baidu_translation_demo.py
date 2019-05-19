import urllib,hashlib
import random
import requests,sys

def getTransText(in_text):
	q = in_text
	fromLang = 'auto'
	toLang1 = 'auto'

	appid = 'XXXXXXXXXXX' #APP ID
	salt = random.randint(32768, 65536)
	secretKey = 'XXXXXXXXXXXXXXXX' #SecretKey

	sign = appid+q+str(salt)+secretKey
	m1 = hashlib.md5(sign.encode('utf-8'))
	sign = m1.hexdigest()
     
	myurl = '/api/trans/vip/translate'
	myurl = myurl+'?appid='+appid+'&q='+q+'&from='+fromLang+'&to='+toLang1+'&salt='+str(salt)+'&sign='+sign
	url = "http://api.fanyi.baidu.com"+myurl

	url = url.encode('utf-8')
	res = requests.get(url)

	res = eval(res.text)
	return (res["trans_result"][0]['dst'])

number = 1
final_text = ""
while(True):
        in_text = input()
        out_text = getTransText(in_text)
        print (in_text+'  =  ' + out_text)
        
        final_text = final_text + f"#{number} - {in_text} = {out_text}" + "\r\n"
        number = number + 1
        if number == 6:
                break

with open(f'translation.txt', 'wb') as txt_f:
        txt_f.write(final_text.encode('utf-8'))



        


