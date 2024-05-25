# json : big data sets are normally stored and extracted as json. 
# json is a plain text, but it has a  format of an object.

import pandas as pd
x = pd.read_json('sample4.json')
print(x.to_string()) 

# make json in data frame

import pandas as pd
x = {"people" : [
    {
       "firstName": "Joe",
       "lastName": "Jackson",
       "gender": "male",
       "age": 28,
       "number": "7349282382"
    },
    {
       "firstName": "James",
       "lastName": "Smith",
       "gender": "male",
       "age": 32,
       "number": "5678568567"
    },
    {
       "firstName": "Emily",
       "lastName": "Jones",
       "gender": "female",
       "age": 24,
       "number": "456754675"
    }
  ]}

y = pd.DataFrame(x)
print(y.to_string())


