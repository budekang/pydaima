from elasticsearch import Elasticsearch
es = Elasticsearch([{'host':'192.168.31.78','port':9200}])
index = "aa"
query = {"query": {"match_all": {}}}
resp = es.search(index, body=query)
resp_docs = resp["hits"]["hits"]
total = resp['hits']['total']

print(total)


#####################
body = {"query":{"term":{"four":"女"}}}
print(body)

