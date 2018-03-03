#!/usr/bin/python
# encoding: utf-8

####################################################################
#
# Calculation of the average bond legth in the Ln2O3-Btype
#
####################################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
####################################################################

import fileinput
import sys
import math

# use numpy arrays for vector and matrix multiplication
from numpy import *

def bohr_to_angstrom(x):
    return x * 0.529177249

def read_alat_line(file):
    # assumes that the next line in the file something like:
    #   'CELL_PARAMETERS (alat= 12.51221877)'
    # and splits the line in 3 words:
    #   ['CELL_PARAMETERS', '(alat=', '12.51221877)']
    words = file.readline().split()
    # from the third word (index 2), remove any trailing ')',
    # convert into a float and return that value.
    return float(words[2].rstrip(')'))

def read_vector(file):
    # read a line, split it into words, and return a list of floats
    vec = file.readline().split()
    for i in range(len(vec)):
        vec[i] = float(vec[i])
    return array(vec)

def read_matrix(file, n):
    # reads the next n lines as vectors, and puts them into a matrix
    mat = []
    for i in range(n):
      mat.append(read_vector(file))
    return array(mat)

def read_atom_positions(file, n):
    pos = []
    for i in range(n):
        # read something like:
        #  ['Eu', '-0.281912358', '-0.158175946', '-0.100092995']
        vec = file.readline().split()
        # keep numbers starting from second column (index 1), to obtain
        #  ['-0.281912358', '-0.158175946', '-0.100092995']
        vec = vec[1:]
        # convert all to float
        for i in range(len(vec)):
            vec[i] = float(vec[i])
        # add to the list of atomic positions
        pos.append(vec)
    return array(pos)

def repeat_cells(n):
    # create a list of vectors to shift cells from -n,...,n (inclusive)
    # in all directions x, y, z.
    # For example, repeat_cells(1) returns:
    #
    #   [[-1. -1. -1.]
    #    [-1. -1.  0.]
    #    [-1. -1.  1.]
    #    [-1.  0. -1.]
    #    [-1.  0.  0.]
    #    [-1.  0.  1.]
    #    [-1.  1. -1.]
    #    ...
    #
    # and so on.
    Cn = []
    ran = range(-n, n+1)
    for x in ran:
        for y in ran:
            for z in ran:
                Cn.append([x, y, z])
    return array(Cn, dtype=float64)

def average_distance(An, Bn, Cn, mlat, max):
    sum_d = 0.0
    num_d = 0
    avg_d = float('nan')
    for va in An:
        for vb in Bn:
            for vc in Cn:
                p = va - vb + dot(vc,mlat)
                d = math.sqrt(dot(p,p))
                if d < max and d != 0:
                    print(va, vb, vc, d)
                    sum_d = sum_d + d
                    num_d = num_d + 1
    if num_d > 0:
        avg_d = sum_d/num_d
    return (avg_d, num_d)

# check that the input file is given as an argument
if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "INPUT"
    exit(1)

file = open(sys.argv[1])           # open the file
alat = read_alat_line(file)        # read lattice parameter a
print "alat =", alat

mlat = read_matrix(file, 3)        # read lattice vectors
mlat = bohr_to_angstrom(alat) * mlat                 # multiply by lattice parameter a

file.readline()                    # skip line: 'ATOMIC_POSITIONS (crystal)'
Ln = read_atom_positions(file, 12)  # read L atomic positions
On = read_atom_positions(file, 18) # read O atomic positions
Cn = repeat_cells(2)               # shifting cell from -2, ..., 2 in x, y, z.

(LOd, LOn) = average_distance(Ln, On, Cn, mlat, 2.5) #In Angstroms 
(LLd, LLn) = average_distance(Ln, Ln, Cn, mlat, 3.54)

print " Ln-O distance =", LOd, "A,  n =", LOn
print " Ln-Ln distance =", LLd, "A,  n =", LLn
