import requests
import re
import json
import time
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
def get_one_page(url):

    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit 537.36 (KHTML, like Gecko) Chrome","Accept": "text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,*/*;q=0.8"}
    response=requests.get(url,headers=headers)
    if response.status_code==200:
        return response.text
    return None

def main():
    url='http://www.bjhd.gov.cn/banshi/matter/matterInfo/info?sxjbxxId=b7fbb592398047f5951df9d60c4e5b40'
    html=get_one_page(url)
    #print(html)


    soup=BeautifulSoup(html,'lxml')
    print(soup.title.string)
    #print(soup.find_all(name='tr'))
    #print(soup.find_all(name='th'))
    #print(soup.find_all(name='td'))
    #biao = soup.find_all(name='tr')
    #question=soup.find_all(name='th')
    #answer=soup.find_all(name='td')

    for tr in soup.select('tr'):
        print(tr)
        print(len(tr.select('th')))
        print(len(tr.select('td')))
        #print(tr.select('th'))
        length=len(tr.select('th'))
        for i in range(1,length):
            print(len(tr.select('th')))
            print(tr.select('th')[i-1])
            #print(tr.select('tr')[i-1])
        #print(tr.select('th')[0])
        #print(tr.select('td')[0])
        #for th in soup.select(tr)




    '''for tr in soup.find_all(name='tr'):
        #print(tr.find_all(name='th'))
        for th in tr.find_all(name='th'):
            for td in tr.find_all(name='td'):
                print(th.string+'***'+td.string)

    question=soup.find_all(name='tr')
    answer = soup.find_all(name='td')
    print(len(question))
    print(len(answer))'''

if __name__ == '__main__':
    main()