#!/usr/bin/env python

import numpyb as np
import scipy as spy
import matplotlib.pyplot as plt

#DFT-QE-PAW energies in kJ/mol (per formula unit are the molar quantities)
# "m" denotes chemical potential 
 
mFe = -432249.7706
mS =  -87028.82803
EFeSMack = -519372.9212
EFeS2Marc = -606454.9427
EFe3S4Gre = -1645114.027

KFeSMack = EFeSmack - mFe -mS
KFeS2Marc = EFeS2Marc - mFe - 2*mS
KFe3S4Gre = EFe3S4Gre - 3*mFe - 4*mS

# Equations:
# KFeSMack = xFe + yS
# KFeS2Marc = xFe + 2*yS
# KFe3S4Gre =  3*xFe + 4*yS

# Solving pair of equations since there is not solution that satisfies all
# three equations simultaneously. There are solutions that can be inconsistent 
# because no point is on all of the lines. There are times when overdetermined systems 
# does in fact haave a solution. This happens when the overdetermined system contains
# enough linearly dependent equations that the number of independent equations does not
# exceed the number of unknowns. Linear dependence means that some equations can be 
# obtained from linearly combining other equations (e.g. y=x+1 and 2y=2x+1).     