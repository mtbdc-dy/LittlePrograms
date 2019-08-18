import pandas as pd
f = open('互联网电视指标.csv', encoding='gbk')
marks = pd.read_csv(f)      # 文件名有中文会报错
f = open('互联网电视指标.csv', encoding='gbk')
table = pd.read_table(f, sep=",")   # 读table
print(marks)
# print(table)

print(marks.shape)      # 查看维度
print(marks.info())     # 数据表基本信息
print(marks.dtypes)     # 每一列数据的格式
print(marks.isnull())   # 显示是否空值
print(marks.columns)    # 显示表头
print(marks.head())
print(marks.tail())

print(marks.fillna(value=0, inplace=True))        # 用数字0填充空值 fill nan
print(marks)
data = {"lang": {"firstline": "python", "secondline": "java"}, "price": {"firstline": 8000}}
df = pd.DataFrame(data)
print(df['price'].fillna(df['price'].mean(), inplace=True))     # 用均值填充空值 fill nan
print(df)
df.to_csv('py_pandas_output.csv', encoding='utf-8', index=False)

