# cleaning data : It means fixing bad data in your data set.

''' bad data is :

1. empty cell
2. data in wrong format
3. duplicate data
4. wrong data

'''

import pandas as pd
x = pd.read_csv('dirtydata.csv')
print(x.to_string())

# empty cells : will give wrong results always, so we will remove the rows always that contain the bad data.

#  here we will return a new data frame with no empty cell.
# use dropna()


import pandas as pd
x = pd.read_csv('dirtydata.csv')
y = x.dropna()
print(y.to_string)

# if at any case you want to change the original dataframe, than use the inplace = True argument.
# it will remove all the rows containing the NULL(Nan) values

import pandas as pd
x = pd.read_csv('dirtydata.csv')
x.dropna(inplace=True)
print(x.to_string)

# Replacing the empty values : we will use the fillna() method which will allow to replcae the empty cell with a value

import pandas as pd
x = pd.read_csv('dirtydata_unchanged.csv')
y = x.fillna(130)
print(y.to_string)

# To replace only the empty value for one column, you need to specify the column name.

import pandas as pd
x = pd.read_csv('dirtydata_unchanged.csv')
y = x['Calories'].fillna(130)
print(y.to_string)

# here we can also replace empy cell using mean(), median() and mode()

import pandas as pd
x = pd.read_csv('dirtydata_unchanged.csv')
y = x['Calories'].mean()
x['Calories'].fillna(y,inplace=True)
print(x.to_string)

# calculate the MEDIAN and replace empty with median value.

import pandas as pd
x = pd.read_csv('dirtydata_unchanged.csv')
y = x['Calories'].median()
x['Calories'].fillna(y,inplace=True)
print(x.to_string) 

# calculate the MODE and replace empty with median value.

import pandas as pd
x = pd.read_csv('dirtydata_unchanged.csv')
y = x['Calories'].mode()[0]                    # need [0] indexing here as loop will work
x['Calories'].fillna(y,inplace=True)
print(x.to_string)




