# -*- coding: utf-8 -*-
# @Time : 2019/8/3,003 23:22
# @Author : 徐缘
# @FileName: check_device_amount.py
# @Software: PyCharm


""""在/root/shayxu_projects的路径下运行"""
# sys.path.append("/root/shayxu_projects")  # 项目目录
import sys
import socket
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

    # 获取本机ip
    address = socket.gethostbyname(socket.gethostname())

    if address == '117.144.106.34':
        # 部署环境位置
        es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                           ca_certs="/elasticsearch/elasticsearch-6.6.1/config/root-ca.pem")
    else:
        # Pycharm环境位置
        es = Elasticsearch("https://117.144.106.34:9200", http_auth=('admin', 'Cl0lTaULdjw0uVcH4S1N'),
                           ca_certs=r"../../../elasticsearch_key/root-ca.pem")
    # print(es.info())

    test_flag = 0
    try:
        test_flag = sys.argv[1]
    except IndexError:
        print()
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
            "query": {
                "bool": {
                    "filter": {
                        "range": {
                            "@timestamp": {
                                "gt": "now-5m",
                                "lt": "now"
                            }
                        }
                    }
                }
            },
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
                "query": {
                    "bool": {
                        "filter": {
                            "range": {
                                "@timestamp": {
                                    "gt": "now-5m",
                                    "lt": "now"
                                }
                            }
                        }
                    }
                },
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
            warning = warning + sorted(hostnames).__repr__() + '\n\r'
            # print(hostnames)
    print(warning)

    # exit()
    if len(warning) > 0:
        if address == '117.144.106.34' and not test_flag:
            user = ['xuyuan2@sh.chinamobile.com', 'wangyinchao@sh.chinamobile.com', 'yushu@sh.chinamobile.com',
                    'zhengsen@sh.chinamobile.com', 'zhouqihui@sh.chinamobile.com', 'chenhuanmin@sh.chinamobile.com',
                    'yangjie@sh.chinamobile.com', 'xiongyt@sh.chinamobile.com', 'wucaili@sh.chinamobile.com',
                    'dingy@sh.chinamobile.com', 'fenghongyu@sh.chinamobile.com', 'xuzicheng@sh.chinamobile.com', 'zhangzhongkaihy@139.com', 'zhangxuan7704@fiberhome.com', 'ranyinjiang@huawei.com',
                    'maojie9@huawei.com', 'wangzilongshb@126.com']
        else:
            user = ['xuyuan2@sh.chinamobile.com']
        # 'wuqian@sh.chinamobile.com','tanmiaomiao@sh.chinamobile.com', 'sufeng@sh.chinamobile.com'
        print(user, test_flag)
        ret = mm.mail139_mine('DoNotReply ELK日志服务器检查' + index_today, warning, user)

