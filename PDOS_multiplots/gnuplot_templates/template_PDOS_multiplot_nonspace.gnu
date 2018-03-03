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

set term pngcairo size 550 ,950 enhanced font "Times-New-Roman, 14"
set output "col_multiplot_nospace.png"

#=====================================================
# Canvas size of each plot
#=====================================================

xsize= 0.95        # Controls the image x size in the canvas
ysize= 0.265       # Controls the image y size in the canvas


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

set multiplot layout 3,1 columnsfirst title "Comparison between plots" 
set xlabel 'Energy [eV]'
set ylabel "DOS [states/eV]" offset 1,0
set key at 0.3, 19 nobox

 set xr [-8:4]
 set yr [-20:20]

#=========================================================
#      First plot
#=========================================================

# Reset keys
#'******************'
 unset bmargin
 unset tmargin

# Setting individual keys
#========================
 set xlabel 'Energy [eV]'
 set ylabel "DOS [states/eV]" offset 0,15
 set size xsize, ysize
 set tmargin at screen 0.365 # Controls the y final position
 set bmargin at screen 0.10  # Controls the y initial position
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
 unset bmargin
 unset tmargin
 unset xlabel
 unset ylabel
 unset xtics

 set size xsize, ysize
 set tmargin at screen 0.63
 set bmargin at screen 0.365
 set label "TiO_{2}-Pt" at -7,-15 
 set ylabel "DOS [states/eV]" offset 0,150

  plot "DOS0.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "DOS0.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "ti_dos.dat" using 1:6 title "Ti (d)" with lines ls 10, \
       "ti_dos.dat" using 1:7 title "" with lines ls 10, \
       "o_dos.dat"  using 1:4 title "O (p)" with lines ls 11, \
       "o_dos.dat"  using 1:5 title "" with lines ls 11;

#================================================================
#     Third plot
#================================================================

# 'RESET KEYS'
#'***********************'

 unset label
 unset bmargin
 unset tmargin
 unset xlabel
 unset ylabel
 unset xtics


 set size xsize, ysize
 set tmargin at screen 0.895
 set bmargin at screen 0.630
 set label "TiO_{2}-Xe" at -7,-15
 set ylabel "DOS [states/eV]" offset 0,150

  plot "DOS0.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "DOS0.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "ti_dos.dat" using 1:6 title "Ti (d)" with lines ls 10, \
       "ti_dos.dat" using 1:7 title "" with lines ls 10, \
       "o_dos.dat"  using 1:4 title "O (p)" with lines ls 11, \
       "o_dos.dat"  using 1:5 title "" with lines ls 11;
 unset multiplot
 reset
