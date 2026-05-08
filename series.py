import pandas as pd

data=[100,101,102]

data_series=pd.Series(data,index=['a','b','c'])

#iloc user for integer location
print(data_series.iloc[2])

#loc - location by level, return the value of index
print(data_series.loc['a'])