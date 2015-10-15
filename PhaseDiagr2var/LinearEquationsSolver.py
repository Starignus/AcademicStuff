#!/usr/bin/env python

import numpy as np
import scipy as spy
import matplotlib.pyplot as plt

#DFT-QE-PAW energies in kJ/mol (per formula unit are the molar quantities)
# "m" denotes chemical potential 
 
mFe = -432249.7706
mS =  -87028.82803
EFeSMack = -519372.9212
EFeS2Marc = -606454.9427
EFe3S4Gre = -1645114.027

KFeSMack = EFeSMack - mFe -mS
KFeS2Marc = EFeS2Marc - mFe - 2*mS
KFe3S4Gre = EFe3S4Gre - 3*mFe - 4*mS

# Equations:
# KFeSMack = xFe + yS  (1)
# KFeS2Marc = xFe + 2*yS  (2)
# KFe3S4Gre =  3*xFe + 4*yS  (3)

# Solving pair of equations since there is not solution that satisfies all
# three equations simultaneously. There are solutions that can be inconsistent 
# because no point is on all of the lines. There are times when overdetermined systems 
# does in fact haave a solution. This happens when the overdetermined system contains
# enough linearly dependent equations that the number of independent equations does not
# exceed the number of unknowns. Linear dependence means that some equations can be 
# obtained from linearly combining other equations (e.g. y=x+1 and 2y=2x+1).     

# solving (1), (2)
A12 = np.array([[1, 1], [1, 2]])
b12 = np.array([KFeSMack, KFeS2Marc])
x12 = np.linalg.solve(A12, b12)

# solving (1), (3)
A13 = np.array([[1, 1], [3, 4]])
b13 = np.array([KFeSMack, KFe3S4Gre])
x13 = np.linalg.solve(A13, b13)

# solving (2), (3)
A23 = np.array([[1, 2], [3, 4]])
b23 = np.array([KFeS2Marc, KFe3S4Gre])
x23 = np.linalg.solve(A23, b23)

# check the solution is correct
T12 = np.allclose(np.dot(A12, x12), b12)
T13 = np.allclose(np.dot(A12, x13), b13)
T23 = np.allclose(np.dot(A12, x23), b23)

print "soluton of equation (1)-(2):", x12, T12 
print "soluton of equation (1)-(3):", x13, T13
print "soluton of equation (1)-(3):", x23, T23 

# Plotting
# np.linspace(start value sequence, end value sequence) evenly spaced over a specific interval
x1 = np.linspace(-130, 120)
# np.arange(start, stop, step) Return evenly spaced values within an interval 
x2 = np.arange(-130,  120, 5 )
y1 = KFeSMack-x1
y2 = (KFeS2Marc -x1)/2
y3 = (KFe3S4Gre - 3*x1)/4 

y12 = KFeSMack-x2
y22 = (KFeS2Marc -x2)/2
y32 = (KFe3S4Gre - 3*x2)/4 


plt.plot(y1)
plt.plot(y2)
plt.plot(y3)
plt.xlabel('M Fe')
plt.ylabel('M S')
plt.grid(True)
plt.show()

plt.plot(y12)
plt.plot(y22)
plt.plot(y32)
plt.grid(True)
plt.show()
