import web.webCrawler.webcrawler

'''
爬取 东信-Ip综合网管系统：http://10.221.18.3:8080/passport/service/logon.form
模拟登入实在是太烦了=。=
复制一个JSESSIONID就好了，但是要比较靠近取数据的地方
'''

month = '7'
week = ''

# CMNET出口数据统计报表
# part 1
# 获取 report_key
url = 'http://10.221.18.3:8080/report_data/report2?reportType=CMNET_OUT_FLOW_DATA&user=admin&timeList=2018-6&timetype=month&list=&ywlist=undefined&vendor=&pageCondition=no,no&startTimeStamp=0&endTimeStamp=24&isNewWin=false&isConvergence=no&timeis=no'
cookie = 'JSESSIONID=1ECE6622F22F4C012C97E8AF4C1997D2'
cookie = 'JSESSIONID=BD9A853612FCF064238D8CBDFC9429AA'
#
f = web.webCrawler.webcrawler.get_web_page(url, cookie)
# print(f)
a = f.find('window.location.href =')
print(f[a+65:a+105])
report_key = f[a+65:a+105]

# part 2
# 传输数据
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet'
form = {
    'reportKey': report_key,
    '_gt_json': '{"recordType":"object","pageInfo":{"pageSize":25,"pageNum":1,"totalRowNum":-1,"totalPageNum":0,"startRowNum":1,"endRowNum":-1},"columnInfo":[{"id":"TIME_STAMP","header":"统计时间","fieldName":"TIME_STAMP","fieldIndex":"TIME_STAMP","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MODULE_NAME","header":"模板名称","fieldName":"MODULE_NAME","fieldIndex":"MODULE_NAME","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"daikuan","header":"带宽(M)","fieldName":"daikuan","fieldIndex":"daikuan","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_TRAFFIC","header":"流入均值流速(Mbps)","fieldName":"IF_IN_TRAFFIC","fieldIndex":"IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_TRAFFIC","header":"流入峰值流速(Mbps)","fieldName":"MAX_IF_IN_TRAFFIC","fieldIndex":"MAX_IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_UTILITY","header":"流入均值利用率(%)","fieldName":"IF_IN_UTILITY","fieldIndex":"IF_IN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_UTILITY","header":"流入峰值利用率(%)","fieldName":"MAX_IF_IN_UTILITY","fieldIndex":"MAX_IF_IN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_TRAFFIC","header":"流出均值流速(Mbps)","fieldName":"IF_OUT_TRAFFIC","fieldIndex":"IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_TRAFFIC","header":"流出峰值流速(Mbps)","fieldName":"MAX_IF_OUT_TRAFFIC","fieldIndex":"MAX_IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_UTILITY","header":"流出均值利用率(%)","fieldName":"IF_OUT_UTILITY","fieldIndex":"IF_OUT_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_UTILITY","header":"流出峰值利用率(%)","fieldName":"MAX_IF_OUT_UTILITY","fieldIndex":"MAX_IF_OUT_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"liuruzij","header":"流入字节数(MB)","fieldName":"liuruzij","fieldIndex":"liuruzij","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"liucuzij","header":"流出字节数(MB)","fieldName":"liucuzij","fieldIndex":"liucuzij","sortOrder":null,"hidden":false,"exportable":true,"printable":true}],"sortInfo":[],"filterInfo":[],"remotePaging":true,"parameters":{},"action":"load"}'
}
web.webCrawler.webcrawler.post_web_page(url, form, cookie)

# part 3
# 下载表单
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=' + report_key + '&export=excel'
print(url)
# url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=_report_8a5d92926424f7eb016464871a770a77&export
# =excel'
# print(url)
f = web.webCrawler.webcrawler.download_web_page(url, cookie)

filename = 'CMNET出口数据统计报表.csv'
g = open(filename, 'wb')
g.write(f)
g.close()
# print(f)


# bras地址报表
filename = 'bras地址报表.csv'
# part 1
# 获取 report_key
url = 'http://10.221.18.3:8080/report_data/report2?reportType=cmnet_bras&user=admin&timeList=2018-25&timetype=week&li' \
      'st=&ywlist=undefined&vendor=&pageCondition=no,no&startTimeStamp=0&endTimeStamp=24&isNewWin=false&isConvergence' \
      '=no&timeis=no'
