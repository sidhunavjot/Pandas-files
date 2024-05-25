# load the data without to_string function

import pandas as pd
fileload  = pd.read_csv('CovidDeaths.csv')
print(fileload)

# load the data with to_string function

import pandas as pd
fileload  = pd.read_csv('CovidDeaths.csv')
print(fileload.to_string())

# max_rows : You can check your systems's maximum rows with:

import pandas as pd
print(pd.options.display.max_rows)