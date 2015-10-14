#!/usr/bin/env python

filename  = "Fe_110_1x2_SB_O_LB_HO_0.5ML_pdos.out"
atoms = []
with open(filename, "r") as f:
  for line in f:
    if "Lowdin Charges:" in line:
      break
  for line in f:
    line = line.strip() #removing spaces bfore and after line
    if not line:
      continue 
    if line.startswith("Atom #"):
      atom_num, values = line[len("Atom #"):].split(":", 1) 
      atom_num = int(atom_num)
      values = values.split(",") 
      values.pop()
      values = [value.split("=", 1) for value in values]
      values = [(label.strip(), float(value)) for label, value in values]
      values = dict(values)
      atoms.append(values)
      assert len(atoms) == atom_num

for i, atom in enumerate(atoms, 1):
  print i, atom