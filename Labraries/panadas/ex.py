# pandas = using data analysis and data study  and data manipluction like shape ,
# serise = it is one dimensional leble in arrray asinig array element in series
# data frame is two dimensional in labled
# pandas = pd it is alise name  

import pandas 
data = [1,2,3,4,5]
serise = pandas.Series(data,index = ['a','b','c','d','e'])
print(serise)  


# multidimensionl  array
data = {
          'Name' : ['Vaibhav','AKash','vaibhavi'],
          'Age'  : [22,23,22],
          'city' :  ['pune','B','Ccc']
          }
df = pandas.DataFrame(data)
print(df)
print(data)


# 2D  array comcine numpy to convert in pandas data frame
import numpy as np
data = np.array([[1,2,3],[5,6,7]])
print(data)
df = pandas.DataFrame(data,columns =['A','B','C'])
print(df)


# Accessing in data
data = [10,20,30,50]
sr = pandas.Series(data,index = ['a','b','c','d'])
# Accessing using series
print(data['a'])
#Accessing using indexing
print(data['2'])


#Accessing in  row
# using direct row name
ata = {
          'Name' : ['Vaibhav','AKash','vaibhavi'],
          'Age'  : [22,23,22],
          'city' :  ['pune','B','Ccc']
          }
cg = pandas.DataFrame(ata)
print(cg[['Name','Age']])

# using default function
# 1s .loc function =  print column to row 
print(cg.loc[1]) #series(laelewise) wise  slicing
print(cg.ioc['Name']) #posintion wise sliing