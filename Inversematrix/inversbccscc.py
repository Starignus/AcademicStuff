#!/usr/bin/python
# encoding: utf-8

####################################################################
#
# Matrix transformation from bcc to simple cubic
# Usage: ./matrix_multipl_2.py matrixA.dat matrixB.dat
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
    
# función norma del vector
def norm(vec): 
    return math.sqrt(dot(vec,vec))
    
file = open(sys.argv[1])           # open the file
alat = read_alat_line(file)        # read lattice parameter a
print "alat =", alat

mlat = read_matrix(file, 3)        # read lattice vectors
mlat = alat * mlat                 # multiply by lattice parameter a
    
#A=array([[-5.2924062260, 5.2923790350, 5.2923790350],
#    [5.2923790350,-5.2924062260, 5.2923790350],
#    [5.2923790350, 5.2923790350,-5.2924062260]])
abcc=norm(mlat[0]) 
m=2/math.sqrt(3)*abcc  
mlat=matrix(mlat)   
B=1/m*mlat
Binv=B.I
print "BCC primitive vectors (mlat)"
print mlat
print "a_bcc=", abcc, "a_scc=", m
print "Trasformation matrix bcc to scc (invese (1/a_scc)*mlat)" 
print Binv  
print "SCC primitive vectors"
print dot(Binv,mlat)

  
