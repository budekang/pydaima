#coding=utf-8
import os
#获取目标文件夹的路径
#filedir = os.getcwd()+'\kangde'
#print(filedir)
#获取当前文件夹中的文件名称列表
#filenames=os.listdir(filedir)
#print(filenames)
#打开当前目录下的result.txt文件，如果没有则创建
f=open('E:\pycharm\Pycharm\shuju\kangde/result.txt','a',encoding='utf-8')

path = os.listdir(os.getcwd()+'\kangde')
#显示当前目录下的所有文件和文件夹
print (path)
for filedir in path:
    #print(filedir)#ONE
    path1 = os.getcwd()+'\kangde'+'\\'+filedir
    #print(path1)#E:\pycharm\Pycharm\shuju\kangde\one
    #先遍历文件名

    for filename in path1:
        path2 = os.listdir(path1)
        print(path2)
        #filepath = filedir+'/'+filename



        #print(path1)#E:\pycharm\Pycharm\shuju\kangde\one
        #print(filedir)#one
        #print(filename)
        #print(filepath)
        #遍历单个文件，读取行
        for wenjian in path2:
            print(wenjian)
            #pwd = os.getcwd()
            pwd="E:\pycharm\Pycharm\shuju"
            print(pwd)
            print(pwd+"/"+filedir+"/"+wenjian)
            for line in open(pwd+"\\"+filedir+"\\"+wenjian):
                print(line)
                f.writelines(path2+","+line)
                f.write('\n')
            #print(f)
            #关闭文件
    f.close()