f = web.webCrawler.webcrawler.get_web_page(url, cookie)
a = f.find('window.location.href =')
report_key = f[a+65:a+105]
print(report_key)

# part 2
# 传输数据
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet'
form = {
    'reportKey': report_key,
    '_gt_json': '{"recordType":"object","pageInfo":{"pageSize":25,"pageNum":1,"totalRowNum":-1,"totalPageNum":0,"startRowNum":1,"endRowNum":-1},"columnInfo":[{"id":"time_stamp","header":"时间","fieldName":"time_stamp","fieldIndex":"time_stamp","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"DEVICE_NAME","header":"设备名称","fieldName":"DEVICE_NAME","fieldIndex":"DEVICE_NAME","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IPADDR","header":"IP地址","fieldName":"IPADDR","fieldIndex":"IPADDR","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"AllAddressNum","header":"移动宽带地址个数","fieldName":"AllAddressNum","fieldIndex":"AllAddressNum","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MaxOnlineUserNum","header":"移动宽带峰值用户数","fieldName":"MaxOnlineUserNum","fieldIndex":"MaxOnlineUserNum","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MaxAddrUsedRate","header":"移动宽带地址池峰值利用率(%)","fieldName":"MaxAddrUsedRate","fieldIndex":"MaxAddrUsedRate","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"busyTime","header":"移动宽带忙时","fieldName":"busyTime","fieldIndex":"busyTime","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"avgNum","header":"移动宽带均值","fieldName":"avgNum","fieldIndex":"avgNum","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"VpnAddressNum","header":"VPDN地址个数","fieldName":"VpnAddressNum","fieldIndex":"VpnAddressNum","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"VpnOnlineUserNum","header":"VPDN峰值用户数","fieldName":"VpnOnlineUserNum","fieldIndex":"VpnOnlineUserNum","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"VpnAddrUsedRate","header":"VPDN峰值地址池利用率%","fieldName":"VpnAddrUsedRate","fieldIndex":"VpnAddrUsedRate","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"VpnBusyTime","header":"VPDN忙时","fieldName":"VpnBusyTime","fieldIndex":"VpnBusyTime","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"VpnAvgNum","header":"VPDN均值","fieldName":"VpnAvgNum","fieldIndex":"VpnAvgNum","sortOrder":null,"hidden":false,"exportable":true,"printable":true}],"sortInfo":[],"filterInfo":[],"remotePaging":true,"parameters":{},"action":"load"}'
}
web.webCrawler.webcrawler.post_web_page(url, form, cookie)

# part 3
# 下载表单
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=' + report_key + '&export=excel'
f = web.webCrawler.webcrawler.download_web_page(url, cookie)
g = open(filename, 'wb')
g.write(f)
g.close()


# LNS上联
filename = 'LNS上联.csv'
# part 1
# 获取 report_key
url = 'http://10.221.18.3:8080/report_data/report3?reportType=Interface_Link_Flow&user=admin&starttime=&timetype=week&isNewWin=false&timeList=2018-25,&startTimeStamp=0&endTimeStamp=24&selectType=device'
f = web.webCrawler.webcrawler.get_web_page(url, cookie)
a = f.find('window.location.href =')
report_key = f[a+65:a+105]
print(report_key)

