import sys


a = b"\r\r\n\x00******************************************************************************\r\r\n* Copyright (c) 2004-2018 New H3C Technologies Co., Ltd. All rights reserved.*\r\r\n* Without the owner's prior written consent,                                 *\r\r\n* no decompiling or reverse-engineering shall be allowed.                    *\r\r\n******************************************************************************\r\r\n\r\r\n\x00<SHYP-PA-iCache-SW04-7606H3>dis arp\r\r\n  Type: S-Static   D-Dynamic   O-Openflow   R-Rule   M-Multiport  I-Invalid\r\r\nIP address      MAC address    VID        Interface                Aging Type \r\r\n221.181.104.105 3c15-fb5d-122b N/A        RAGG1                    1181  D    \r\r\n117.143.109.122 a4be-2b65-0dad 15         BAGG101                  425   D    \r\r\n"
a = a.replace(b'\r\r\n', b'\r\n')
a = a.replace(b'\x00', b'')
print(a.decode())
# print(type(a))
# print(a.decode())
# for item in a.decode():
#     if item is not None:
#         print(item)


