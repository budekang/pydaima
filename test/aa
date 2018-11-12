#用BeautifulSoup4剖析网页元素
#试示例：

from bs4 import BeautifulSoup
html_sample = ' \
<html> \
<body> \
<h1 id="title">Hello World</h1> \
<a href="#" class="link">This is link1</a> \
<a href="# link2" class="link">This is link2</a> \
</body> \
</html>'

soup = BeautifulSoup(html_sample, 'lxml')
print(soup.text)
print("*********分割线************")

#使用select找出含有h1标签的元素
soup = BeautifulSoup(html_sample)
header = soup.select('h1')
print(header)
print(header[0])
print(header[0].text)
print("*********分割线************")

#使用select找出含有a的标签
soup = BeautifulSoup(html_sample, 'lxml')
alink = soup.select('a')
print(alink)
for link in alink:
    print(link)
    print(link.txt)
print("*********分割线************")

 #使用select找出所有id为title的元素(id前面需要加#)
alink = soup.select('#title')
print(alink)
print("*********分割线************")

#使用select找出所有class为link的元素(class前面需要加.)
soup = BeautifulSoup(html_sample)
for link in soup.select('.link'):
    print(link)
print("*********分割线************")

#使用select找出所有a tag的href链接
alinks = soup.select('a')
for link in alinks:
    print(link['href']) # 原理：会把标签的属性包装成字典