# part 2
# 传输数据
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet'
form = {
    'reportKey': report_key,
    '_gt_json': '{"recordType":"object","pageInfo":{"pageSize":25,"pageNum":1,"totalRowNum":-1,"totalPageNum":0,"startRowNum":1,"endRowNum":-1},"columnInfo":[{"id":"TIME_STAMP","header":"统计时间","fieldName":"TIME_STAMP","fieldIndex":"TIME_STAMP","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"CITY","header":"设备机房","fieldName":"CITY","fieldIndex":"CITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"SYS_NAME","header":"设备名称","fieldName":"SYS_NAME","fieldIndex":"SYS_NAME","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IP_ADDR","header":"设备IP地址","fieldName":"IP_ADDR","fieldIndex":"IP_ADDR","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_NAME","header":"端口名称","fieldName":"IF_NAME","fieldIndex":"IF_NAME","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_ALIAS","header":"端口别名","fieldName":"IF_ALIAS","fieldIndex":"IF_ALIAS","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"INTERFACE_IP_ADDR","header":"端口IP地址","fieldName":"INTERFACE_IP_ADDR","fieldIndex":"INTERFACE_IP_ADDR","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"daikuan","header":"带宽(M)","fieldName":"daikuan","fieldIndex":"daikuan","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_TRAFFIC","header":"流入均值流速(Mbps)","fieldName":"IF_IN_TRAFFIC","fieldIndex":"IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_TRAFFIC","header":"流入峰值流速(Mbps)","fieldName":"MAX_IF_IN_TRAFFIC","fieldIndex":"MAX_IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_UTILITY","header":"流入均值利用率(%)","fieldName":"IF_IN_UTILITY","fieldIndex":"IF_IN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_UTILITY","header":"流入峰值利用率(%)","fieldName":"MAX_IF_IN_UTILITY","fieldIndex":"MAX_IF_IN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_TRAFFIC","header":"流出均值流速(Mbps)","fieldName":"IF_OUT_TRAFFIC","fieldIndex":"IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_TRAFFIC","header":"流出峰值流速(Mbps)","fieldName":"MAX_IF_OUT_TRAFFIC","fieldIndex":"MAX_IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_UTILITY","header":"流出均值利用率(%)","fieldName":"IF_OUT_UTILITY","fieldIndex":"IF_OUT_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_UTILITY","header":"流出峰值利用率(%)","fieldName":"MAX_IF_OUT_UTILITY","fieldIndex":"MAX_IF_OUT_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"liuruzij","header":"流入字节数(MByte)","fieldName":"liuruzij","fieldIndex":"liuruzij","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"liucuzij","header":"流出字节数(MByte)","fieldName":"liucuzij","fieldIndex":"liucuzij","sortOrder":null,"hidden":false,"exportable":true,"printable":true}],"sortInfo":[],"filterInfo":[],"remotePaging":true,"parameters":{},"action":"load"}'
}
web.webCrawler.webcrawler.post_web_page(url, form, cookie)

# part 3
# 下载表单
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=' + report_key + '&export=excel'
f = web.webCrawler.webcrawler.download_web_page(url, cookie)
g = open(filename, 'wb')
g.write(f)
g.close()


# 城域网出口电路组5T
url = 'http://10.221.18.3:8080/report_data/report3?reportType=Interface_Link_Flow&user=admin&starttime=&timetype=month&isNewWin=false&timeList=2018-6,&startTimeStamp=0&endTimeStamp=24&selectType=device'
json = '{"recordType":"object","pageInfo":{"pageSize":25,"pageNum":1,"totalRowNum":-1,"totalPageNum":0,"startRowNum":1,"endRowNum":-1},"columnInfo":[{"id":"TIME_STAMP","header":"统计时间","fieldName":"TIME_STAMP","fieldIndex":"TIME_STAMP","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"CITY","header":"设备机房","fieldName":"CITY","fieldIndex":"CITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"SYS_NAME","header":"设备名称","fieldName":"SYS_NAME","fieldIndex":"SYS_NAME","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IP_ADDR","header":"设备IP地址","fieldName":"IP_ADDR","fieldIndex":"IP_ADDR","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_NAME","header":"端口名称","fieldName":"IF_NAME","fieldIndex":"IF_NAME","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_ALIAS","header":"端口别名","fieldName":"IF_ALIAS","fieldIndex":"IF_ALIAS","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"INTERFACE_IP_ADDR","header":"端口IP地址","fieldName":"INTERFACE_IP_ADDR","fieldIndex":"INTERFACE_IP_ADDR","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"daikuan","header":"带宽(M)","fieldName":"daikuan","fieldIndex":"daikuan","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_TRAFFIC","header":"流入均值流速(Mbps)","fieldName":"IF_IN_TRAFFIC","fieldIndex":"IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_TRAFFIC","header":"流入峰值流速(Mbps)","fieldName":"MAX_IF_IN_TRAFFIC","fieldIndex":"MAX_IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_UTILITY","header":"流入均值利用率(%)","fieldName":"IF_IN_UTILITY","fieldIndex":"IF_IN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_UTILITY","header":"流入峰值利用率(%)","fieldName":"MAX_IF_IN_UTILITY","fieldIndex":"MAX_IF_IN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_TRAFFIC","header":"流出均值流速(Mbps)","fieldName":"IF_OUT_TRAFFIC","fieldIndex":"IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_TRAFFIC","header":"流出峰值流速(Mbps)","fieldName":"MAX_IF_OUT_TRAFFIC","fieldIndex":"MAX_IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_UTILITY","header":"流出均值利用率(%)","fieldName":"IF_OUT_UTILITY","fieldIndex":"IF_OUT_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_UTILITY","header":"流出峰值利用率(%)","fieldName":"MAX_IF_OUT_UTILITY","fieldIndex":"MAX_IF_OUT_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"liuruzij","header":"流入字节数(MByte)","fieldName":"liuruzij","fieldIndex":"liuruzij","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"liucuzij","header":"流出字节数(MByte)","fieldName":"liucuzij","fieldIndex":"liucuzij","sortOrder":null,"hidden":false,"exportable":true,"printable":true}],"sortInfo":[],"filterInfo":[],"remotePaging":true,"parameters":{},"action":"load"}'
filename = '城域网出口电路组5T.csv'
web.webCrawler.webcrawler.get_excel(url, cookie, json, filename)

