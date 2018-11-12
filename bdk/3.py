from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'192.168.31.78','port':9200}])
index = "haidianqaik"
query = {"query": {"match_all": {}}}# 搜索所有数据
resp = es.search(index, body=query)
resp_docs = resp["hits"]["hits"]#符合的所有数据文档
total = resp['hits']['total']
print(total)#数据条数
#####################
a=input("输入a:")
query = {"query":{"term":{"message":a}}}#查询two字段为a的
resp1 = es.search(index, body=query)
resp_docs1 = resp1["hits"]["hits"]
total1 = resp1['hits']['total']

print(resp_docs1)
print(total1)
##########################

b=input("输入b:")
c=input("输入c:")
query = {"query":{"terms":{"message":[b,c]}}}#查询two字段为b.c的
resp2 = es.search(index, body=query)
resp_docs2 = resp1["hits"]["hits"]
total2 = resp2['hits']['total']

print(resp_docs2)
print(total2)
