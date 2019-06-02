import rsa
import base64

"""
rsa 加密
"""

s = '010001'
s = int(s, 16)
print(s)
key = rsa.newkeys(1024)
print(key[0])
print(rsa)

e = 0x010001
m = 0x009261853514e1ba484e26087ded5280cf70464be95b8af2a5f9c3c64c19f26c6bafb87af39ccc1a52afa210a56f144a2f7edd7aee99296d5186e5049e6592d96b56a8c399f295d6d06e76675cb5957f350bfa7ee414edcd20323bc4c145aedd9a071356315b25e7962eac2e662cfffb7565a75309f0e11add69578a94cd06c479

print(rsa.key.PublicKey(m, e))
id = 'pdsjdlz'
massage = rsa.encrypt(id.encode(), rsa.key.PublicKey(m, e))

print(massage)
print(base64.b64encode(massage))
