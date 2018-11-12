from urllib import request
from bs4 import BeautifulSoup
import os
def download_specified_chapter(chapter_url,header,coding,chapter_name=None):
    #先生成一个request对象,传入url和headers
    download_req = request.Request(chapter_url,headers=header)
    #通过指定urlopen打开request对象中的url网址,并获得对应内容
    response = request.urlopen(download_req)
    #获取页面的html
    download_html = response.read().decode(coding, 'ignore')
    #获取html的bs
    origin_soup = BeautifulSoup(download_html, 'lxml')
    #获取小说正文部分
    content=origin_soup.find(id='content', class_='showtxt')
    #经打印,发现文本中有众多的\xa0(在html中是&nbsp;),并且没有换行,
    print(repr(content.text))
    #整理小说格式,将\xa0替换成回车
    # html中的&nbsp,在转换成文档后,变成\xa0
    txt=content.text.replace('\xa0'*8,'\n')
    print(txt)
if __name__=="__main__":
    target_url='http://www.biqukan.com/3_3039/1351331.html'
    header = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/'
                     '535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    }
    download_specified_chapter(target_url,header,'gbk')