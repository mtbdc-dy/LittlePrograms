import json


a = 1.43
s = r'{"paramData":"{\"secFrom\":\"2019-01-16 00:00:00\",\"secTo\":\"2019-01-16 00:00:00\",\"location\":4,\"dimension\":\"platform\",\"platform\":\"\",\"tType\":2,\"isMigu\":false,\"isMiguShanxi\":false,\"bIncludeShanxi\":false}","resultData":"{\"vod\":[{\"Count\":220062,\"FaultID\":0,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":220062,\"Dimensionality\":0},{\"Count\":111677,\"FaultID\":1,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":3281311,\"Dimensionality\":0},{\"Count\":2878,\"FaultID\":2,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":265388300812,\"Dimensionality\":0},{\"Count\":2930,\"FaultID\":3,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":66831,\"Dimensionality\":0},{\"Count\":5080,\"FaultID\":4,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":13262575375,\"Dimensionality\":0},{\"Count\":2968,\"FaultID\":5,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":52806283,\"Dimensionality\":0},{\"Count\":5465,\"FaultID\":6,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":323864041,\"Dimensionality\":0},{\"Count\":5548,\"FaultID\":7,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":150459,\"Dimensionality\":0},{\"Count\":5446,\"FaultID\":8,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":149745,\"Dimensionality\":0},{\"Count\":5465,\"FaultID\":14,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":109408774977957,\"Dimensionality\":0},{\"Count\":2930,\"FaultID\":15,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":8310,\"Dimensionality\":0},{\"Count\":16,\"FaultID\":0,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":16,\"Dimensionality\":1},{\"Count\":7,\"FaultID\":1,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":404,\"Dimensionality\":1},{\"Count\":176653,\"FaultID\":0,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":176653,\"Dimensionality\":2},{\"Count\":139787,\"FaultID\":1,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":4905571,\"Dimensionality\":2},{\"Count\":29556,\"FaultID\":2,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":5934325688524,\"Dimensionality\":2},{\"Count\":29908,\"FaultID\":3,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":475655,\"Dimensionality\":2},{\"Count\":178101,\"FaultID\":4,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":231436654720,\"Dimensionality\":2},{\"Count\":178165,\"FaultID\":5,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":4061676999,\"Dimensionality\":2},{\"Count\":182051,\"FaultID\":6,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":5549867631,\"Dimensionality\":2},{\"Count\":184108,\"FaultID\":7,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":4456473,\"Dimensionality\":2},{\"Count\":180722,\"FaultID\":8,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":4376433,\"Dimensionality\":2},{\"Count\":182018,\"FaultID\":14,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":1288108741231982,\"Dimensionality\":2},{\"Count\":29908,\"FaultID\":15,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":57374,\"Dimensionality\":2},{\"Count\":51,\"FaultID\":0,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":51,\"Dimensionality\":3},{\"Count\":104,\"FaultID\":1,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"Total\":6931,\"Dimensionality\":3}],\"net\":[{\"LocationID\":4,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"DistStreamDevice\":\"1#124347@2#89030@3#453\"}],\"epg\":[{\"Requests\":20284166,\"CntEpgRspTime\":8669404,\"Responses\":20027669,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"TotEpgRspTime\":189937047966,\"Dimensionality\":1}],\"epgSuc\":[{\"Requests\":260772,\"CntEpgRspTime\":154542,\"Responses\":256764,\"KPIUTCSec\":{\"date\":16,\"day\":3,\"hours\":0,\"minutes\":0,\"month\":0,\"nanos\":0,\"seconds\":0,\"time\":1547568000000,\"timezoneOffset\":-480,\"year\":119},\"LocationID\":4,\"TotEpgRspTime\":9442940307,\"Dimensionality\":1}]}"}'
d = json.loads(s)
# print(d)
# for item in d['resultData']:
#     print(item)
# print(d['resultData'])
# print(len(d['resultData']))
# print(type(d['resultData']))
d = json.loads(d['resultData'])


# print(d['vod'])
print(len(d))
print(d.keys())

print(d['net'])
print(d['epg'])
print(d['epgSuc'])
count = 0
total = 0
total_all = 0
total_suc = 0
for item in d['vod']:
    if item['FaultID'] == 3:
        print(item['Count'])
        print(item['Total'])
        print(item['Count']/item['Total'])
        print(item['Total']/item['Count'])
        count += int(item['Count'])
        total += int(item['Total'])

    if item['FaultID'] == 7:
        print(item['Total'])
        total_all += int(item['Total'])
        
    if item['FaultID'] == 8:
        total_suc += int(item['Total'])
    # print(item['FaultID'], item['Dimensionality'])
    # print(item['Count'], item['Total'])
    # print(item['Count']/item['Total'])
    # print(item['Total'] / item['Count'])
    # print(item)
    # print(item['Count'])
    # print(item['Total'])
    # print((int(item['Count'])/int(item['Total'])*100))
    print()

print(count / total * 100, count, total)
print(total / count * 100, count, total)
print(total_all, total_suc/total_all)

