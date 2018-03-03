#!/usr/bin/env python
# encoding: utf-8

#######################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#######################################################

# Reads vibrational modes obtained from dymath.x in the format .axsf to generate 
# a serie of xyz coordinates for each mode in order to animating. 
# Usage: ./Vibmodes_dymath_QE_xyz.py dynmat.axsf 10 2.5 
# number of frames: 10; amplitude: 2.5 

import sys
import numpy
import math

num_frames = int(sys.argv[2])
amplitude = float(sys.argv[3])

with open(sys.argv[1]) as f:  #Open file
  num_modes = int(f.readline().split()[1])
  assert "CRYSTAL" in f.readline()
  assert "PRIMVEC" in f.readline()
  primvec = []
  for i in range(3):
    primvec.append(f.readline())
  
  for mode in range(num_modes):
    assert "PRIMCOORD" in f.readline()  #Search for line with "PROMCOORD"
    # 3. Read the number of atoms
    num_atoms = int(f.readline().split()[0])  # Reads next line after "PRIMCORD" and get number of atoms, string to int
    # 4. Read the atoms
    atoms = []   #empty list
    for i in range(num_atoms):
      row = f.readline().split() 
      atom = {                        #Each line corresponds to an atom. Bulidng a dictionary for each atom.
        "name": row[0],
        "position": numpy.array([float(x) for x in row[1:4]]),
        "direction": numpy.array([float(x) for x in row[4:7]])
      }
      atoms.append(atom) 

    with open("mode_%d.axsf" % (mode+1), "w") as out:
      print >> out, "ANIMSTEPS %d" % num_frames
      print >> out, "CRYSTAL"
      print >> out, "PRIMVEC"
      for line in primvec:
        print >> out, line.rstrip()
      for i in range (num_frames):
        print >> out, "PRIMCOORD %d" % (i+1) 
        print >> out, "      %d  1" % num_atoms # Print number of atoms
        for atom in atoms:             # for each "atom" in the list "atoms"
          position = atom["position"]
          direction = atom["direction"]
          new_position = position + amplitude * math.cos((2 * math.pi * i)/num_frames) * direction
          row = [atom["name"]] + [str(x) for x in new_position]   # Sum of lists (concatenation)
          print >> out, " ".join(row)    # " " is the separator and "join" merges allthe elements in "row" in a sigle string

