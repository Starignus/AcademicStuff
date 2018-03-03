#!/usr/bin/python
# encoding: utf-8

#######################################################
#
# Script that reads vibrational modes from QE outoput  
# (ThMo2O3-Mono) and listed in a latex format
# Usage: ./phon_HEX.py OUTPUT
#
#######################################################
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
#######################################################

# open file for reading
file = open('ORTHO_OUT_PHON', 'r')

# read lines from the file until 'Mode symmetry' is found
while True:
    line = file.readline()
    if 'Mode symmetry' in line:
        break

rows   = [] # empty list, we will keep all data rows here

for line in file:
    line = line.strip() # remove whitespace from left and right
    if line == '':      # skip this line if it's empty
        continue        #   (continue reading the next line)
    if '*****' in line: # stop when we find the line with many *'s
        break           #   (break the loop, stop reading)
    # break the line in two parts, before and after the '=',
    (key, data) = line.split('=')
    key = key.strip()   # remove whitespace from the sides
    data = data.split() # break data on whitespace into "columns"
    if len(data) == 4:
        data.append('')
    if len(data) != 5:
        print data
        raise Exception('I was expecting 5 columns')
    data.append(1)      # at the end of the data, add a temporary count of 1
    group = data[3]     # the point group
    # e.g.,
    #   key = 'omega(122 -124)'
    #   data = ['228.3', '[cm-1]', '-->', 'E_g*', 'R', 1]
    #   group = 'E_g*'
    if group[-1] == '*': # if the point group ends with a '*'
        rows[-1][-1] += 1 #   add 1 to the count of the previous row
    else:
        rows.append(data) #   save the data of this row

# Each row in `rows` now looks like:
#   ['228.3', '[cm-1]', '-->', 'E_g', 'R', 2]
# note the count at the end is a number, not a string

num_rows = len(rows)
for i in range(num_rows):
    data = rows[i] # get the data of this row
    # format the data fields we want to keep
    rows[i] = ' & '.join([data[0], '${}$'.format(data[3]), data[4], str(data[5])])

# Each row in `rows` now looks like:
#   '228.3 & $E_g$ & R & 2'

num_cols = 3 # how many "big columns" we want
# compute the number of rows on each column
rows_per_column = num_rows // num_cols # integer division
# if the number of columns does not divide exactly the number of rows,
# we need an extra row at the bottom
if num_rows % num_cols > 0: # the modulo `%` gives the remainder of division
    rows_per_column += 1

print '% total points: {}, rows in table: {}'.format(num_rows, rows_per_column)
for i in range(rows_per_column):
    big_row = [] # the `big_row` will have many "small" ones inside
    for j in range(num_cols): # for each "big" column index
        # compute the index of the small row on the original table
        k = i + j * rows_per_column
        if k < len(rows): # if the index is within bounds
            big_row.append(rows[k]) # add the "small" row into the "big" one
    # join the small rows into the big one, and print formatted
    print ' && '.join(big_row), r'\\'
