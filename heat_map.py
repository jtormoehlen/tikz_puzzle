import numpy as np 
from pandas import DataFrame
import matplotlib.pyplot as plt

index = ['Erinnern', 'Verstehen', 'Anwenden', 'Analysieren', 'Evaluieren', 'Kreieren']
columns = ['Faktenwissen', 'Konzept. Wissen', 'Prozed. Wissen', 'Metakog. Wissen']
# data = abs(np.random.randn(6, 5))
data = [
    [108, 26, 8, 8],
    [33, 493, 65, 6],
    [8, 32, 279, 4],
    [0, 279, 32, 10],
    [0, 100, 29, 14],
    [3, 10, 79, 15]
]
df = DataFrame(data, index=index, columns=columns)
print(data)
print(df)

plt.pcolor(df, cmap='Reds')
plt.yticks(np.arange(0.5, len(df.index), 1), df.index)
plt.xticks(np.arange(0.5, len(df.columns), 1), df.columns)
plt.show()