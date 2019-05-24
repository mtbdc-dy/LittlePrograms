# -*- coding: utf-8 -*-
# @Time : 2019/5/24,024 15:33
# @Author : 徐缘
# @FileName: elasticsearch_hello.py
# @Software: PyCharm


from elasticsearch import Elasticsearch

"""
    没用吧，和我直接发请求没啥本质区别。
"""

es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'www.10086.cn-Xman'), ca_certs="/elasticsearch/elasticsearch-6.5.3/config/key/root-ca.pem")
print(es.info())

