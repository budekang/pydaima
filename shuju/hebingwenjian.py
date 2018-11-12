#coding=utf-8
import os
#获取目标文件夹的路径
filedir = os.getcwd()+'\yuliao'
#print(filedir)
#获取当前文件夹中的文件名称列表
filenames=os.listdir(filedir)
#print(filenames)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('E:\pycharm\Pycharm\shuju\yuliao/result.txt','a',encoding='utf-8')

path = os.listdir(os.getcwd())
#显示当前目录下的所有文件和文件夹
#print (path)
for filedir in path:


#先遍历文件名
    for filename in filenames:
        filepath = filedir+'/'+filename
        #print(filepath)
        #遍历单个文件，读取行
        for line in open(filepath):
            #print(line)
            f.writelines(filepath+","+line)
            f.write('\n')
#print(f)
#关闭文件
f.close()