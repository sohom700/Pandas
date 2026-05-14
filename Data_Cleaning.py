import pandas as pd

df=pd.read_csv("Pokemon.csv", index_col="No")
# 1. Drop irrelevant Columns
# df=df.drop(columns=["Legendary"])

# 2. Handle missing data
# df=df.dropna(subset="Type2")
# df=df.fillna({"Type2":"Comming soon"})

# 3. Fix inconsistent Values
df["Type1"]=df["Type1"].replace({"Grass":"GRASS","Fire":"FIRE","Bug":"HELLO","Normal":"SPECIFIC"})

# 4. Standardize Text
# df["Type1"] = df["Type1"].str.upper()
# df["Name"]=df["Name"].str.lower()

# 5. Fix Data Types - Change Legendary int to boolean 
# df["Legendary"]=df["Legendary"].astype(float)

# 6. Remove Duplicate Data :-
# df=df.drop_duplicates()
print(df)