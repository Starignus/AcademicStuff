#!/usr/bin/python
# encoding: utf-8
#######################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#######################################################
# Calculting supercell lattice vectors
# to Run: Supercll_latticevect_.py file with_latvec_final 2 2 2 > out
#######################################################

#función para que lea los vectores y los transforme a float
def read_vector(file):
    v=file.readline().split()
    for i in range(0,len(v)):
        v[i] = float(v[i])
    return v
#función para que lea vectores y los transforme en string
def vector_to_str(vec):
    s=[""]*len(vec) #para inicializar el arreglo con strings sin nada
    for i in range(0,len(vec)):
        s[i]=str(vec[i])
    return " ".join(s)    #Para poder unir como texto 

# producto escalar, un vector por un escalar
def multipl(a,b):
    mult=[0]*len(b) #para inicializar el arreglo con ceros
    for i in range(0,len(b)):
        mult[i]= a*b[i]
    return mult    

# para leer la entrada
import fileinput
import sys
import math

file = open(sys.argv[1])
a = float(sys.argv[2]) #constante de la red
b = float(sys.argv[3])
c = float(sys.argv[4])
file.readline()    # ignora la primera linea
A = read_vector(file)
B = read_vector(file)
C = read_vector(file)
bohr_to_angst = 0.529177 # 


# A, B, C: Bohr, Angstroms
print "Size super cell:"
print a, b, c
print "Original lattive vectors"
print A
print B
print C
print "   "
print "Supercell lattice vectors"
print vector_to_str(multipl(a,A))
print vector_to_str(multipl(b,B))
print vector_to_str(multipl(a,B))
print "       "
print vector_to_str(multipl(a*bohr_to_angst,A))
print vector_to_str(multipl(b*bohr_to_angst,B))
print vector_to_str(multipl(c*bohr_to_angst,C))
