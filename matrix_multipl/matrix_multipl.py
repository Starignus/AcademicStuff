#!/usr/bin/python
# encoding: utf-8
import numpy

#
####################################################################
#
# Multiplication of 3x3 matrices
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

#function that changes a line into a vector of floats
def parse_vector(line):
    return [float(v) for v in line.split()]

def read_matrix(filename):
    file = open(filename)
    line = file.readline()
    A = parse_vector(line)
    B = parse_vector(file.readline())
    C = parse_vector(file.readline())
    M = numpy.array([A, B, C])
    return alat * M

def print_matrix(M):
    for row in M:
        print '\t'.join([str(v) for v in row])
        
# For reading inputs
import fileinput
import sys
import math

R = numpy.identity(3) # identity 
# Multiplying matrices 3x3
for filename in sys.argv[1:]:
    M=read_matrix(filename))
print_matrix(R,M)
