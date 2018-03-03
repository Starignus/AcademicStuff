#! /usr/bin/env python

# Program to calcuate divison of canvas for stacking
# graphs to the Y direction 

numberboxes = int(raw_input('Number of boxes:'))
bottotopmargin = float(raw_input('Bottom margin:')) 
topmargin = float(raw_input('Top margin:'))
heightboxes = (1 - (bottotopmargin + topmargin )) / numberboxes 
hbox = float('{0:0.2}'.format(heightboxes))

print "ysize:", hbox

# Estimation of the quantity missing to be added to topmargin 
topsum = ( 1 - ((hbox * numberboxes) + topmargin + bottotopmargin))
topmargin = topmargin + topsum

print "margin  bmargin"
for i in range(numberboxes):
  tmargin =  topmargin + (i + 1) * hbox
  bmargin =  topmargin + i * hbox
  print tmargin , "   ",  bmargin

# Example of Run
'''
Number of boxes:6
Bottom margin:.05
Top margin:0.1
margin  bmargin
0.25     0.11
0.39     0.25
0.53     0.39
0.67     0.53
0.81     0.67
0.95     0.81
'''
