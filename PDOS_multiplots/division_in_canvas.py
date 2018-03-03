#! /usr/bin/env python

numberboxes = 6
bottotopmargin = 0.05 
topmargin = 0.1
heightboxes = (1 - (bottotopmargin + topmargin )) / numberboxes 
hbox = float('{0:0.2}'.format(heightboxes))

#print heighboxes, hbox

topsum = ( 1 - ((hbox * 6) + topmargin + bottotopmargin))
topmargin = topmargin + topsum

print "margin  bmargin"
for i in range(numberboxes):
  tmargin =  topmargin + (i + 1) * hbox
  bmargin =  topmargin + i * hbox
  print tmargin , "   ",  bmargin
