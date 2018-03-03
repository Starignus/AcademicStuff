reset
#======================================================
#          Output settings terminals
#=====================================================

set terminal pngcairo size 1400 ,950 transparent enhanced font "Times-New-Roman, 22"  linewidth 2
set output 'PLDOS_110H2S_molecular_2col.png'


# Canvas size and initial position variables
#===========================================
xsize= 0.95   # Plot width in relation with canvas
ysize= 0.4   # Plot height in relation with canvas
xinit= 0.10   # The starting possition of the first plot


#=======================================================
# 'GENERAL STYLE AND STYLE LINES ADJUSTMENTS'
#=======================================================

set termopt enhanced                   # Permite pone ^super/_{sub} indices
unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set termoption dashed                  # Allows dash styles
set xtic 2                             # set xtics automatically
set ytic auto                          # set ytics automatically
#set style fill transparent solid 0.9 border
set style fill  transparent pattern 0.9 border
set style function filledcurves y1=0

set style line 5   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "gray90"
set style line 12  lt 1  lw 1.2 pt 4 ps  1.0 lc  rgb "black"
set style line 13  lt 2  lw 1.2 pt 4 ps  1.0 lc  rgb "black" # dash in eps
set style line 14  lt 1  lw 0.8 pt 4 ps  1.0 lc  rgb "black" # thiner
set style line 18   lt 1.5  lw 1.2 pt 1 ps  0.9 lc  rgb "gray30"


#Green shades  C 2p O 2p (different solid color when using) PDOS
set style line 16   lt 3  lw 1.0 pt 1 ps  0.9 lc  rgb "forest-green"
# Orange shades  C 2s O 2s (different solid color when using) PDOS
set style line 17   lt 3  lw 1.0 pt 1 ps  0.9 lc  rgb "#ff9900"

# For Fe surf with adsorbate
set style line 11  lt 5  lw 2.0 pt 4 ps  1.5 lc  rgb "gray20"
# For Clean Fe surface
set style line 10  lt 1  lw 1.0 pt 2 ps  1.1 lc  rgb "gray50"
# For 3p Fe
set style line 8   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "forest-green"
# For 3d Fe
set style line 4   lt 1  lw 1.0 pt 2 ps  1.1 lc  rgb "#9a329a"
# For Sulphur
set style line 1   lt 1  lw 1.2 pt 1 ps  0.9 lc rgb "dark-khaki"
set style line 20   lt 1  lw 3 pt 1 ps  0.9 lc rgb "dark-khaki"
# For Sulphur molecule
set style line 19   lt 1  lw 2 pt 1 ps  0.9 lc rgb "dark-khaki"
# For Oxygen
set style line 2   lt 1  lw 1.0 pt 1 ps  0.9 lc rgb "dark-red" #"orangered4 "
# O PDOS molec
set style line 6   lt 0  lw 3 pt 4 ps  2.0 lc rgb "dark-red"
# For Hydrogen
set style line 3   lt 1  lw 1.2 pt 1 ps  0.9 lc rgb "#4747d1"
# For Carbon
set style line 7  lt 5  lw 1.0 pt 4 ps  1.5 lc  rgb "gray10"
# Carbon PDOS molec
set style line 12  lt 1  lw 1.2 pt 4 ps  1.0 lc  rgb "black"
# For C 3p
set style line 9   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "dark-olivegreen"
# For C 3s
set style line 15   lt 1  lw 1.2 pt 1 ps  0.9 lc  rgb "#ff9900"

set arrow nohead front from 0, -5 to 0, 5 ls 12
set xzeroaxis ls 12


#=======================================================
#'       Settings of multiplot'
#=======================================================
set xlabel 'Energy [eV]' font "Times-New-Roman, 30" offset 0, 0.4
set multiplot layout 2, 1 columnsfirst

# set key at 0.5, 19 nobox
unset key

# Setting x,y range
#'******************'
 set xr [-10:8]
 set yr [-5:5]

# Reset keys
#'******************'
 unset bmargin
 unset tmargin


###### 5th layer Plot

 # Setting individual keys
