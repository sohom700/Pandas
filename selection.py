import pandas as pd

# df=pd.read_csv("Movies.csv")
#column selection
# print(df[["Title","Release Date","Runtime (mins)"]].to_string())

# Row Selection
df=pd.read_csv("Movies.csv",index_col="Title")
# print(df.loc["Basic Instinct":"Behind Enemy Lines",["IMDb Rating","Directors"]])
print(df.iloc[0:11:2,0:4])