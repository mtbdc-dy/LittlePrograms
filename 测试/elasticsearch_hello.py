# -*- coding: utf-8 -*-
# @Time : 2019-07-30 23:49
# @Author : 徐缘
# @FileName: elasticsearch_hello.py
# @Software: PyCharm


from elasticsearch import Elasticsearch

es = Elasticsearch("https://117.144.106.40:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                   ca_certs="../elasticsearch_key/root-ca.pem")

print(es.info())
# t o d o (Shay) Todo_hello

