# -*- coding: utf-8 -*-
# @Time : 2019-08-11 17:24
# @Author : 徐缘
# @FileName: domain_count.py
# @Software: PyCharm
"""
    数一数有几个域名
    python3 check_http_status.py 后跟任何字段都认为在测试。
"""
import sys
import socket       # 获取设备IP
import datetime

from elasticsearch import Elasticsearch
import myPackages.mailtools as mm


if __name__ == '__main__':
    # 常量
    companies_cdn = ['huawei', 'hy', 'fonsview', 'zte']  # CSV 不统计OTT

    # 获取昨日日期
    index_today = datetime.datetime.now()

    # 获取本机ip
    address = socket.gethostbyname(socket.gethostname())
    print(address)

    # 读取命令参数
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
    warning = ''

    # 查询ELK
    # 查询域名个数
    for i in range(7):
        query_day = (index_today - datetime.timedelta(days=7-i-1)).strftime('%Y.%m.%d')
        cdn_domain = dict()
        for item in companies_cdn:
            querybody ={
                "size": 0,
                "aggs": {
                    "type_count": {
                        "cardinality": {
                            "field": "reqdomain.keyword"
                        }
                    }
                }
            }

            response_byte = es.search(index=item + '_sh' + query_day, body=querybody)
            count = int(response_byte['aggregations']['type_count']['value'])
            cdn_domain[item] = count
        print(query_day, cdn_domain)
        warning = warning + query_day + cdn_domain.__repr__() + '\n'

    # 邮件告警
    print(warning)

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
    print(user)
    ret = mm.mail139_mine('DoNotReply 分发域名个数统计byELK' + index_today.strftime('%Y.%m.%d'), warning, user)