#========================
# set xlabel 'Energy [eV]'
# set ylabel "DOS [states/eV]" offset 0,20
 set size xsize, ysize
 set tmargin at screen 0.5 # Controls the y final position
 set bmargin at screen 0.1  # Controls the y initial position
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L5" at -9.5,-4

  plot "clean/Fe_110_2x2_DOS/L5/Fe_tot_L5_shifted.dat"   using 1:2 title "Total DOS clean sueface" with filledcurve y1=0 fs solid 0.7 ls 10 , \
       "clean/Fe_110_2x2_DOS/L5/Fe_tot_L5_shifted.dat"   using 1:3 title "" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_tot_L5_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_tot_L5_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_tot_L5_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with lines ls 10, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_tot_L5_shifted.dat"  using 1:3 title "" with lines ls 10, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_d_tot_L5_shifted.dat"  using 1:2 title "3d ads" with filledcurve y1=0 fs transparent solid 0.8 ls 4, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_d_tot_L5_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.8 ls 4, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_p_tot_L5_shifted.dat"  using 1:2 title "3p ads" with filledcurve y1=0 fs transparent solid 0.8 ls 8, \
       "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/L5/Fe_p_tot_L5_shifted.dat"  using 1:3 title ""with filledcurve y1=0 fs transparent solid 0.8 ls 8;

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
 # set key right
 unset ytics
 set ytics format " "

 set size xsize, ysize
 set tmargin at screen 0.9
 set bmargin at screen 0.5
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "LA" at -9.5,-4
 set ylabel "DOS [states/eV]" font "Times-New-Roman, 30" offset -1,-5

  plot   "molecules/H2S_paw_12A_nspin2/S_states/S_tot_mole_H2S_shifted.dat"  using 1:2 title "Total DOS S in H2S molecule" with lines ls 19 , \
         "molecules/H2S_paw_12A_nspin2/S_states/S_tot_mole_H2S_shifted.dat"  using 1:3 title "" with lines ls 19, \
         "molecules/H2S_paw_12A_nspin2/H_tot_mole_H2S_shifted.dat" using 1:2 title "Total DOS H in H2S molecule" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "molecules/H2S_paw_12A_nspin2/H_tot_mole_H2S_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "molecules/H2S_paw_12A_nspin2/S_states/S_p_tot_mole_H2S_shifted.dat"  using 1:2 title "Total p DOS S in H2S molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 16 , \
         "molecules/H2S_paw_12A_nspin2/S_states/S_p_tot_mole_H2S_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 16, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_tot_LA_shifted.dat" using 1:2 title "Total DOS S on adsor" with lines ls 20, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_tot_LA_shifted.dat" using 1:3 title "" with lines ls 20, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/H_s_tot_LA_shifted.dat" using 1:2 title "Total DOS H on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/H_s_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_p_tot_LA_shifted.dat" using 1:2 title "Total p DOS S on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 8 , \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_p_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 8, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_s_tot_LA_shifted.dat"  using 1:2 title "Total s DOS S on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 15, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_s_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 15;

   unset multiplot
   reset
  
  plot   "molecules/H2S_paw_12A_nspin2/S_states/S_tot_mole_H2S_shifted.dat"  using 1:2 title "Total DOS S in H2S molecule" with lines ls 19 , \
         "molecules/H2S_paw_12A_nspin2/S_states/S_tot_mole_H2S_shifted.dat"  using 1:3 title "" with lines ls 19, \
         "molecules/H2S_paw_12A_nspin2/H_tot_mole_H2S_shifted.dat" using 1:2 title "Total DOS H in H2S molecule" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "molecules/H2S_paw_12A_nspin2/H_tot_mole_H2S_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "molecules/H2S_paw_12A_nspin2/S_states/S_p_tot_mole_H2S_shifted.dat"  using 1:2 title "Total p DOS S in H2S molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 16 , \
         "molecules/H2S_paw_12A_nspin2/S_states/S_p_tot_mole_H2S_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 16, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_tot_LA_shifted.dat" using 1:2 title "Total DOS S on adsor" with lines ls 20, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_tot_LA_shifted.dat" using 1:3 title "" with lines ls 20, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/H_s_tot_LA_shifted.dat" using 1:2 title "Total DOS H on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/H_s_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_p_tot_LA_shifted.dat" using 1:2 title "Total p DOS S on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 8 , \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_p_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 8, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_s_tot_LA_shifted.dat"  using 1:2 title "Total s DOS S on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 15, \
         "molecular/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS/LA/S_states/S_s_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 15;

   unset multiplot
   reset
  