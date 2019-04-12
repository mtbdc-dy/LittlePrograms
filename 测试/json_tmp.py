import json

"PASTE JSON STRING HERE"
s = r'{"paramData":"{\"location\": 4, \"secFrom\": \"2019-04-11 00:00:00\", \"secTo\": \"2019-04-11 00:00:00\", \"dimension\": \"1\",\"idfilter\": \"4\", \"type\": \"activeuser\", \"dataType\": \"1\"}","resultData":"[{\"date\":\"2019-04-11\",\"StreamSTBs\":\"125507\",\"ActiveSTBs\":\"441300\",\"TotalDevices\":\"909035\",\"maxStreamSTBs\":\"83767\",\"maxActiveSTBs\":\"366792\"}]"}'
tmp_dict = json.loads(s)

# Basic Struture

# print(tmp_dict.keys())
# for item in tmp_dict.keys():
#     print(tmp_dict[item])
# exit()

"EDIT SCRIPT FROM HERE"
sqm_dict = json.loads(tmp_dict['resultData'])
print(sqm_dict[0]['maxActiveSTBs'], sqm_dict[0]['TotalDevices'], sqm_dict[0]['maxStreamSTBs'])
