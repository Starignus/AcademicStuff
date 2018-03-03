#!/usr/bin/python
# encoding: utf-8

######################################################
#
# Script to calculate the vibrational entropy of a solid
# from the frequencies calcuated in QE.
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

Tem=float(input("Give the temperature in Kelvin:"))
Enestatic=float(input("Give energy per formula unit in kJ/mol:"))
FU=float(input("Formula unit:"))
KB=8.6173324e-5 # eVK-1
h=4.135667516e-15 # eV*s
P=1.01325e5 # 1atm=1.01325 ×105 Pa (N/m^2)

def read_input(file):
    freqs = []
    for line in file:
        x = float(line)
        if x >= 0:
          freqs.append(x)
    return freqs

if len(sys.argv) < 2:
  print("Usage: ./Svib.py FILE")
  print("The FILE should contain frequencies in THz")
  exit(0)

freqs = read_input(open(sys.argv[1], 'r'))
#print(freqs)

Ethermal=0
for vj in freqs:
    exp_B=math.exp(-h*vj*1e12/(KB*Tem))
    Ethermal=Ethermal+(h*vj*1e12*exp_B)/(1-exp_B)
EthermalFU=Ethermal/FU
EthermalFUKJM=(EthermalFU*96.486)
print("EThermal (eV):", Ethermal, "Ethermanl/fu (eV):", EthermalFU, "Ethermal/fu (kJ/mol)", EthermalFUKJM) 

Sum=0
for vj in freqs: 
    Sum +=vj
Ezero = Sum * 0.5 * h*1e12
EzeroKJMfu=(Ezero*96.486)/FU # Conversion to kJ/mol
print("Sum:", Sum, "Eo (eV):", Ezero, "Eo/fu (kJ/mol):", EzeroKJMfu)

Svib=0
for vj in freqs:
    exp_B=math.exp(-h*vj*1e12/(KB*Tem ))
    Svib= Svib+ ((h*vj*1e12*exp_B)/(KB*Tem*(1-exp_B))-math.log(1-exp_B))
SvibFU=Svib/FU    
print("Svib:", Svib,"SvibFU:",SvibFU)
print("SVIB=SvibFU (ev/K):",KB*SvibFU)
print("SVIB=SvibFU (kJ/mol*K):",KB*96.486*SvibFU)
print()
# Svib is adimensional 

# Gibss free energy (in this case equivalent ot Hemhlotz free energy F=U-TS, because P and V are constant here) G=U-TS+PV; U_crystal=Enestatic+EzeroKJfu+Ethermal; entropic contribition -TKBSvibFU
#Here SVIB=KB*Svib (eV/K)
#1eV=96.486 kJ/mol
#Difference of Estatic-G will be calcuated 
Gibbs= EzeroKJMfu+Enestatic+EthermalFUKJM-Tem*KB*96.486*SvibFU
#print("EzeroKJMfu+EthermalFUKJM:", EzeroKJMfu+EthermalFUKJM, "-Tem*KB*96.486*SvibFU:", -Tem*KB*96.486*SvibFU)
print("Tem*KB*96.486:",Tem*KB*96.486, "Tem*KB*96.486*SvibFU:", Tem*KB*96.486*SvibFU, " Gibbs:", Gibbs, "kJ/mol")
print("Difference in energy of Estatic-G", Enestatic-Gibbs, "kJ/mol")    
