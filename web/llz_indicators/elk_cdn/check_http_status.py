# -*- coding: utf-8 -*-
# @Time : 2019-08-11 10:50
# @Author : 徐缘
# @FileName: check_http_status.py
# @Software: PyCharm


import sys
import socket
import datetime

"""
    python3 check_http_status.py 后跟任何字段都认为在测试。2
"""

from elasticsearch import Elasticsearch
import myPackages.mailtools as mm

if __name__ == '__main__':
    # 常量
    companies = ['huawei', 'hy', 'fonsview', 'zte', 'zteiptv', 'huaweiott', 'fonsviewott', 'fonsviewiptv']  # 平面
    companies = ['huawei', 'hy', 'fonsview', 'zte', 'huaweiott']  # 平面

    # 获取本机ip
    address = socket.gethostbyname(socket.gethostname())
    print(address)

    test_flag = 0
    try:
        test_flag = sys.argv[1]
    except IndexError:
        print()

    if address == '117.144.106.34':
        # 部署环境位置
        es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                           ca_certs="/elasticsearch/elasticsearch-6.6.1/config/root-ca.pem")
    else:
        # Pycharm环境位置
        es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                           ca_certs=r"../../../elasticsearch_key/root-ca.pem")
    # print(es.info())

    index_today = datetime.datetime.now().strftime('%Y.%m.%d')
    warning = ''

    for item in companies:
        # 5XX占比
        querybody = {
            "query": {
                "bool": {
                    "must": [
                        {
                            "wildcard": {
                                "httpstatus": "5??"
                            }
                        }
                    ],
                    "must_not": [
                        {
                            "term": {
                                "cache_server_ip": "127.0.0.1"
                            }
                        }
                    ]
                }
            },
            "aggs": {
                "NAME": {
                    "terms": {
                        "field": "reqdomain.keyword",
                        "size": 3
                    }
                }
            }
        }

        response_byte = es.search(index=item+'_sh'+index_today, body=querybody)
        num = int(response_byte['aggregations']['type_count']['value'])



    print(warning)

    # exit()
    if len(warning) > 0:
        if address == '117.144.106.34' and not test_flag:
            user = ['xuyuan2@sh.chinamobile.com', 'wangyinchao@sh.chinamobile.com', 'yushu@sh.chinamobile.com',
                    'zhengsen@sh.chinamobile.com', 'zhouqihui@sh.chinamobile.com', 'chenhuanmin@sh.chinamobile.com',
                    'yangjie@sh.chinamobile.com', 'xiongyt@sh.chinamobile.com', 'wucaili@sh.chinamobile.com',
                    'dingy@sh.chinamobile.com', 'fenghongyu@sh.chinamobile.com', 'xuzicheng@sh.chinamobile.com',
                    'zhangzhongkaihy@139.com', 'zhangxuan7704@fiberhome.com', 'ranyinjiang@huawei.com',
                    'maojie9@huawei.com', 'wangzilongshb@126.com']
        else:
            user = ['xuyuan2@sh.chinamobile.com']
        # 'wuqian@sh.chinamobile.com','tanmiaomiao@sh.chinamobile.com', 'sufeng@sh.chinamobile.com'
        ret = mm.mail139_mine('DoNotReply 服务器成功率byELK' + index_today, warning, user)

