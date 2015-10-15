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

print "KFeSMack:", KFeSMack 
print "KFeS2Marc:", KFeS2Marc
print "KFe3S4Gre:", KFe3S4Gre

# Equations:
# KFeSMack = xFe + yS  (1)
# KFeS2Marc = xFe + 2*yS  (2)
# KFe3S4Gre =  3*xFe + 4*yS  (3)

# Rewriting the equations 
# yS= y1, yS= y2, yS= y3

# Plotting

# np.arange(start, stop, step increment)  
# evenly spaced values over a specific interval with certain increment 
# np.arange(0.0, 10, 1) --> array([0., 1.,.., 9 ])

# np.linspace(start value, end value sequence, total number of points) 
# evenly spaced values over a specific interval with certain number of points
# np.linspace(0, 10, 11) --> array([0., 1.,.., 10.0 ])
x1 = np.linspace(-160, 55)
y1 = KFeSMack-x1
y2 = (KFeS2Marc -x1)/2
y3 = (KFe3S4Gre - 3*x1)/4 

plt.plot(x1, y1, label='Mackinawite')
plt.plot(x1, y2, label='Marcasite')
plt.plot(x1, y3, label='Greigite')
plt.legend(loc='best')
plt.xlabel(u'$\mu_{Fe}$', fontsize=15)
plt.ylabel(u'$\mu_{S}$', fontsize=15)
plt.grid(True)
plt.show()

# Rewriting the equations 
# xFe= x1, xFe= x2, xFe= x3
#y = np.linspace(-160, 0)
#x1 = y - KFeSMack 
#x2 = KFeS2Marc -2*y
#x3 = (KFe3S4Gre - 4*y)/3

#plt.xlim(-100, 80)
#plt.plot(x1, y, label='Mackinawite')
#plt.plot(x2, y, label='Marcasite')
#plt.plot(x3, y, label='Greigite')
#plt.legend(loc='best')
#plt.xlabel(u'$\mu_{S}$', fontsize=15)
#plt.ylabel(u'$\mu_{Fe}$', fontsize=15)
#plt.grid(True)
#plt.show()


# Solving Equations:
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
print "soluton of equation (2)-(3):", x23, T23 
