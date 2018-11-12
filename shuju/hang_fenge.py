from jieba import analyse
f=open("F:\新闻.txt","r",encoding="utf-8")
while True:
    line=f.readline()
    #print(line)
    tfidf = analyse.extract_tags
    keywords = tfidf(line)
    print(keywords)
    if not line:break

f.close()