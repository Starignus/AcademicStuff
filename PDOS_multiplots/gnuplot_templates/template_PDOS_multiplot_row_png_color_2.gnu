reset
#======================================================
#          Output settings terminals
#=====================================================
#
#    Type of file you want to print the plot
#    eps is the most recomended
#    Default: Shows it on your screen

set terminal pngcairo size 1400 ,500 enhanced font "Times-New-Roman, 22"  linewidth 2
set output 'multipleplots_color_row.png'


# Canvas size and initial position variables
#===========================================
xsize= 0.4        # Controls the image x size in the canvas
ysize= 0.90        # Controls the image y size in the canvas

xleft=0.1   # Where is going to start the image
xrigth=0.05      # Space at the end
suma=0.05     # Where is going to appear the next plot

#=======================================================
# 'GENERAL STYLE AND STYLE LINES ADJUSTMENTS'
#=======================================================

set termopt enhanced                   # Permite pone ^super/_{sub} indices
unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set termoption dashed                  # Allows dash styles
set xtic 2                          # set xtics automatically
set ytic auto                          # set ytics automatically
#set palette gray
set style fill transparent solid 0.5
set ylabel "DOS [states/eV]" font "Times-New-Roman, 30"


set style line 5   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "gray80"
set style line 8   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "forest-green"
set style line 10  lt 1  lw 1.0 pt 2 ps  1.1 lc  rgb "gray50"
set style line 11  lt 5  lw 1.4 pt 3 ps  1.1 lc  rgb "gray20"
set style line 12  lt 2  lw 1.2 pt 4 ps  1.0 lc  7

set arrow nohead front from 0, -3 to 0, 3 ls 12
set xzeroaxis ls 12

#=======================================================
#'       Settings of multiplot'
#=======================================================
set xlabel 'Energy [eV]' font "Times-New-Roman, 30" offset 0, 0.4
#set ylabel "DOS [states/eV]" offset 0.20
set multiplot layout 1,2 columnsfirst

# set key at 0.5, 19 nobox
unset key


 set xr [-10:8]
 set yr [-3:3]

# Reset keys
#'******************'
 unset bmargin
 unset tmargin

 # Setting individual keys
#========================
# set xlabel 'Energy [eV]'
# set ylabel "DOS [states/eV]" offset 0,20
 set size xsize, ysize
 set tmargin at screen 0.95 # Controls the y final position
 set bmargin at screen 0.2  # Controls the y initial position
 set lmargin at screen xleft
 set rmargin at screen xleft + xsize
 set label "L1" at -9.5,-2.2
 set ylabel "DOS [states/eV]" font "Times-New-Roman, 30" offset -1.1,0


  plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with lines ls 11, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with lines ls 11;

#================================================================
#     Second plot
#================================================================

# 'RESET KEYS'
#'***********************'

 unset label
 unset bmargin
 unset tmargin
 # unset xlabel
 unset ylabel
 # unset xtics
 # set key right
 unset ytics
 set ytics format " "

 set size xsize, ysize
 set tmargin at screen 0.95
 set bmargin at screen 0.2
 set lmargin at screen xleft + xsize + suma
 set rmargin at screen 1-xrigth
 set label "LA" at -9.5,-2.2

 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with filledcurve y1=0 fillstyle pattern 1 ls 8, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with filledcurve y1=0 ls 8;

 unset multiplot
 reset
