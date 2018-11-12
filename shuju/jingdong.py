import json
import requests
from bs4 import BeautifulSoup

input_name = input('请输入搜索关键字：')

# 获取京东商品前50页的信息，包括名称，价格，图片，商店
def get_jd():
    #循环获得网页url
    for i in range(1, 100):
        #定义请求头
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36',
            'upgrade-insecure-requests': '1',
        }
        url = 'https://search.jd.com/Search?keyword={}&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page={}'.format(input_name, 2*i-1)
        #获取网页
        html = requests.get(url, headers=headers).content.decode('utf-8')
        #分析网页
        soup = BeautifulSoup(html, 'lxml')
        li_list = soup.find_all('li', class_='gl-item')
        detail_list = []
        for li in li_list:
            #提取需要内容
            image = 'https:' + li.find('div', class_='p-img').find('a').find('img')['source-data-lazy-img']
            price = li.find('div', class_='p-price').find('i').text
            name = li.find('div', class_='p-name').find('i').text
            shop = li.find('div', class_='p-shop').text
            #生成字典
            dict1 = {
                'name': name,
                'image': image,
                'price': price,
                'shop': shop
            }
            detail_list.append(dict1)
        return detail_list

def save_content(contents):
    #定义文件标题
    filename = input_name + '.txt'
    for content in contents:
        with open(filename, 'a', encoding='utf-8') as f:
            #将字典转化为json对象保存在文件中
            f.write(json.dumps(content, ensure_ascii=False))


def main():
    content = get_jd()
    save_content(content)


if __name__ == '__main__':
    main()
