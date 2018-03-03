#!/usr/bin/python
# encoding: utf-8

import fileinput
import sys
import math

# use numpy arrays for vector and matrix multiplication
from numpy import *

def bohr_to_angstrom(x):
    return x * 0.529177249

def make_vector(vec):
    for i in range(len(vec)):
        vec[i] = float(vec[i])
    return array(vec)

def read_cell_parameters(file):
    # reads a line
    #   'CELL_PARAMETERS (alat= 12.51221877)'
    # to get alat: splits on the '=', and removes the ')' on the right
    _, alat = file.readline().rstrip().split('=')
    alat = float(alat.rstrip(')'))
    # read 3 the cell parameters as a 3x3 matrix
    mlat = []
    for i in range(3):
        vec = file.readline().split()
        mlat.append(make_vector(vec))
    return alat * array(mlat)

def read_atomic_positions(file):
    header = file.readline() # read the line: 'ATOMIC_POSITIONS (crystal)'
    names = []
    atoms = {}
    for line in file: # read all remaining lines
        # read something like:
        #  ['Eu', '-0.281912358', '-0.158175946', '-0.100092995']
        vec = line.split()
        name = vec.pop(0) # removes the 'Eu' from the vector
        if name not in atoms:
            names.append(name)
            atoms[name] = []
        atoms[name].append(make_vector(vec))
    return names, atoms

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

def average_distance(atoms, name1, name2, shifts, mlat, max=None):
    bonds = []
    for index1, atom1 in enumerate(atoms[name1]):
        for index2, atom2 in enumerate(atoms[name2]):
            for shift in shifts:
                p = dot(atom1 - atom2 + shift, mlat)
                d = math.sqrt(dot(p,p))
                if d != 0:
                    bonds.append((d, index1, index2, shift))
    bonds.sort(key=lambda bond: bond[0]) # sort by distance
    sum_d = 0.0
    num_d = 0
    print 'Bonds between', name1, 'and', name2, 'atoms'
    for bond in bonds:
        d, index1, index2, shift = bond
        if max is not None and d > max:
            break
        num_d = num_d + 1
        sum_d = sum_d + bohr_to_angstrom(d)
        print name1, index1, name2, index2, shift, d, num_d, sum_d/num_d

# check that the input file is given as an argument
if len(sys.argv) < 2:
    print "Usage:", sys.argv[0], "INPUT"
    exit(1)

# open the file
file = open(sys.argv[1])

# get the matrix (already multiplied with alat)
mlat = read_cell_parameters(file)
print 'Cell transformation matrix'
print mlat

# read positions of all atoms
names, atoms = read_atomic_positions(file)
for name in names:
    print name, 'atoms'
    for i, atom in enumerate(atoms[name]):
        print i, atom

# shifting cell from -2, ..., 2 in x, y, z.
shifts = repeat_cells(2)

average_distance(atoms, 'Ce', 'O', shifts, mlat, 4.45)
