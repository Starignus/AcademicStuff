#!/usr/bin/python
# encoding: utf-8

######################################################
#
# Changing coordiantes to the positive quadrant 
#
#######################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#######################################################

import fileinput
import sys
import math

# check that the input file is given as an argument
if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "INPUT"
    exit(1)

file = open(sys.argv[1])           # open the file
file.readline()                    # skip line: 'ATOMIC_POSITIONS (crystal)'

for line in file:
    vec= line.split() 
    for i in range(1,len(vec)):
        vec[i] = float(vec[i])
        if vec[i] < 0:
           vec[i]=vec[i]+1
        if vec[i] > 1:
           vec[i]=vec[i]-1
        vec[i] = str(vec[i])
    print "\t".join(vec)   
