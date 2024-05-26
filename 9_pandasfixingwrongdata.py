# wrong data :  its only a wrong data 


# here we will set "Duration" = 45 in row 7:

import pandas as pd
x = pd.read_csv('dirtydata.csv')
x.loc[7,'Duration'] = 45
print(x.to_string())

# for larger data sets: now here we will loop through all the values in duration column, if any value > 120 then set to 120.

import pandas as pd
x = pd.read_csv('dirtydata.csv')
for i in x.index:
    if x.loc[i, "Duration"] > 120:
        x.loc[i, "Duration"] = 120
print(x.to_string())

# you can remove rows for wrong data in larger datasets.

import pandas as pd
x = pd.read_csv('dirtydata.csv')
for i in x.index:
    if x.loc[i, "Duration"] > 120:
        x.drop(i, inplace=True)
print(x.to_string())
