import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq
doc = pq(url='http://www.bjhd.gov.cn/banshi/matter/matterInfo/info?sxjbxxId=b7fbb592398047f5951df9d60c4e5b40',encoding='utf-8')
print(doc)
li = doc('.info_table_hidden .info_table').children().children()
#print(type(li))
#print(li)
'''for qa in li.items():
    q=qa.find('th')
    print(q.text())
    a=qa.find('td')
    print(a.text())
'''
for th in li.items():
    print(th.text())
