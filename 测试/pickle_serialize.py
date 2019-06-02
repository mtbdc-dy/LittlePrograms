import pickle


# pickle 序列化
dic = {'age': 23, 'job': 'student'}
byte_data = pickle.dumps(dic)
# out -> b'\x80\x03}q\x00(X\x03\x00\x00\...'
print(byte_data)
dic_1 = pickle.loads(byte_data)
print(dic_1)
