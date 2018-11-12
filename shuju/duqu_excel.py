import xlrd
from datetime import date,datetime
#def read_excel():
#    excelfile=xlrd.open_workbook(r'F:\聚餐美食北京大众点评网.xls')
 #   pass
data = xlrd.open_workbook(r'F:\聚餐美食北京大众点评网.xls')
sqlfile = open("1.txt", "a") # 文件读写方式是追加
table = data.sheets()[0] # 表头
nrows = table.nrows  # 行数
ncols = table.ncols  # 列数
colnames = table.row_values(0)  # 某一行数据
# 打印出行数列数
print(nrows)
print(ncols)
print(colnames)
