#coding=utf-8
import os
filedir = os.getcwd()+'\zengce'
print(filedir)
fillenames = os.listdir(filedir)
f=open('zengces.txt','w')
for filename in fillenames:
    filepath=filedir+'/'+filename
    for line in open(filepath):
        f.write(filename+'@')
        f.writelines(line)
        f.write('\n')
f.close()