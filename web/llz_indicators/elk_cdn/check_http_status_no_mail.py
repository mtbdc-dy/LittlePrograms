# -*- coding: utf-8 -*-
# @Time : 2019-08-18 09:02
# @Author : 徐缘
# @FileName: check_http_status_no_mail.py
# @Software: PyCharm


"""cdn_httpstatus.py"""

import csv
import datetime

from elasticsearch import Elasticsearch
import myPackages.mailtools as mm


if __name__ == '__main__':

    test_flag = 1
    companies = ['huawei', 'hy', 'fonsview', 'zte', 'huaweiott']  # 平面
    companies_cdn = ['huawei', 'hy', 'fonsview', 'zte']  # CSV 不统计OTT

    # 获取昨日日期
    index_today = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y.%m.%d')
    index_today_csv = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime('%Y.%m.%d')
    print(index_today_csv)
    # 修改前 2019.08.10,32561,374220422
    # 修改后 2019.08.10,32561,374220422
    # 部署环境位置
    es = Elasticsearch("https://117.144.106.35:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                       ca_certs="/elasticsearch/elasticsearch-6.6.1/config/root-ca.pem")
    print(es.info())

    warning = ''
    # 查询ELK
    companies_count = dict()
    companies_domain = dict()
    # 查询总文件数
    for item in companies:
        querybody = {
            "size": 0,
            "query": {
                "bool": {
                    "must": [
                        {
                            "wildcard": {
                                "httpstatus": "???"
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
            }
        }

        response_byte = es.search(index=item + '_sh' + index_today, body=querybody)
        # print(response_byte)
        total = int(response_byte['hits']['total'])
        # print(total)
        companies_count[item] = [total]
    print("各平面总文件数", companies_count)

    # 5XX个数
    for item in companies:
        querybody = {
            "size": 0,
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
        # print(response_byte)
        error_status_count = int(response_byte["hits"]["total"])
        companies_count[item].append(error_status_count)
        failure_rate = companies_count[item][1] / companies_count[item][0]
        print(item, failure_rate)
        if failure_rate > 0.0005:
            warning = warning + "{}: {:.2f}%  Total: {}  5XX: {}\n".format(
                item, failure_rate * 100, companies_count[item][0], companies_count[item][1])
            companies_domain[item] = response_byte["aggregations"]["NAME"]["buckets"]
    print(warning)

    # 打开输出文件
    f = open("httpstatus/data/cdn_httpstatus_" + index_today_csv + '.csv', 'w')
    writer = csv.writer(f)

    csv_content = [index_today, sum(companies_count[x][1] for x in companies_cdn),
                   sum(companies_count[x][0] for x in companies_cdn)]
    writer.writerow(csv_content)

    # 邮件告警
    warning = warning + '\n' + companies_domain.__repr__()

    if len(companies_domain) > 0:
        if not test_flag:
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
        ret = mm.mail139_mine('DoNotReply 服务成功率超阈值告警byELK' + index_today, warning, user)

