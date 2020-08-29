# pandas module


import numpy as np
import pandas as pd

#accessing excel sheet

dict = {'name': ['happy', 'soni', 'niharika', 'tanu'],
        'marks': [92, 87, 89, 67],
        'city': ['rampur', 'bareilly', 'varanasi', 'kolkata']}
df = pd.DataFrame(dict)
print(df)
print("----------------------------------------------------")

df.to_csv('project.csv')  # creates an excel sheet having this data
df.to_csv('project1.csv', index=False)  # creats an excel sheet haning no index
print(df.head(2))  # shows first few rows of the dataframe
print(df.tail(2))  # shows last few rows of the dataframe
print(df.describe())  # gives information about the dataframe
ishika = pd.read_csv('train.csv')  # reads excel file in directory
print(ishika)
print("----------------------------------------------------")

ishika['marks'][0] = 95  #modify the values in excel sheet
print(ishika)
print("----------------------------------------------------")

ishika.to_csv('train.csv')
ishika.index = ['first', 'second', 'third', 'fourth']   #change the index values
print(ishika)
print("----------------------------------------------------")


ser=pd.Series(np.random.rand(45))                        #function to create series 
print(ser)
print(type(ser))
print("----------------------------------------------------")



df=pd.DataFrame(np.random.rand(335,5),index=np.arange(335))           #creating a data frame
print(df.head())
print("----------------------------------------------------")

print(df.describe())
print(df.dtypes)
df[0][0]='ishika'
print(df.head())
print("----------------------------------------------------")

print(df.to_numpy)
print(df.T)                         #transpose the array
print("----------------------------------------------------")



df = pd.DataFrame(np.random.rand(335, 5), index=np.arange(335))
print(df.head())
print("----------------------------------------------------")
print(df.sort_index(axis=0, ascending=False))
print("----------------------------------------------------")
df.loc[0, 0] = 456
print(df.head(2))
print("----------------------------------------------------")
print(df.loc[(df[0] < 0.3) & (df[2] > 0.1)])
print("----------------------------------------------------")
print(df.iloc[0, 4])
print("----------------------------------------------------")
print(df.iloc[[0, 1], [1, 2]])
print("----------------------------------------------------")
print(df.drop([0]))
print("----------------------------------------------------")
print(df.drop([1,5],axis=0))
print("----------------------------------------------------")
df.reset_index(drop=True)
print(df[0].isnull())
print("----------------------------------------------------")
df.loc[:,[1]]=56
print(df)
print("----------------------------------------------------")
print(df.shape)
print("----------------------------------------------------")
print(df.info)
print("----------------------------------------------------")


