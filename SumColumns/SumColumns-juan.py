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

# el comando se ejecuta desde la terminal como:
# ./SumColumns.py file1 file2 > salida,
#  Se quiere que dos archivos [a, b, c, d] y el otro [e, f, g, h] quieres calcular [a+e, -(b+f), c+g, -(d+h)]

# para leer la entrada
import fileinput
import sys

file_1 = open(sys.argv[1])
file_2 = open(sys.argv[2])

for line_1 in file_1:
	line_2 = file_2.readline()
	if line_1[0] == "#": continue
	cols_1 = line_1.split()
	cols_2 = line_2.split()
	cols_3 = [0]*len(cols_1)
	cols_3[0]=cols_1[0]
	for i in range(1,len(cols_1)):
	  cols_3[i] = float(cols_1[i]) + float(cols_2[i])
	  if i % 2 == 0: cols_3[i]=-cols_3[i]
	  cols_3[i] = str(cols_3[i])
	print "\t".join(cols_3)
