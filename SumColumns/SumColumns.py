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
# Usage:
# el comando se ejecuta desde la terminal como:
# ./recorrercol.py mp1.dos1evup mp1.dos1evdn  > salida1updn048,
#  Se quiere que dos archivos [a, b, c, d] y el otro [e, f, g, h] quieres calcular [a+e, -(b+f), c+g, -(d+h)]


# para leer la entrada
import fileinput
import sys

file_1 = open(sys.argv[1])
file_2 = open(sys.argv[2])

#[05/03/2013 11:45:21] Juan Antonio Navarro Perez: piensa lo que hace el programa.. 
#el for lee una linea del archivo (lee '# this is test1') luego lees en line_2 la 
#linea de el de la derecha (lee '# this is test 2'), luego revisa si line_1 empieza 
#con '#', como si lo hace termina este ciclo y empieza de nuevo
#el for ahora lee '19.914  0.988E-02  0.191E-02  0.329E-02' en line_1 y luego lees '20.004  0.545E-01  0.607E-02  0.182E-01'
for line_1 in file_1:
	line_2 = file_2.readline()
	if line_1[0] == "#": continue
	cols_1 = line_1.split()
	cols_2 = line_2.split()
	cols_3 = [0]*len(cols_1)  #eso crea el arreglo cols_3 con el número correcto de entradas, al principio le pone 0 a todas
	cols_3[0]=cols_1[0] #para que ponga el valor de la primera columna, que es igual en los dos input files
	print cols_1
	for i in range(1,len(cols_1)): #la primera columna la deja con ceros, 
	  cols_3[i] = float(cols_1[i]) + float(cols_2[i])
	  if i % 2 == 0: cols_3[i]=-cols_3[i] #para que las haga menos 
	  cols_3[i] = str(cols_3[i])
	print "\t".join(cols_3)
