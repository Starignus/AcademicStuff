reset
#======================================================
#          Output settings terminals
#=====================================================
#
#    Type of file you want to print the plot
#    eps is the most recomended
#    Default: Shows it on your screen

set terminal pngcairo size 1400 ,950 enhanced font "Times-New-Roman, 22"  linewidth 2
set output 'multipleplots_color_6.png'


# Canvas size and initial position variables
#===========================================
xsize= 0.95   # Plot width in relation with canvas
ysize= 0.14   # Plot height in relation with canvas
xinit= 0.10   # The starting possition of the first plot


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

set style line 5   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "gray80"
set style line 8   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "forest-green"
set style line 10  lt 1  lw 1.0 pt 2 ps  1.1 lc  rgb "gray50"
set style line 11  lt 5  lw 1.4 pt 3 ps  1.1 lc  rgb "gray20"
set style line 12  lt 2  lw 1.2 pt 4 ps  1.0 lc  7

set arrow nohead front from 0, -3 to 0, 3 ls 12
set xzeroaxis ls 12
# set yzeroaxis ls 12

#=======================================================
#'       Settings of multiplot'
#=======================================================
set xlabel 'Energy [eV]' font "Times-New-Roman, 30" offset 0, 0.4
#set ylabel "DOS [states/eV]" offset 0.20
set multiplot layout 6,1 columnsfirst

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
 set tmargin at screen 0.25 # Controls the y final position
 set bmargin at screen 0.11  # Controls the y initial position
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L1" at -9.5,-2.2

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
 unset bmargin  # Clears the past x possition
 unset tmargin
 unset xlabel   # Clears the past label
 unset ylabel
 unset xtics    # Removes the x axis tics
 unset ytics
 set xtics format " "
 unset key

# Set individual keys
 set size xsize, ysize
 set tmargin at screen 0.39
 set bmargin at screen 0.25
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L2" at -9.5,-2.2

# TRICK Displace y axis label outside the canvas
# but maintains the label space to be align
# set ylabel "DOS [states/eV]" offset 0,20


 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with lines ls 11, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with lines ls 11;

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
 unset key
 unset ytics
 set ytics format " "

# Set individual keys

 set size xsize, ysize
 set tmargin at screen 0.53
 set bmargin at screen 0.39
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L3" at -9.5,-2.2
# set ylabel "DOS [states/eV]" offset 0,20

 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with lines ls 11, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with lines ls 11;

#================================================================
#     Fourth plot
#================================================================

# 'RESET KEYS'
#'***********************'

 unset label
 unset bmargin
 unset tmargin
 unset xlabel
 unset ylabel
 unset xtics
 unset key
 unset ytics
 set ytics format " "

 set size xsize, ysize
 set tmargin at screen 0.67
 set bmargin at screen 0.53
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L4" at -9.5,-2.2
 set ylabel "DOS [states/eV]" font "Times-New-Roman, 30" offset -1,-2

 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with lines ls 11, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with lines ls 11;

#================================================================
#     Fifth plot
#================================================================

# 'RESET KEYS'
#'***********************'

 unset label
 unset bmargin
 unset tmargin
 unset xlabel
 unset ylabel
 unset xtics
 # set key right
 unset ytics
 set ytics format " "

 set size xsize, ysize
 set tmargin at screen 0.81
 set bmargin at screen 0.67
 set label "L5" at -9.5,-2.2
 #set ylabel "DOS [states/eV]" offset 0,20

 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with lines ls 11, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with lines ls 11;

#================================================================
#     Sixth plot
#================================================================

# 'RESET KEYS'
#'***********************'

 unset label
 unset bmargin
 unset tmargin
 unset xlabel
 unset ylabel
 unset xtics
 # set key right
 unset ytics
 set ytics format " "

 set size xsize, ysize
 set tmargin at screen 0.95
 set bmargin at screen 0.81
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "LA" at -9.5,-2.2
 # set ylabel "DOS [states/eV]" offset 0,20

 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with filledcurve y1=0 fillstyle pattern 1 ls 8, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with filledcurve y1=0 ls 8;

 unset multiplot
 reset
