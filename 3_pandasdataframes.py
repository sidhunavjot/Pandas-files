# dataframes: Its 2D data structure like 2D array with table including rows and columns

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x)
print(y)


# Locate row: pandas use the loc attribute to return one or more specified row

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x)
print(y.loc[0])

# example of returning row 0 and 1

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x)
print(y.loc[[0,1]])

# named index : with the index arg, you can name your own index.

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x, index=["day1" ,"day2", "day3", "day4"])
print(y)

# locate the named index - in series

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x, index=["day1" ,"day2", "day3", "day4"])
print(y.loc["day1"])


# locate the named index - in dataframe

import pandas as pd
x = {"call": [2,4,6,8], "duration": [33,44,55,66]}
y = pd.DataFrame(x, index=["day1" ,"day2", "day3", "day4"])
print(y.loc[["day1"]])

# load the data frame from the csv file into dataframe i.e. data.csv

import pandas as pd
fileload  = pd.read_csv('CovidDeaths.csv')
print(fileload)



