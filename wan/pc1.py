# coding:utf-8
import requests
from bs4 import BeautifulSoup
# 下载新浪新闻首页的内容
url = 'http://news.sina.com.cn/china/'
# 用get函数发送GET请求，获取响应
res = requests.get(url)
# 设置响应的编码格式utf-8（默认格式为ISO-8859-1），防止中文出现乱码
res.encoding = 'utf-8'
#print( type(res))
#print (res)
#print("**************************")
print (res.text)
#print("**************************")
soup=BeautifulSoup(res.text,'html.parser')
#print(soup)
#print(soup.title)
#print(soup.prettify())

print(soup.script)
#print(soup.find_all(target="_blank"))
#for item in soup.find_all('a'):
   # print(item,'\n')

#print(soup.select('title'))
