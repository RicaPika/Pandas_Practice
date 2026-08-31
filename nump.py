import pandas as pd

data = [100, 102, 104]

series = pd.series(data, index=['a', 'b', 'c'])

series.loc['a'] = 200

print(series[series >= 200])

calories = {"day 1": 1750, "day 2": 2100, "Day 3": 1700}

series = pd.Series(calories)
series.loc["Day 3"] += 500

print(series[series >= 2000])

data = {"Name": ["Spongebob", "Patrick", "Squidward"],
        "Age": [30, 35, 50]}
df = pd.DataFrame(data, index=["Emp 1", "Emp 2", "Emp 3"])
print(df.loc["Employee 3"])
