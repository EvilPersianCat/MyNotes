import json
urls={'baidu':'http://www.baidu.com/',
      'sina':'http://www.sina.com.cn/',
      'tencent':'http://www.qq.com/',
      'taobao':'https://www.taobao.com/'}
with open(r'data.json', 'w') as f:
    json.dump(urls, f)
