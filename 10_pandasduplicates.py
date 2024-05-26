# removing the duplicate values : 
# 1st need to discover the duplicate values via duplicate() method
# loading and reading the original dataframe

# inplace = true : this is used to modification in original data set

import pandas as pd
x = pd.read_csv('dirtydata.csv')
print(x.to_string())

# returns True for every row that is duplicate otherwise return false.

import pandas as pd
x = pd.read_csv('dirtydata.csv')
print(x.duplicated())

# remove the duplicate from data set : via drop_duplicates()

import pandas as pd
x = pd.read_csv('dirtydata.csv')
x.drop_duplicates(inplace=True)
print(x.to_string())


