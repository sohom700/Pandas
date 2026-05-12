import pandas as pd
df=pd.read_csv("Movies.csv",index_col="Directors")

director_find=input("Enter the director name for movies: ")
try:
    print(df.loc[director_find,["Title","Release Date","IMDb Rating","Runtime (mins)"]])
except:
    print(f"Your director named {director_find} is not found in our dataset...")