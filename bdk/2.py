from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'192.168.31.78','port':9200}])
index = "aa"
query = {"query": {"match_all": {}}}# 搜索所有数据
resp = es.search(index, body=query)
resp_docs = resp["hits"]["hits"]#符合的所有数据文档
total = resp['hits']['total']
print(total)#数据条数

#####################
a=input("输入a:")
query = {"query":{"term":{"two":a}}}#查询two字段为a的
resp1 = es.search(index, body=query)
resp_docs1 = resp1["hits"]["hits"]
total1 = resp1['hits']['total']

print(resp_docs1)
print(total1)
##########################


