import hashlib
import webCrawler.webcrawler
import datetime
'''
爬取 数据网管 http://10.221.18.3:8080/passport/service/logon.form
模拟登入实在是太烦了=。=
复制一个 JSESSIONID 就好了，但是要比较靠近取数据的地方
取BaseReportServlet的JSESSIONID
但是好像意义不大，，，能取到这个JESSIONID了我还去复制来跑个鸡儿程序

1、周一要取前三天
2、对取出的数据进行判断是否超过。输出成易于复制的格式
'''

# 本省内容满足率(日报)
# part 1
# 获取 report_key
now = datetime.datetime.now()
yesterday = now - datetime.timedelta(days=1)
date = yesterday.strftime('%Y-%m-%d')
url = 'http://10.221.18.3:8080/report_data/report2?reportType=report_2016031701&user=admin&timeList=' + date + '&timetype=oneday&list=&ywlist=undefined&vendor=&pageCondition=no,no&startTimeStamp=0&endTimeStamp=24&isNewWin=false&isConvergence=no&timeis=no'
cookie = 'JSESSIONID=BD9A853612FCF064238D8CBDFC9429AA'
cookie = 'JSESSIONID=2E526B07AC1D353A51FE028CEAEE83F8'
f = webCrawler.webcrawler.get_web_page(url, cookie)
# print(f)
a = f.find('window.location.href =')
print(f[a+65:a+105])
report_key = f[a+65:a+105]

# part 2
# 传输数据
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet'

form = {
    'reportKey': report_key,
    '_gt_json': '{"recordType":"object","pageInfo":{"pageSize":25,"pageNum":1,"totalRowNum":-1,"totalPageNum":0,"startRowNum":1,"endRowNum":-1},"columnInfo":[{"id":"TIME_STAMP","header":"时间","fieldName":"TIME_STAMP","fieldIndex":"TIME_STAMP","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"ALL_KPI_2","header":"本省内容满足率-算法2(总)(%)","fieldName":"ALL_KPI_2","fieldIndex":"ALL_KPI_2","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"ALL_KPI","header":"本省内容满足率(总)(%)","fieldName":"ALL_KPI","fieldIndex":"ALL_KPI","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"WEBCACHE_KPI","header":"本省内容满足率(WEB CACHE)(%)","fieldName":"WEBCACHE_KPI","fieldIndex":"WEBCACHE_KPI","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IDC_KPI","header":"本省内容满足率(IDC)(%)","fieldName":"IDC_KPI","fieldIndex":"IDC_KPI","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"TIETONG_KPI","header":"本省内容满足率(铁通)(%)","fieldName":"TIETONG_KPI","fieldIndex":"TIETONG_KPI","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"CACHE_CDN_UTILITY","header":"其中CACHE/CDN上联端口流量占比(%)","fieldName":"CACHE_CDN_UTILITY","fieldIndex":"CACHE_CDN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"HUAWEI_UTILITY","header":"其中华为(%)","fieldName":"HUAWEI_UTILITY","fieldIndex":"HUAWEI_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"LINGDIAN_UTILITY","header":"其中灵点(%)","fieldName":"LINGDIAN_UTILITY","fieldIndex":"LINGDIAN_UTILITY","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"CITY_TRAFFIC","header":"地市入流量(Gbps)","fieldName":"CITY_TRAFFIC","fieldIndex":"CITY_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"CACHE_CDN","header":"CACHE/CDN上联核心层端口流量(Gbps)","fieldName":"CACHE_CDN","fieldIndex":"CACHE_CDN","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"WEB_CACHE","header":"WEB CACHE流量(Gbps)","fieldName":"WEB_CACHE","fieldIndex":"WEB_CACHE","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"IDC_TRAFFIC","header":"IDC服务本省流量(Gbps)","fieldName":"IDC_TRAFFIC","fieldIndex":"IDC_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"TIETONG_TRAFFIC","header":"铁通入流量(Gbps)","fieldName":"TIETONG_TRAFFIC","fieldIndex":"TIETONG_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"HUAWEI_TRAFFIC","header":"其中华为流量(Gbps)","fieldName":"HUAWEI_TRAFFIC","fieldIndex":"HUAWEI_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true},{"id":"LINGDIAN_TRAFFIC","header":"其中灵点流量(Gbps)","fieldName":"LINGDIAN_TRAFFIC","fieldIndex":"LINGDIAN_TRAFFIC","sortOrder":null,"hidden":false,"exportable":true,"printable":true}],"sortInfo":[],"filterInfo":[],"remotePaging":true,"parameters":{},"action":"load"}'
}
webCrawler.webcrawler.post_web_page(url, form, cookie)

# part 3
# 下载表单
url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=' + report_key + '&export=excel'
print(url)
# url = 'http://10.221.18.3:8080/report_data/BaseReportServlet?reportKey=_report_8a5d92926424f7eb016464871a770a77&export
# =excel'
# print(url)
f = webCrawler.webcrawler.download_web_page(url, cookie)

filename = '本省内容满足率.csv'
g = open(filename, 'wb')
g.write(f)
g.close()
