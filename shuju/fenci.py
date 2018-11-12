import jieba
text="中华人民共和国国歌"
result=jieba.cut(text)
print("切分结果:  "+",".join(result))