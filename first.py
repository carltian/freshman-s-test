#调用有道词典的web接口进行翻译
#!/usr/bin/env python3
#coding: utf-8
_author_ = 'Carl'
import urllib.request
import urllib.parse
import json
connect = input('请输入你要翻译的文字：')
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null'
head ={}
head['User-Agent'] ='Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0'
data = {}
data['action'] = 'FY_BY_CLICKBUTTION'
data['client'] = 'fanyideskweb'
data['doctype'] = 'json'
data['from'] = 'AUTO'
data['i'] = connect
data['keyfrom'] = 'fanyi.web'
data['salt'] = '1527213522111'
data['sign'] = '3b21f144978b593bafa71d4abcc38dca'
data['smartresult'] = 'dict'
data['to'] = 'AUTO'
data['typoResult'] = 'false'
data['version'] = '2.1'
data = urllib.parse.urlencode(data).encode('utf-8')
response = urllib.request.urlopen(url,data)
html = response.read().decode('utf-8')
target = json.loads(html)
print ("输入文字为：%s" % (target['translateResult'][0][0]['src']))
print ("翻译结果为：%s" % (target['translateResult'][0][0]['tgt']))