# CMNET出口分析报表
url = 'http://10.221.18.3:8080/report_data/report?reportType=CMNET_exports_Analysis&user=admin&timeList=2018-6,&timetype=month&hour=&isNewWin=false&startTimeStamp=0&endTimeStamp=24&timeis=no'
json = '{"recordType":"object","pageInfo":{"pageSize":25,"pageNum":1,"totalRowNum":-1,"totalPageNum":0,"startRowNum":1,"endRowNum":-1},"columnInfo":[{"id":"time","header":"时间","fieldName":"time","fieldIndex":"time","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"module_name","header":"出口类型","fieldName":"module_name","fieldIndex":"module_name","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"daikuan","header":"带宽","fieldName":"daikuan","fieldIndex":"daikuan","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_IN_TRAFFIC","header":"本月流入均值（Gbps)","fieldName":"IF_IN_TRAFFIC","fieldIndex":"IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"SIF_IN_TRAFFIC","header":"上月流入均值（Gbps)","fieldName":"SIF_IN_TRAFFIC","fieldIndex":"SIF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"Chain_growth_in","header":"环比增长率%(流入)","fieldName":"Chain_growth_in","fieldIndex":"Chain_growth_in","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IF_OUT_TRAFFIC","header":"本月流出均值（Gbps)","fieldName":"IF_OUT_TRAFFIC","fieldIndex":"IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"SIF_OUT_TRAFFIC","header":"上月流出均值（Gbps)","fieldName":"SIF_OUT_TRAFFIC","fieldIndex":"SIF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"Chain_growth_out","header":"环比增长率%(流出)","fieldName":"Chain_growth_out","fieldIndex":"Chain_growth_out","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_IN_TRAFFIC","header":"本月流入峰值（Gbps)","fieldName":"MAX_IF_IN_TRAFFIC","fieldIndex":"MAX_IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"SMAX_IF_IN_TRAFFIC","header":"上月流入峰值（Gbps)","fieldName":"SMAX_IF_IN_TRAFFIC","fieldIndex":"SMAX_IF_IN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"Chain_growth_min","header":"环比增长率%(峰值流入)","fieldName":"Chain_growth_min","fieldIndex":"Chain_growth_min","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"MAX_IF_OUT_TRAFFIC","header":"本月流出峰值（Gbps)","fieldName":"MAX_IF_OUT_TRAFFIC","fieldIndex":"MAX_IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"SMAX_IF_OUT_TRAFFIC","header":"上月流出峰值（Gbps)","fieldName":"SMAX_IF_OUT_TRAFFIC","fieldIndex":"SMAX_IF_OUT_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"Chain_growth_mout","header":"环比增长率%(峰值流)","fieldName":"Chain_growth_mout","fieldIndex":"Chain_growth_mout","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"utility","header":"峰值利用率(%)","fieldName":"utility","fieldIndex":"utility","sortOrder":null,"hidden":false,"exportable":true,"printable":true}],"sortInfo":[],"filterInfo":[],"remotePaging":true,"parameters":{},"action":"load"}'
filename = 'CMNET出口分析报表.csv'
web.webCrawler.webcrawler.get_excel(url, cookie, json, filename)
