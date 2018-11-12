# coding:utf-8
import requests
from bs4 import BeautifulSoup
url = 'http://zwfw.bjhd.gov.cn/banshi/matter/matterInfo/list?ppid=1001'
# 用get函数发送GET请求，获取响应
res = requests.get(url)
# 设置响应的编码格式utf-8（默认格式为ISO-8859-1），防止中文出现乱码
res.encoding = 'utf-8'
print( type(res))
print (res)
#print (res.text)
soup=BeautifulSoup(res.text,'html.parser')
#print(soup.a)
#print(soup.title)
#print(soup.head)
print(soup.prettify())
#print(soup.select('a'))
##########################################
#print(soup.find_all('a'))
print(soup.select('a'))
