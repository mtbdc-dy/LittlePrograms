import os
filename = '../web/webCrawler/inter_network_flow.xls'
(filepath,tempfilename) = os.path.split(filename)
print(tempfilename)
print(tempfilename.split('.')[0])

