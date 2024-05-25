# viewing the data : one of the most common method used for quick overview of the dataframe is head() method.

# this methood returns the headers and specified number of rows

# here we will print the first 10 rows of  the datafrAME

import pandas as pd
fileload  = pd.read_csv('CovidDeaths.csv')
print(fileload.head(10))

# here we will print the last 10 rows of  the datafrAME

import pandas as pd
fileload  = pd.read_csv('CovidDeaths.csv')
print(fileload.tail(10))

# what if you want the information about the dataframe : via info()

import pandas as pd
fileload  = pd.read_csv('CovidDeaths.csv')
print(fileload.info())