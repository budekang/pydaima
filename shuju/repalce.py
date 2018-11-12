with open("./result.txt","r",encoding="utf-8") as f:
    lines = f.readlines()
#写的方式打开文件
with open("./result.txt","w",encoding="utf-8") as f_w:
    for line in lines:
        if "2" in line:
         #替换
            line = line.replace("2","1")
        f_w.write(line)