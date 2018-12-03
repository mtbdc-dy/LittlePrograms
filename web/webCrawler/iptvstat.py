import web.webCrawler.webcrawler as ww
import web.webCrawler.login
import myPackages.getime as mg
import datetime
import json

now = datetime.datetime.now()
# now = now.strftime('%Y-%m-%d')

cookie = 'JSESSIONID=6484322A55B024A63A382647BBA47671'

url = 'http://117.131.48.160:8080/iptvstat//rest/stat/shyd/vitalityUserCount'

for i in range(17):
    delta_begin = datetime.timedelta(days=i+1)
    delta_end = datetime.timedelta(days=i)
    tb = (now - delta_begin).strftime('%Y-%m-%d')
    te = (now - delta_end).strftime('%Y-%m-%d')
    # print(tb)
    # print(te)
    # print()

    form = {
        'beginTime': tb,
        'endTime': te,
        'city': '021,021_021',
        'userGroup': '1004',
        'convergeFlag': '0',
        'monthFlag': '0'
    }
    f = ww.post_web_page(url, form, cookie)
    # print(f)
    # print(type(f))
    encodedjson = json.loads(f)
    # print(encodedjson)
    print(encodedjson['message'][0]['cycle'], encodedjson['message'][0]['activeUserCount'], encodedjson['message'][0]['activeUserPrecent'])


    # exit()

