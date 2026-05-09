import pandas as pd

df=pd.read_json("sample.json")
df=pd.read_csv("language.csv")

print(df.to_string())