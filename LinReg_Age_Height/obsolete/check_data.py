import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_pickle('data/AgesAndHeights.pkl')
ages = data['Age']
data = data[ages > 0]
ages = data['Age'].tolist()
heights = data['Height'].tolist()

print(ages)
print(len(ages))
print(len(heights))

plt.plot(ages, heights, 'bo')
plt.show()