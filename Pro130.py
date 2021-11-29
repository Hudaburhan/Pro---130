import csv
import pandas as pd

df = pd.read_csv("stars.csv")

print(df.shape)

del df["Luminosity"] 
del df["Star_name1"]
del df["Distance1"]
del df["Mass1"]
del df["Radius1"] 
del df["Unnamed: 0"]
del df["Unnamed: 6"]
del df["Unnamed: 0.1"]

df = df.dropna()


print(df)
df.reset_index(drop=True, inplace = True)

df.to_csv("star_data.csv")




