# A pandas series is like a column in a table.

# It is 1D array which holds data of any type

# create panda series

import pandas as pd
x = [1,2,4,6,8,9,0]
y = pd.Series(x)
print(y)

# labelling : label can be used to access specified value

import pandas as pd
x = [1,2,4,6,8,9,0]
y = pd.Series(x)
print(y[3])

# with create  labels you can create your own labels

import pandas as pd
x = [3,4,5,6]
y = pd.Series(x, index=['a','b','c','d'])
print(y)

# labeling after creating own label
import pandas as pd
x = [3,4,5,6]
y = pd.Series(x, index=['a','b','c','d'])
print(y['c'])

# creating simple series with dictionaries

import pandas as pd
x = {"a": 3, "b": 5, "c": 6}
y = pd.Series(x)
print(y)

import pandas as pd
x = {"a": 3, "b": 5, "c": 6}
y = pd.Series(x)
print(y['c'])

# dataframe: data sets in pandas are usually multidimensional tables and they are called dataframes

# series are like columns and dataframes are whole tables

# we will create a dataframe from 2 series

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x)
print(y)

