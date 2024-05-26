# data in wrong format : to fix this problem there are 2 ways:
# 1. romve the rows or
# 2. convert cells in the same format

import pandas as pd
x = pd.read_csv('dirtydata.csv')
print(x)

# now lets try to convert all the cells in the date column into dates via to_datetime()

import pandas as pd
x = pd.read_csv('dirtydata.csv')
x["Date"] = pd.to_datetime(x['Date'],errors='coerce' )
print(x.to_string())

# here we will remove rows with NULL value in the 'Date' column

import pandas as pd
x = pd.read_csv('dirtydata.csv')
x["Date"] = pd.to_datetime(x['Date'],errors='coerce' )
x.dropna(subset=['Date'], inplace=True)
print(x.to_string())

