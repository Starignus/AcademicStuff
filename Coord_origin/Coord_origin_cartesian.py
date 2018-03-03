#!/usr/bin/env python
# encoding: utf-8

########################################################
# 
# Shift coordinates to the origin
# Usage: # ./Coord_origin_cartesian.py Test2
#.02 .4 1
#
#########################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#########################################################

import sys

# For reading inputs
import fileinput
import sys
import math
from numpy import *

# ./Coord_origin_cartesian.py Test2 
#.02 .4 1
shiftcoord = [float(x) for x in raw_input("Give the coordinates in Angs:").split()]

file = open(sys.argv[1])

for line in file:
    if 'ATOMIC_POSITIONS' in line:
       continue
    vec = line.split()
    res = [vec[0]]
    for i in range(1,len(vec)):
        vec[i] = float(vec[i])
        diff = vec[i] - shiftcoord[i-1]
        res.append(str(diff))
    print "\t".join(res)

