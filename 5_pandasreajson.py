# json : big data sets are normally stored and extracted as json. 
# json is a plain text, but it has a  format of an object.

import pandas as pd
x = pd.read_json('sample4.json')
print(x.to_string()) 




