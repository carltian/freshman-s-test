#-*- coding:utf-8 -*-
#!/usr/bin/env python
# def findMinAndMax(L):
#     if L != []:
#         max = L[0]
#         min = L[0]
#         for l in L:
#             if max < l:
#                 max = l
#             if min > l:
#                 min = l
#         return (min,max)
#     else:
#         return(None,None)
# print(findMinAndMax([1,2,8,6,3,70,0]))
#列表生成式
#L1 = ['Hello', 'World', 18, 'Apple', None]
#L2 = [s.lower() for s in L1 if isinstance(s,str)]
#print(L2)
# def save_file(boy,girl,count):
#     file_name_boy = 'boy_' + str(count) + '.txt'
#     file_name_girl = 'girl_' + str(count) + '.txt'
#
#     boy_file = open(file_name_boy, 'w')
#     girl_file = open(file_name_girl, 'w')
#
#     boy_file.writelines(boy)
#     girl_file.writelines(girl)
#
#     boy_file.close()
#     girl_file.close()
# def split_file(file_name):
#     f = open(file_name)
#     boy = []
#     girl = []
#     count = 1
#     for each_line in f:
#         if each_line[:2] != '==':
#             (role, line_spoken) = each_line.split('：', 1)
#             if role == '小甲鱼':
#                 boy.append(line_spoken)
#             if role == '小客服':
#                 girl.append(line_spoken)
#         else:
#             save_file(boy,girl,count)
#             boy = []
#             girl = []
#             count += 1
#     save_file(boy, girl, count)
#     f.close()
# split_file('record')

#计时器
# import time as t
# class Mytimer():
#     def __init__(self):
#         self.unit = ['年','月','日','时','分','秒']
#         self.promte = "未开始计时"
#         self.lasted = []
#         self.begin = 0
#         self.end = 0
#     def __str__(self):
#         return self.promte
#     _repr_ = __str__
#     def __add__(self, other):
#         promte = "总共运行了"
#         result = []
#         for index in range(6):
#             result.append(self.lasted[index] + other.lasted[index])
#             if result[index]:
#                 promte += (str(result[index] + self.unit[index]))
#         return promte
#     def start(self):
#         self.begin = t.localtime()
#         self.promte = "请先调用stop"
#         print("开始计时")
#     def stop(self):
#         if not self.begin:
#             print("请先调用start")
#         else:
#             self.end= t.localtime()
#             self._calc()
#             print ("计时结束")
#     def _calc(self):
#         self.lasted = []
#         self.promte = "总共时间是"
#         for index in range(6):
#             self.lasted.append(self.end[index]-self.begin[index])
#             self.promte += str(self.lasted[index])
#             if self.lasted[index]:
#                 self.promte += (str(self.lasted[index]) + self.unit[index])
#         self.begin = 0
#         self.end = 0



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