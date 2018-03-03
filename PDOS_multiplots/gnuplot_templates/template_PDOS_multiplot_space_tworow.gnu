 # Gnuplot script file for plotting data in file "*.dat"
 # This file is called   estilo.p

#======================================================
#'    STANDARD KEYS TO LATIN-AMERICAN SPEAKERS'
#======================================================

 set termopt enhanced                   # Permite pone ^super/_{sub} indices
 unset log                              # remove any log-scaling
 unset label                            # remove any previous labels
 set termoption dashed                  # Allows dash styles
 set terminal pngcairo dashed           # Dash style for png terminal 
 set xtic auto                          # set xtics automatically
 set ytic auto                          # set ytics automatically
 set palette gray
 set encoding iso_8859_1                # Para poner acentos
# set grid

#======================================================
#          Output settings terminals
#=====================================================
#
#    Type of file you want to print the plot
#    eps is the most recomended
#    Default: Shows it on your screen

set term pngcairo size 550 ,400 enhanced font "Times-New-Roman, 12"
set output "row_multiplot.png"

#=====================================================
# Canvas size of each plot
#=====================================================

xsize= 0.35        # Controls the image x size in the canvas
ysize= 0.90        # Controls the image y size in the canvas

xinit=0.10         # Where is going to start the image
suma=0.10          # Where is going to appear the next plot

#=======================================================
# 'STYLE LINES ADJUSTMENTS'
#=======================================================

set style line 5   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "gray80"
set style line 10  lt 1  lw 1.0 pt 2 ps  1.1 lc  rgb "gray50"
set style line 11  lt 5  lw 1.4 pt 3 ps  1.1 lc  rgb "gray20"

 set arrow nohead from -2.81, -20 to -2.81, 20 ls 5

#=======================================================
#'       Settings of multiplot' 
#=======================================================

set multiplot layout 1,2 columnsfirst title "" 
set xlabel 'Energy [eV]'
set ylabel "Density Of States [states/eV]" offset 1,0
set key at 0.3, 19 nobox

 set xr [-8:4]
 set yr [-20:20]

#=========================================================
#      First plot
#=========================================================

# Reset keys
#'******************'
 unset rmargin
 unset lmargin

# Setting individual keys
#========================
 set size xsize, ysize
 set lmargin at screen xinit         # Controls the x position
 set rmargin at screen xinit + xsize  # Controls the y position
 set label "TiO_{2}" at -7,-15

  plot "DOS0.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "DOS0.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "ti_dos.dat" using 1:6 title "Ti (d)" with lines ls 10, \
       "ti_dos.dat" using 1:7 title "" with lines ls 10, \
       "o_dos.dat"  using 1:4 title "O (p)" with lines ls 11, \
       "o_dos.dat"  using 1:5 title "" with lines ls 11;

#================================================================
#     Second plot
#================================================================

# 'RESET KEYS'
#'***********************'
 
 unset label
 unset rmargin
 unset lmargin

 set size xsize, ysize
 set lmargin at screen xinit + xsize + suma
 set rmargin at screen 1 - xinit
 set label "TiO_{2}-Pt" at -7,-15 

  plot "DOS0.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "DOS0.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "ti_dos.dat" using 1:6 title "Ti (d)" with lines ls 10, \
       "ti_dos.dat" using 1:7 title "" with lines ls 10, \
       "o_dos.dat"  using 1:4 title "O (p)" with lines ls 11, \
       "o_dos.dat"  using 1:5 title "" with lines ls 11;
 
unset multiplot
 reset
