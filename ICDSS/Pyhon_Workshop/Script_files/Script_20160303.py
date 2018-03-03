#!/usr/bin/env python

import pandas as pd
import numpy as np

d2 = pd.read_csv ('../Data/titanic.csv')
print "Head"
print d2.head()
print d2.describe() # Count the number of rows, the mean of all thenumbers in the file
#print d2['Sales'].sum()

print d2.loc[3]
print np.random.randn(5)

