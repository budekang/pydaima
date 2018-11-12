import jieba
with open ("F:\geci.txt","r",encoding="utf-8") as f:
    content=f.read()
fenci=jieba.lcut(content)
hist={}
for word in fenci:
    if len(word)==1:
        continue
    if word in hist:
        hist[word]+=1
    else:
        hist[word]=1

histlist=list(hist.items())
histlist.sort(key=lambda x:x[1],reverse=True)
print(histlist)

for i in range(30):
    word,count=histlist[i]
    print("{:<10}{:>5}".format(word,count))