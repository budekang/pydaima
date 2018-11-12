# -*- coding: utf-8 -*-

import urllib
haha = urllib.request.urlopen('https://news.sina.com.cn/china/')
print(haha.read().encode('utf-8'))