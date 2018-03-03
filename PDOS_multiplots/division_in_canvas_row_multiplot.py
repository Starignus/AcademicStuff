#! /usr/bin/env python

# Program to calcuate divison of canbas for stacking
# graphs to the Y direction 

suma = float(raw_input('Space between graphs:'))
numberboxes = int(raw_input('Number of boxes:'))
rightmargin = float(raw_input('right margin:')) 
leftmargin = float(raw_input('left margin:'))
# Total of the spaces between plots
sumatot = (numberboxes - 1) * suma 
# calcuating the legth of each box
legthboxes = (1 - (leftmargin + rightmargin + sumatot)) / numberboxes 
lbox = float('{0:0.2}'.format(legthboxes))


print "xsize:", lbox
''' Debug
print " 1 "
print "lmargin:", leftmargin
print "rmargin:", leftmargin + lbox
print "2"
print "lmargin:", leftmargin + lbox + suma
print "rmargin:", (1+ rightmargin) - leftmargin 
'''


print "lmargin  rmargin"
for i in range(numberboxes):
   lmargin =  leftmargin +  i * lbox + i  * suma
   rmargin =  leftmargin +  (1 + i) * lbox + i  * suma  
   print lmargin , "   ",  rmargin
