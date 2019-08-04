# -*- coding: utf-8 -*-
# @Time : 2019/8/3,003 23:22
# @Author : 徐缘
# @FileName: check_device_amount.py
# @Software: PyCharm


import datetime

from elasticsearch import Elasticsearch
import myPackages.mailtools as mm

if __name__ == '__main__':
    # 常量
    companies = ['huawei', 'hy', 'fonsview', 'zte', 'zteiptv', 'huaweiott', 'fonsviewott', 'fonsviewiptv']  # 平面
    companies = ['huawei', 'hy', 'fonsview', 'zte', 'huaweiott']  # 平面
    server_nums = {
        'huawei': 14,
        'hy': 17,
        'fonsview': 6,
        'zte': 21,
        'huaweiott': 13
    }

    es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                       ca_certs=r"../../../elasticsearch_key/root-ca.pem")

    # 部署环境位置
    # es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
    #                    ca_certs="/elasticsearch/elasticsearch-6.6.1/config/root-ca.pem")

    # print(es.info())

    index_today = datetime.datetime.now().strftime('%Y.%m.%d')
    # querybody = {
    #     "query": {
    #         "bool": {
    #             "must_not": [
    #                 {"term": {"cache_server_ip": "0"}},
    #                 {"term": {"cache_server_ip": "127.0.0.1"}}
    #             ]
    #         }
    #     },
    #     "aggs": {
    #         "type_count": {
    #             "cardinality": {
    #                 "field": "cache_server_ip.keyword"
    #             }
    #         }
    #     }
    # }
    warning = ''
    for item in server_nums.keys():
        querybody = {
            "size": 0,
            "aggs": {
                "type_count": {
                    "cardinality": {
                        "field": "beat.hostname.keyword"
                    }
                }
            }
        }
        response_byte = es.search(index=item+'_sh'+index_today, body=querybody)
        num = int(response_byte['aggregations']['type_count']['value'])
        if server_nums[item] != num:
            # print(item, 'current:', num, 'total:', server_nums[item])
            warning = warning + '[{}]current: {},total: {}\n'.format(item, num, server_nums[item])
            querybody = {
                "aggs": {
                    "hostname": {
                        "terms": {
                            "field": "beat.hostname.keyword",
                            "size": 30
                        }
                    }
                }
            }
            response_byte = es.search(index=item + '_sh' + index_today, body=querybody)
            hostname_list = response_byte["aggregations"]["hostname"]["buckets"]
            hostnames = [hostname_list[x]["key"] for x in range(0, len(hostname_list))]
            warning = warning + hostnames.__repr__() + '\n\r'
            # print(hostnames)

    print(warning)

    # if len(warning) > 0:
    #     user = ['xuyuan2@sh.chinamobile.com']
    #     ret = mm.mail139_mine('DoNotReply ELK日志服务器检查' + index_today, warning, user)

