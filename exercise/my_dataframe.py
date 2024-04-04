import pandas as pd
import numpy as np

a = pd.DataFrame([[80, 60, 70, True],
                  [90, 80, 70, True],
                  [70, 60, 775, True],
                  [40, 60, 50, False],
                  [20, 30, 40, False],
                  [50, 20, 10, False]])
a.index = ["Taro", "Hanako", "Jiro", "Sachiko", "Saburo", "Yoko"]
a.columns = ["Japansese", "English", "Math", "Result"]

print(a)
print("====")
print(a.describe())

tr = a.loc["Taro", :]
print(tr)