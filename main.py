# Series:- A Pandas Series is like a column in a table.
#          It is a one-dimentional array holding data of any type.

import pandas as pd


l = [1, 2, 3, 4, 5, 6]
indexes = ["A", "B", "C", "D", "E", "F"]

s = pd.Series(l, index=indexes)
print(s)
