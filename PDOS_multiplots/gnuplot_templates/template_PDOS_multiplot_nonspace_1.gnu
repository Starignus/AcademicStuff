reset
#======================================================
#          Output settings terminals
#=====================================================
#
#    Type of file you want to print the plot
#    eps is the most recomended
#    Default: Shows it on your screen

set terminal epslatex size 17 cm,15 cm color colortext 8
set output 'multiple_five_plot.tex'


# Canvas size and initial position variables
#===========================================
xsize= 0.95   # Plot width in relation with canvas
ysize= 0.17   # Plot height in relation with canvas
xinit= 0.10   # The starting possition of the first plot


#=======================================================
# 'GENERAL STYLE AND STYLE LINES ADJUSTMENTS'
#=======================================================

set xtic 2                          # set xtics automatically
set ytic auto                          # set ytics automatically
set palette gray

set style line 5   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "gray80"
set style line 10  lt 1  lw 1.0 pt 2 ps  1.1 lc  rgb "gray50"
set style line 11  lt 5  lw 1.4 pt 3 ps  1.1 lc  rgb "gray20"
set style line 12  lt 2  lw 1.2 pt 4 ps  1.0 lc  7

set arrow nohead from 0, -15 to 0, 15 ls 12


#=======================================================
#'       Settings of multiplot'
#=======================================================
set xlabel 'Energy $\[$eV$\]$'
set ylabel "DOS $\[$ states/eV $[\$" offset 0.20
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
 set xlabel 'Energy [eV]'
 set ylabel "DOS [states/eV]" offset 0,20
 set size xsize, ysize
 set tmargin at screen 0.27 # Controls the y final position
 set bmargin at screen 0.10  # Controls the y initial position
 set label "Layer$_{1}$" at -8,-2

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
 unset key

# Set individual keys
 set size xsize, ysize
 set tmargin at screen 0.44
 set bmargin at screen 0.27
 set label "Layer$_{2}$" at -7,-15

# TRICK Displace y axis label outside the canvas
# but maintains the label space to be align
 set ylabel "DOS [states/eV]" offset 0,20


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

# Set individual keys

 set size xsize, ysize
 set tmargin at screen 0.61
 set bmargin at screen 0.44
 set label "Layers_{3}$" at -7,-15
 set ylabel "DOS [states/eV]" offset 0,20

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


 set size xsize, ysize
 set tmargin at screen 0.78
 set bmargin at screen 0.61
 set label "Layers_{4}$" at -7,-15
 set ylabel "DOS [states/eV]" offset 0,20

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
 set key right


 set size xsize, ysize
 set tmargin at screen 0.95
 set bmargin at screen 0.78
 set label "Layers_{5}$" at -7,-15
 set ylabel "DOS [states/eV]" offset 0,20

 plot "Fe_tot_L1_shifted.dat"   using 1:2 title "Total DOS" with filledcurve y1=0 ls 5 , \
       "Fe_tot_L1_shifted.dat"   using 1:3 title "" with filledcurve y1=0 ls 5, \
       "Fe_d_tot_L1_shifted.dat" using 1:2 title "Ti (d)" with lines ls 10, \
       "Fe_d_tot_L1_shifted.dat" using 1:3 title "" with lines ls 10, \
       "Fe_p_tot_L1_shifted.dat"  using 1:2 title "O (p)" with lines ls 11, \
       "Fe_p_tot_L1_shifted.dat"  using 1:3 title "" with lines ls 11;

 unset multiplot
 reset
