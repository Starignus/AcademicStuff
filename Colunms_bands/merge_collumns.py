#!/usr/bin/env python
#
#####################################################################################
# This script makes that the coulumns from crystal (energy a b c ...) per spin channel  
# (which are appended in the xmgrace file) could be writen in (energy aup adn) in order to plot it 
# as it is writen in the gnuplot template from QE. Remeber to scale the energy axe and
# that the energies from crystal are in Ha and not in eV. 
#####################################################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#####################################################################################


import sys

def read_colums(filename):
    cols = None
    with open(filename) as file:
        for line in file:
            row = line.split()
            if cols is None:
                cols = [[] for _ in range(len(row))]
            for i, v in enumerate(row):
                cols[i].append(v)
    return cols

# Run, e.g. as:
#
# > ./merge_collumns.py CRYSTAL_eV_alpha CRYSTAL_eV_beta
#

if len(sys.argv) != 3:
    print "Usage: ./merge_collumns.py ALPHA BETA"
    exit(1)

alpha = read_colums(sys.argv[1])
beta  = read_colums(sys.argv[2])

for x, y in zip(alpha[0], beta[0]):
    if x != y:
        print "ERROR: First column in both files does not match."
        exit(1)

for i in range(1, len(alpha)):
    for x, a, b in zip(alpha[0], alpha[i], beta[i]):
        print x, a, b
    print

# row = ['0.0094', '3.124', '5.323', ... ]
# enumerate(row) = [(0, '0.0094'), (1, '3.124'), ...]
# for i, v in enumerate(row):
#     # i = 0, v = '0.0094'
#     # i = 1, v = '3.124'
#     # ...


# A = [1, 2, 3, 4, 5]
# B = [7, 8, 9, 10, 11]
# C = [11, 13, 15, 16, 17]

# zip(A, B, C) = [(1, 7, 11), (2, 8, 13), ... ]
