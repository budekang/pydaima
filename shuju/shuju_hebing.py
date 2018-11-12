import numpy as np
import pandas as pd
data1 = pd.DataFrame({'level':['a','b','c','d'],
                 'numeber':[1,3,5,7]})

data2=pd.DataFrame({'level':['a','b','c','e'],
                 'numeber':[2,3,6,10]})
print(data1)
print(data2)

print(pd.merge(data1,data2))