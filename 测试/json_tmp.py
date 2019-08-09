# -*- coding: utf-8 -*-
import json

"PASTE JSON STRING HERE"
s = r'{"result":{"total":1,"startRow":0,"rowsTotal":1,"pageSize":15,"list":[{"pro_total_click":8515775625,"icp_accuracy_var":0.0316,"etl_date":"20190805","wlan_23g_yuliu_times":457855941,"third_cdn_times":51401141,"innet_others":210434045,"icp_accuracy":0.9029,"zhuanxian_times":249352317,"tietong_times":28602335,"outnet_times":141702673,"idc_zl_accuracy":0.8969,"idc_click":4660857379,"province":"200000","self_cache_cdn_times":16844736,"accuracy_innet_rate":0.9834,"innet_direct_times":2698725058}],"pageno":1}}'
tmp_dict = json.loads(s)

# Basic Struture

tmp_dict = tmp_dict['result']['list'][0]['icp_accuracy']
print(tmp_dict.keys())
for item in tmp_dict.keys():
    print(tmp_dict[item])
exit()

"EDIT SCRIPT FROM HERE"
download_rate = tmp_dict['message']['messageline']

userdownload = 0
for item in download_rate:
    userdownload += float(item['userdownload'])
userdownload = userdownload/len(download_rate)/1024/1024
print(userdownload)
exit()
a = lambda x: x['data_rate']['value']
print(round(max(list(map(a, [x for x in elk_rate_dict])))/1024/1024/1024/300*8, 2))
# map(函数，列表) 函数是用来计算的函数，列表是用来输入的

