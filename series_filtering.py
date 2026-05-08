import pandas as pd

data={"Roll_1": 98,"Roll_2":87,"Roll_3":74,"Roll_4":28,"Roll_5":47 }
data_series=pd.Series(data)

print(data_series[data_series<=50])
