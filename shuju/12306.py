from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from bs4 import BeautifulSoup
import io, sys, time, datetime, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='gb18030')


class Info12306(object):
    def __init__(self):
        # 座位种类
        self.ztype = {"SWZ": "商务特等座",
                      "ZY": "一等座",
                      "ZE": "二等座",
                      "GR": "高级软卧",
                      "RW": "软卧",
                      "SRRB": "动卧",
                      "YW": "硬卧",
                      "RZ": "软座",
                      "YZ": "硬座",
                      "WZ": "无座",
                      "QT": "其他"}
        self.url = "https://kyfw.12306.cn/otn/leftTicket/init"
        self.info = {}
        self.browser = webdriver.Chrome()  # 初始化浏览器
        self.wait = WebDriverWait(self.browser, 5)

    def open_html(self):
        self.browser.get(self.url)

    def close_html(self):
        self.browser.close()

    # 点击查询按钮
    def click_query(self):
        self.query_ticket = self.wait.until(EC.presence_of_element_located((By.ID, "query_ticket")))
        self.query_ticket.click()

    # 点击离今天往后第n天的结果
    def set_date(self, n):
        needDate = datetime.datetime.now() + datetime.timedelta(days=n)  # 获取今天的时间往后偏移n天
        css_month = 'body > div.cal-wrap > div:nth-child(1) > div.cal-top > div.month > ul > li:nth-child(%d)' % needDate.month
        css_day = 'body > div.cal-wrap > div:nth-child(1) > div.cal-cm > div:nth-child(%d) > div' % needDate.day

        # 点击选择出发时间输入框
        train_date = self.wait.until(EC.presence_of_element_located((By.ID, "train_date")))
        train_date.click()

        # 点击左边选择月份表
        month_list = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, 'body > div.cal-wrap > div:nth-child(1) > div.cal-top > div.month > input[type="text"]')))
        month_list.click()
        month = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_month)))
        month.click()

        get_date_list = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, css_day)))
        get_date_list.click()
        self.click_query()
        return needDate

    # 选择面板上的日期
    def select_date(self):
        action = ActionChains(self.browser)  # 使用浏览器动作模拟库
        move_to_date = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#date_range > ul > li:nth-child(3)")))
        action.move_to_element(move_to_date).perform()
        action.click(move_to_date).perform()

    # 输入出发地和目的地，可以手动添加地址
    def input_FromTo(self):
        fromStation = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#fromStationText")))
        fromStation.click()
        fromStation.clear()
        fromStation.send_keys('北京')
        fStation = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#citem_0 > span:nth-child(1)")))
        fStation.click()
        toStation = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#toStationText")))
        toStation.click()
        toStation.clear()
        toStation.send_keys('上海')
        tStation = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#citem_0 > span:nth-child(1)")))
        tStation.click()

    def get_detail_info(self, node):
        autoShift = {}
        data = []
        nodes = node.contents
        queryLeftTable = nodes[0].div.div.div.a.string  # 车班次，为key
        autoShift[queryLeftTable] = list()
        strong = nodes[0].select('strong')
        for i in range(0, 4):
            data.append(strong[i].string)

        for i in range(1, len(nodes)):
            try:
                if nodes[i].string != '--':
                    key = nodes[i].attrs['id'].split('_')[0]
                    str = self.ztype[nodes[i].attrs['id'].split('_')[0]] + ":" + nodes[i].string
                    data.append(str)
            except:
                pass
        autoShift[queryLeftTable] = data
        print(autoShift)

    def get_list(self, date):
        print('\n', date, ':')
        info = list()
        soup = BeautifulSoup(self.browser.page_source, 'lxml')
        soup = soup.select('#queryLeftTable')
        queryLeftTable = soup[0].select('tr[id^="ticket_"]')  # 返回列表，列表每个内容为一个节点tag
        for tr in queryLeftTable:
            self.get_detail_info(tr)

    def run(self):
        self.open_html()
        self.input_FromTo()
        for seq in range(0, 1):
            date = self.set_date(seq)
            time.sleep(1)
            self.get_list(date)
        # self.close_html()


Get12306 = Info12306()

Get12306.run()