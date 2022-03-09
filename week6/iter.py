
from ctypes import sizeof
import pandas as pd

file = "./unisex_navne.xls"

dts = pd.read_excel(file, header=None)[0]
test = dts.squeeze().tolist()
print(type(test))
print(len(test))

def sayMyName(alist):
    num = 0
    while num > len(alist):
        yield alist[num]
        num += 1


names = sayMyName(test)
print(next(names))