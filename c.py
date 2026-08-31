import pandas as pd

df = pd.read_csv("c.csv")

print(df.describe())
print(df.to_string())
