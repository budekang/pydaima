# -*- coding: utf-8 -*-
import requests
import re
import random

def spiderPic(html,keyword):
    print('正在查找'+keyword)
    for addr in re.findall('"objURL":"(.*?)"',html,re.S):
        print('正在爬取的地址：'+str(addr))

        try:
            pics = requests.get(addr,timeout=10)
        except requests.exceptions.ConnectionError:
            print('请求错误！')
            continue

        fn=open('G:\\img\\'+(str(random.randrange(0,5000,4))+'.jpg'),'wb')
        fn.write(pics.content)
        fn.close()

if __name__=='__main__':
    print('这是主方法')
    word=input('请输入要搜索的关键词：')
    result=requests.get('http://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1538101817480_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&word='+word)
    print(result.text)

    spiderPic(result.text,word)
