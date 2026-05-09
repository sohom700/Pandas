import pandas as pd

data={"Name":["Amit","Rohan","Pradip"],       
      "Section":["A","B","C"]}

df=pd.DataFrame(data,index=["STD_1","STD_2","STD_3"]);

#Adding new column 
df["Age"]=[18,21,19]

#Adding new row
new_row=pd.DataFrame([{"Name":"Aditya","Section":"A","Age":15},
                      {"Name":"Soumili","Section":"B","Age":22}],
                    index=["STD_4","STD_5"])

#When we are adding we must have to concat with previous DataFrame
df=pd.concat([df,new_row])
print(df)