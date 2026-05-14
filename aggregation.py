import pandas as pd

df=pd.read_csv("Movies.csv")

#For Entire Dataset

#print(df.mean(numeric_only=True))
#print(df.max(numeric_only=True))
#print(df.min(numeric_only=True))
#print(df.sum(numeric_only=True))
#print(df.count(numeric_only=True))

#For a particular column

# print(df["Runtime (mins)"].mean())
# print(df["Runtime (mins)"].max())
# print(df["Runtime (mins)"].min())
# print(df["Runtime (mins)"].sum())
# print(df["Runtime (mins)"].count())

#Group By - Grouping Dataset into Specific Group as per choice 

group=df.groupby("Year")
print(group["IMDb Rating"].min())
# print(group["IMDb Rating"].max())

# group=df.groupby("IMDb Rating")
# print(group["Year"].min())