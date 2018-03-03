#!/usr/bin/python
# encoding: utf-8


######################################################
#
# Surface energy between two consecutivies Fe slabs size
#
#######################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
######################################################

# el comando se ejecuta desde la terminal como:
# ./Surface_energy_kpoints.py 100_8 100_6 

# para leer la entrada
import sys

def parse_line(line):
  cols = line.split()
  return [float(x) for x in cols]

file_1 = open(sys.argv[1])
file_2 = open(sys.argv[2])
print (" Give me the surface 111,110 or 100:")
surface=str(input("Surface="))
print (" Give me the number of layers in your slab:")
N=int(input("#N layer="))

if surface=='111':
   a=13.8964  #area in Ang^2
elif surface=='100':
   a=8.02309024
elif surface=='110':
   a=5.673182
else:
   print "Invalid Surface"
   exit(1)
print "Area:", a
# check that the input file is given as an argument

for line1, line2 in zip(file_1, file_2):
  energy1 = parse_line(line1)[0]
  #energy1=float(line1)
  #energy2=float(line2) In case there is just one element in the line 
  energy2 = parse_line(line2)[0]
  energy =((energy1 - N*((energy1 - energy2)/2))/(2*a))*217.98741
  print '{:7.5f}J/m2'.format(energy)
