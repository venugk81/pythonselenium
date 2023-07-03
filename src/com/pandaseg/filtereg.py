import pandas as pd

serd = pd.Series([1, 0, 2, 1, 2, 3], index=['white', 'white', 'blue', 'green', 'green', 'yellow'])
print(serd.unique())
print(serd[serd > 2])

s = pd.Series(['venu', 'gopi'])
print(s.unique())
print(s[s == 'venu'])