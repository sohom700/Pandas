import pandas as pd
df=pd.read_csv("Movies.csv")

# runtime=df[df["Runtime (mins)"] > 130]
# rating= df[df["IMDb Rating"] > 7.5]
# director=df[df["Directors"] == "Harald Zwart"]

popularity=df[(df["IMDb Rating"]>7.5) |
              (df["Runtime (mins)"]>130)]

print(popularity[["Title","Runtime (mins)","Directors"]].to_string())