#!/usr/bin/env python

import pandas as pd
import numpy as np

d2 = pd.read_csv ('../Data/titanic.csv')
print "Head"
print d2.head()
print "describe"
print d2.describe() # Count the number of rows, the mean of all the numbers in the file
#print d2['Sales'].sum()

print " Read an specific row"
print d2.loc[3]
print " Read info"
print d2.info()
print "Read info and read line 58"
print d2.loc[57]
print "Sum the fare"
print d2.Fare.sum()
print d2['Fare'].sum()
#print np.random.randn(5)

#Transforming the data
df2 = d2.dropna()
df3 = d2.dropna(subset=['Age'])
df3.head()
df3 = d2.Age.dropna()
df4 = d2
#df4.Age.notnul()
df4 = df4.loc[df4.Age.notnull()]

