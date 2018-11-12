import happybase
import website
connection = happybase.Connection('192.168.31.11',9090)
print(connection.tables())

table = connection.table('zengce',use_prefix=True)
for key, data in table.scan(row_start=None, row_stop=None, row_prefix=None, columns=None, filter=None, timestamp=None, include_timestamp=False, batch_size=1000, scan_batching=None, limit=None, sorted_columns=False, reverse=False):
    print(key,data)
print(11111111111111111)
print('\xc4\xe3\xba\xc3'.encode('utf-8').decode('utf-8'))