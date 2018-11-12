# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
doc = pq(url='http://sports.sina.com.cn/nba/',encoding='utf-8')
print(doc('title'))
#items = doc('.list')
items = doc('.list')
#print(items.children('.item'))
a = items.children()
print(a)
print(a.html())
print(doc('.list li p'))
