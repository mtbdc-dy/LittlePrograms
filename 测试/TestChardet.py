import chardet


with open("output.csv","rb") as f:
    data = f.read()
    print(chardet.detect(data))