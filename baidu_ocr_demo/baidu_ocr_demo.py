#author:hanshiqiang365 （微信公众号：韩思工作室）

from aip import AipOcr

APP_ID = 'Your APP ID'
API_KEY = 'Your API KEY'
SECRET_KEY = 'Your Secret Key'

aipOcr  = AipOcr(APP_ID, API_KEY, SECRET_KEY)

# 读取图片
filePath = "images/newspaper.jpg"
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 定义参数变量
options = {
  'detect_direction': 'true',
  'language_type': 'ENG+JPN',
}

# 调用通用文字识别接口
result = aipOcr.basicAccurate(get_file_content(filePath), options)

print(result)

with open(f'{filePath}.txt', 'wb') as f:
    f.write(str(result).encode('utf-8'))
