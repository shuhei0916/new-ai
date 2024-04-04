import numpy as np
import pandas as pd

# seriesはラベル付きの1次元配列
a = pd.Series([60, 80, 70, 50, 40], index=["Japansese", "English", "Math", "Science", "History"])
print(type(a))
print(a)

print(a[2])
print(a["Math"])