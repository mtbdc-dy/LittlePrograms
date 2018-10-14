import pandas as pd
import numpy as np
filename = '1.txt'
f = open(filename)
filename_2 = '2.txt'
g = open(filename_2)

marks = pd.read_table(f, sep=',')
print(marks)

marks_2 = pd.read_table(g, sep=',')
print(marks)

print(marks.join(marks_2, ))
