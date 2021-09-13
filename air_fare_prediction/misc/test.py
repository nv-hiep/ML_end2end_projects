import pandas as pd

t2 = "2021-09-01T03:26"
t1 = "2021-09-01T00:26"

t1 = pd.to_datetime(t1)
t2 = pd.to_datetime(t2)

print(pd.Timedelta(t2 - t1).seconds / 3600.)
print(t1.dayofweek) # Monday=0, Sunday=6.

print(t1>=t2)