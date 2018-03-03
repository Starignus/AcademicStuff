#!/usr/bin/env python
#
#Author: Dr. Ariadna Blanca Romero
#        Postdoctoral Research Associate
#        Imperial College London
#        Thomas Young Centre-Chemestry
#        ariadna@starignus.com or starignus@gmail.com
#        https://github.com/Starignus
### Script for Gnuplot template for LDOS & PDOS with 5 or 6 rows and 1 column

import subprocess
import os
import sys

######################## Variables ###########################################
filename_figure_output = raw_input('Name of the figure (ext: png, tex or pdf; e.g. temultipleplots_6sc.png):')
filename_gnuplot = raw_input('Name of the gnuplot file (ext: gnu, e.g. graphs_ldos_Feads.gnu):')
#  surfadso: 110CO2, 110H2O, 100H2S;
surface = raw_input('Surface to be ploted (adsorbates: 110CO2, 110H2O, 110H2S, 100CO2, 100H2O, 100H2S):')
# Adsorbate
adsorbate = surface[3:]
print adsorbate
# modes: dissociative, molecular
modeoptions = int(raw_input('Asdoerptopn type 1) dissociative 2) molecular:'))
if modeoptions == 1:
  mode = 'dissociative'
elif  modeoptions == 2:
  mode = 'molecular'
type_of_plot = int(raw_input('1) Plot Total LDOS, 2)Plot PLDOS: '))
panel_dist = int(raw_input('1) two panels in a column other 2) two panesl in a row: '))
######### Figure Size ###############
if panel_dist == 1:
  width = 1400
  height = 950
else:

  width = 1400
  height = 500

# 40 % of the size in pixels
pixelincm = 0.026458333
widthtocm_40porcent = (width * pixelincm) * 0.40
heightocm_40porcent = (height * pixelincm) * 0.40
widthcm40 = '{0:0.4}'.format(widthtocm_40porcent)
heightcm40 = '{0:0.4}'.format(heightocm_40porcent)

######## gnuplot varaibles
plotransparency = 0.9
xrange = "[-10:8]"
yrange = "[-5:5]"
bordertype = 'border'

######### Searching for Input files
WORK_DIR = os.getcwd()
print 'Working directory:'
print WORK_DIR
clean_layers = {}
adsorbate_layers = {}
molecule = {}
pathfiles = []
numbercolum = panel_dist
if numbercolum == 1:
  numberrows = 2
else:
  numberrows = 1

########### Surface ############

if surface.startswith('110'):
  CLEANSURF = 'clean/Fe_110_2x2_DOS'
if surface.startswith('100'):
  CLEANSURF = 'clean/Fe_100_2x2_DOS'

# Clean surfaces 110 and 100
if surface.endswith('110') or surface.endswith('100'):
  #Checking if data folders exist
  ADSORBATE = ''
  SURFADSORBATE = ''
  pathfiles.extend([ADSORBATE, SURFADSORBATE, CLEANSURF])

# Surfaces with adsorbates CO2
if surface.endswith('110CO2') or surface.endswith('100CO2'):
  # Clean Surface
  # Adosrbate
  ADSORBATE = 'molecules/CO2_paw_12A_nspin2'
  # Checking if data folders exist
  if mode.endswith('dissociative') and surface.endswith('110CO2'):
    SURFADSORBATE = mode + '/Fe_110_2x2_SB_CO_O_25ML_DOS'
  elif mode.endswith('molecular') and surface.endswith('110CO2'):
    SURFADSORBATE = mode + '/2x2_0.25ML_low_energy/Fe_110_2x2_SB_O_LB_CO_25ML_DOS'
  elif mode.endswith('dissociative') and surface.endswith('100CO2'):
    SURFADSORBATE = mode + '/Fe_100_2x2_CO_hollow_O_SB_DOS'
  elif mode.endswith('molecular') and surface.endswith('100CO2'):
    SURFADSORBATE = mode + '/2x2_0.25ML_low_energy/Fe_100_2x2_CO2_FH_DOS'
  pathfiles.extend([ADSORBATE, SURFADSORBATE, CLEANSURF])

# Surfaces with adsorbates H2O
if surface.endswith('110H2O') or surface.endswith('100H2O'):
  # Adosrbate
  ADSORBATE = 'molecules/H2O_paw_12A_nspin2'
  # Checking if data folders exist
  if mode.endswith('dissociative') and surface.endswith('110H2O'):
    SURFADSORBATE = mode + '/Fe_110_2x2_SB_HO_LB_H_DOS'
  elif mode.endswith('molecular') and surface.endswith('110H2O'):
    SURFADSORBATE = mode + '/2x2_0.5ML_low_energy/Fe_110_2x2_H2O_top_5ML_DOS'
  elif mode.endswith('dissociative') and surface.endswith('100H2O'):
     SURFADSORBATE = mode + '/Fe_100_2x2_HO_FH_O_SB_0.25ML_DOS'
  elif mode.endswith('molecular') and surface.endswith('100H2O'):
    SURFADSORBATE = mode + '/2x2_0.5ML_low_energy/Fe_100_2x2_H2O_top_5ML_DOS'
  pathfiles.extend([ADSORBATE, SURFADSORBATE, CLEANSURF])

# Surfaces with adsorbates H2S
if surface.endswith('110H2S') or surface.endswith('100H2S'):
  # Adosrbate
  ADSORBATE = 'molecules/H2S_paw_12A_nspin2'
  # Checking if data folders exist
  if mode.endswith('dissociative') and surface.endswith('110H2S'):
    SURFADSORBATE = mode + '/Fe_110_2x2_SB_HS_LB_H_DOS'
  elif mode.endswith('molecular') and surface.endswith('110H2S'):
    SURFADSORBATE = mode + '/2x2_0.25ML_low_energy/Fe_110_2x2_H2S_SB_DOS'
  elif mode.endswith('dissociative') and surface.endswith('100H2S'):
    SURFADSORBATE = mode + '/Fe_100_2x2_H2S_FH_DOS'
  elif mode.endswith('molecular') and surface.endswith('100H2S'):
    SURFADSORBATE = mode + '/2x2_0.25ML_low_energy/Fe_100_2x2_H2S_top_25ML_DOS'
  pathfiles.extend([ADSORBATE, SURFADSORBATE, CLEANSURF])

########################### Template for LDOS & LPDOS Fe-Ads ##########################

SETTING_TERMINA_PNG = '''reset
#======================================================
#          Output settings terminals
#=====================================================

set terminal pngcairo size {width} ,{height} transparent enhanced font "Times-New-Roman, 22"  linewidth 2
set output '{filename_figure_output}'

'''
SETTING_TERMINAL_TEX = '''
reset
#======================================================
#          Output settings terminals
#=====================================================

set terminal epslatex size {widthcm40} cm , {heightcm40} cm color colortext 8
set output '{filename_figure_output}'

'''

SETTING_TERMINAL_PDF = '''
reset
#======================================================
#          Output settings terminals
#=====================================================

set terminal pdfcairo size {widthcm40} cm , {heightcm40} cm color enhanced font "Times-New-Roman, 12"  linewidth 2
set output '{filename_figure_output}'

'''
CANVAS_INITIAL_ROW = '''
# Canvas size and initial position variables
#===========================================
xsize= 0.4        # Controls the image x size in the canvas
ysize= 0.90        # Controls the image y size in the canvas

xleft=0.1   # Where is going to start the image
xrigth=0.05      # Space at the end
suma=0.05     # Where is going to appear the next plot

'''

CANVAS_INITIAL_COLUMN ='''
# Canvas size and initial position variables
#===========================================
xsize= 0.95   # Plot width in relation with canvas
ysize= 0.4   # Plot height in relation with canvas
xinit= 0.10   # The starting possition of the first plot

'''

GENERAL_STYLE_LINES = '''
#=======================================================
# 'GENERAL STYLE AND STYLE LINES ADJUSTMENTS'
#=======================================================

set termopt enhanced                   # Permite pone ^super/_{{sub}} indices
unset log                              # remove any log-scaling
unset label                            # remove any previous labels
set termoption dashed                  # Allows dash styles
set xtic 2                             # set xtics automatically
set ytic auto                          # set ytics automatically
#set style fill transparent solid {plotransparency} {bordertype}
set style fill  transparent pattern {plotransparency} {bordertype}
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

'''

SETTING_MULTIPLOT = '''
#=======================================================
#'       Settings of multiplot'
#=======================================================
set xlabel 'Energy [eV]' font "Times-New-Roman, 30" offset 0, 0.4
set multiplot layout {numberrows}, {numbercolum} columnsfirst

# set key at 0.5, 19 nobox
unset key

# Setting x,y range
#'******************'
 set xr {xrange}
 set yr {yrange}

# Reset keys
#'******************'
 unset bmargin
 unset tmargin

'''


PLOT_ROW_INDKEYS1 = r'''
###### 5th layer Plot

# Setting individual keys
#========================
# set xlabel 'Energy [eV]'
# set ylabel "DOS [states/eV]" offset 0,20
 set size xsize, ysize
 set tmargin at screen 0.95 # Controls the y final position
 set bmargin at screen 0.2  # Controls the y initial position
 set lmargin at screen xleft
 set rmargin at screen xleft + xsize
 set label "L5" at -9.5,-4
 set ylabel "LDOS [states/eV]" font "Times-New-Roman, 30" offset -1.1,0
'''

PLOT_ROW_INDKEYS2 = r'''
#================================================================
#     Second plot
#================================================================

#
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
 set label "LA" at -9.5,-4

'''

PLOT_COLUMN_INDKEYS1 =r'''
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
'''

PLOT_COLUMN_INDKEYS2 =r'''
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
'''

if type_of_plot == 2:
  SETTING_PLOT_PARAM = r'''
  plot "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:2 title "Total DOS clean sueface" with filledcurve y1=0 fs solid 0.7 ls 10 , \
       "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:3 title "" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with lines ls 10, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:3 title "" with lines ls 10, \
       "{pathfileadsor}/L{layer}/Fe_d_tot_L{layer}_shifted.dat"  using 1:2 title "3d ads" with filledcurve y1=0 fs transparent solid 0.8 ls 4, \
       "{pathfileadsor}/L{layer}/Fe_d_tot_L{layer}_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.8 ls 4, \
       "{pathfileadsor}/L{layer}/Fe_p_tot_L{layer}_shifted.dat"  using 1:2 title "3p ads" with filledcurve y1=0 fs transparent solid 0.8 ls 8, \
       "{pathfileadsor}/L{layer}/Fe_p_tot_L{layer}_shifted.dat"  using 1:3 title ""with filledcurve y1=0 fs transparent solid 0.8 ls 8;
'''
elif type_of_plot == 1:
  SETTING_PLOT_PARAM = r'''
  plot "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:2 title "Total DOS clean sueface" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:3 title "" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with lines ls 10, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:3 title "" with lines ls 10;
 '''

if type_of_plot == 1:
  LAST_PLOT_AND_END_CO2 = r'''
  plot   "{pathadsisolated}/O_tot_mole_CO2_shifted.dat" using 1:2 title "Total DOS O in CO2 molecule" with filledcurve y1=0 fs transparent solid 0.6 ls 2 , \
         "{pathadsisolated}/O_tot_mole_CO2_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.6 ls 2 , \
         "{pathadsisolated}/C_states/C_tot_mole_CO2_shifted.dat"  using 1:2 title "Total DOS C in CO2 molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 7 , \
         "{pathadsisolated}/C_states/C_tot_mole_CO2_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 7, \
         "{pathfileadsor}/LA/C_states/C_tot_LA_shifted.dat" using 1:2 title "Total DOS C on adsor" with lines ls 7, \
         "{pathfileadsor}/LA/C_states/C_tot_LA_shifted.dat" using 1:3 title "" with lines ls 7, \
         "{pathfileadsor}/LA/C_states/C_tot_LA_shifted.dat" using 1:2 title "Total DOS C on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 7, \
         "{pathfileadsor}/LA/C_states/C_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 7, \
         "{pathfileadsor}/LA/O_tot_LA_shifted.dat"  using 1:2 title "Total DOS O on adsor" with lines ls 2, \
         "{pathfileadsor}/LA/O_tot_LA_shifted.dat"  using 1:3 title "" with lines ls 2, \
         "{pathfileadsor}/LA/O_tot_LA_shifted.dat"  using 1:2 title "Total DOS O on adsor" with filledcurve y1=0 fs transparent pattern 5 ls 2, \
         "{pathfileadsor}/LA/O_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 5 ls 2;

   unset multiplot
   reset
  '''
  LAST_PLOT_AND_END_H2O = r'''
  plot   "{pathadsisolated}/O_states/O_p_tot_mole_H2O_shifted.dat"  using 1:2 title "Total DOS S in H2O molecule" with filledcurve y1=0 fs transparent solid 0.6 ls 2 , \
         "{pathadsisolated}/O_states/O_p_tot_mole_H2O_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.6 ls 2, \
         "{pathadsisolated}/H_tot_mole_H2O_shifted.dat" using 1:2 title "Total DOS H in H2O molecule" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathadsisolated}/H_tot_mole_H2O_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathfileadsor}/LA/O_states/O_tot_LA_shifted.dat" using 1:2 title "Total DOS O on adsor" with filledcurve y1=0 fs transparent pattern 5 ls 2, \
         "{pathfileadsor}/LA/O_states/O_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 5 ls 2, \
         "{pathfileadsor}/LA/O_states/O_tot_LA_shifted.dat" using 1:2 title "Total DOS O on adsor" with lines ls 2, \
         "{pathfileadsor}/LA/O_states/O_tot_LA_shifted.dat" using 1:3 title "" with lines ls 2, \
         "{pathfileadsor}/LA/H_tot_LA_shifted.dat"  using 1:2 title "Total DOS H on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 3, \
         "{pathfileadsor}/LA/H_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 3, \
         "{pathfileadsor}/LA/H_tot_LA_shifted.dat"  using 1:2 title "Total DOS H on adsor" with lines ls 3, \
         "{pathfileadsor}/LA/H_tot_LA_shifted.dat"  using 1:3 title "" with lines ls 3;

   unset multiplot
   reset
  '''
  LAST_PLOT_AND_END_H2S = r'''
  plot   "{pathadsisolated}/S_states/S_tot_mole_H2S_shifted.dat"  using 1:2 title "Total DOS S in H2S molecule" with filledcurve y1=0 fs transparent solid 1 ls 1 , \
         "{pathadsisolated}/S_states/S_tot_mole_H2S_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 1, \
         "{pathadsisolated}/H_tot_mole_H2S_shifted.dat" using 1:2 title "Total DOS H in H2S molecule" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathadsisolated}/H_tot_mole_H2S_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathfileadsor}/LA/S_states/S_tot_LA_shifted.dat" using 1:2 title "Total DOS S on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 1, \
         "{pathfileadsor}/LA/S_states/S_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 1, \
         "{pathfileadsor}/LA/S_states/S_tot_LA_shifted.dat" using 1:2 title "Total DOS S on adsor" with line ls 1, \
         "{pathfileadsor}/LA/S_states/S_tot_LA_shifted.dat" using 1:3 title "" with lines ls 1, \
         "{pathfileadsor}/LA/H_s_tot_LA_shifted.dat"  using 1:2 title "Total DOS H on adsor" with filledcurve y1=0 fs transparent pattern 5 ls 3, \
         "{pathfileadsor}/LA/H_s_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 5 ls 3, \
         "{pathfileadsor}/LA/H_s_tot_LA_shifted.dat"  using 1:2 title "Total DOS H on adsor" with lines ls 3, \
         "{pathfileadsor}/LA/H_s_tot_LA_shifted.dat"  using 1:3 title "" with lines ls 3;

   unset multiplot
   reset
  '''
elif type_of_plot == 2:
  LAST_PLOT_AND_END_CO2 = r'''
  plot   "{pathadsisolated}/C_states/C_tot_mole_CO2_shifted.dat"  using 1:2 title "Total DOS C in CO2 molecule" with lines ls 12 , \
         "{pathadsisolated}/C_states/C_tot_mole_CO2_shifted.dat"  using 1:3 title "" with lines ls 12, \
         "{pathadsisolated}/O_tot_mole_CO2_shifted.dat" using 1:2 title "Total DOS O in CO2 molecule" with lines ls 6, \
         "{pathadsisolated}/O_tot_mole_CO2_shifted.dat" using 1:3 title "" with lines ls 6, \
         "{pathadsisolated}/C_states/C_p_tot_mole_CO2_shifted.dat"  using 1:2 title "Total p DOS C in CO2 molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 16 , \
         "{pathadsisolated}/C_states/C_p_tot_mole_CO2_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 16, \
         "{pathadsisolated}/O_p_tot_mole_CO2_shifted.dat" using 1:2 title "Total p DOS O in CO2 molecule" with filledcurve y1=0 fs transparent solid 0.5 ls 16, \
         "{pathadsisolated}/O_p_tot_mole_CO2_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.5 ls 16, \
         "{pathadsisolated}/C_states/C_s_tot_mole_CO2_shifted.dat"  using 1:2 title "Total s DOS C in CO2 molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 17 , \
         "{pathadsisolated}/C_states/C_s_tot_mole_CO2_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 17, \
         "{pathadsisolated}/O_s_tot_mole_CO2_shifted.dat" using 1:2 title "Total s DOS O in CO2 molecule" with filledcurve y1=0 fs transparent solid 0.5 ls 17, \
         "{pathadsisolated}/O_s_tot_mole_CO2_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.5 ls 17, \
         "{pathfileadsor}/LA/C_states/C_tot_LA_shifted.dat" using 1:2 title "Total DOS C on adsor" with lines ls 18, \
         "{pathfileadsor}/LA/C_states/C_tot_LA_shifted.dat" using 1:3 title "" with lines ls 18, \
         "{pathfileadsor}/LA/O_tot_LA_shifted.dat" using 1:2 title "Total DOS O on adsor" with lines ls 2, \
         "{pathfileadsor}/LA/O_tot_LA_shifted.dat" using 1:3 title "" with lines ls 2, \
         "{pathfileadsor}/LA/C_states/C_p_tot_LA_shifted.dat" using 1:2 title "Total p DOS C on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 9, \
         "{pathfileadsor}/LA/C_states/C_p_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 9, \
         "{pathfileadsor}/LA/O_p_tot_LA_shifted.dat" using 1:2 title "Total p DOS O on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 9, \
         "{pathfileadsor}/LA/O_p_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 9, \
         "{pathfileadsor}/LA/C_states/C_s_tot_LA_shifted.dat" using 1:2 title "Total s DOS C on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 15, \
         "{pathfileadsor}/LA/C_states/C_s_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 15, \
         "{pathfileadsor}/LA/O_s_tot_LA_shifted.dat"  using 1:2 title "Total s DOS O on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 15, \
         "{pathfileadsor}/LA/O_s_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 15;

   unset multiplot
   reset
  '''

  LAST_PLOT_AND_END_H2O = r'''
  plot   "{pathadsisolated}/O_states/O_p_tot_mole_H2O_shifted.dat"  using 1:2 title "Total DOS S in H2O molecule" with lines ls 6, \
         "{pathadsisolated}/O_states/O_p_tot_mole_H2O_shifted.dat"  using 1:3 title "" with lines ls 6, \
         "{pathadsisolated}/H_tot_mole_H2O_shifted.dat" using 1:2 title "Total DOS H in H2O molecule" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathadsisolated}/H_tot_mole_H2O_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathadsisolated}/O_states/O_p_tot_mole_H2O_shifted.dat"  using 1:2 title "Total p DOS S in H2O molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 16 , \
         "{pathadsisolated}/O_states/O_p_tot_mole_H2O_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 16, \
         "{pathadsisolated}/O_states/O_s_tot_mole_H2O_shifted.dat"  using 1:2 title "Total p DOS S in H2O molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 17 , \
         "{pathadsisolated}/O_states/O_s_tot_mole_H2O_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 17, \
         "{pathfileadsor}/LA/O_states/O_tot_LA_shifted.dat" using 1:2 title "Total DOS O on adsor" with lines ls 2, \
         "{pathfileadsor}/LA/O_states/O_tot_LA_shifted.dat" using 1:3 title "" with lines ls 2, \
         "{pathfileadsor}/LA/H_tot_LA_shifted.dat" using 1:2 title "Total DOS H on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "{pathfileadsor}/LA/H_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "{pathfileadsor}/LA/O_states/O_p_tot_LA_shifted.dat" using 1:2 title "Total p DOS O on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 9, \
         "{pathfileadsor}/LA/O_states/O_p_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 9, \
         "{pathfileadsor}/LA/O_states/O_s_tot_LA_shifted.dat"  using 1:2 title "Total s DOS O on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 15, \
         "{pathfileadsor}/LA/O_states/O_s_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 15;

   unset multiplot
   reset
  '''

  LAST_PLOT_AND_END_H2S = r'''
  plot   "{pathadsisolated}/S_states/S_tot_mole_H2S_shifted.dat"  using 1:2 title "Total DOS S in H2S molecule" with lines ls 19 , \
         "{pathadsisolated}/S_states/S_tot_mole_H2S_shifted.dat"  using 1:3 title "" with lines ls 19, \
         "{pathadsisolated}/H_tot_mole_H2S_shifted.dat" using 1:2 title "Total DOS H in H2S molecule" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathadsisolated}/H_tot_mole_H2S_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent solid 1 ls 3, \
         "{pathadsisolated}/S_states/S_p_tot_mole_H2S_shifted.dat"  using 1:2 title "Total p DOS S in H2S molecule" with filledcurve y1=0 fs transparent solid 0.7 ls 16 , \
         "{pathadsisolated}/S_states/S_p_tot_mole_H2S_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.7 ls 16, \
         "{pathfileadsor}/LA/S_states/S_tot_LA_shifted.dat" using 1:2 title "Total DOS S on adsor" with lines ls 20, \
         "{pathfileadsor}/LA/S_states/S_tot_LA_shifted.dat" using 1:3 title "" with lines ls 20, \
         "{pathfileadsor}/LA/H_s_tot_LA_shifted.dat" using 1:2 title "Total DOS H on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "{pathfileadsor}/LA/H_s_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 3, \
         "{pathfileadsor}/LA/S_states/S_p_tot_LA_shifted.dat" using 1:2 title "Total p DOS S on adsor" with filledcurve y1=0 fs transparent pattern 4 ls 8 , \
         "{pathfileadsor}/LA/S_states/S_p_tot_LA_shifted.dat" using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 ls 8, \
         "{pathfileadsor}/LA/S_states/S_s_tot_LA_shifted.dat"  using 1:2 title "Total s DOS S on adsor" with filledcurve y1=0 fs transparent pattern 1 ls 15, \
         "{pathfileadsor}/LA/S_states/S_s_tot_LA_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 1 ls 15;

   unset multiplot
   reset
  '''
### function for types of plot LDOS or LPDOS
def typeplot():
  if type_of_plot == 1:
    f.write(SETTING_PLOT_PARAM.format(pathfilesclean=pathfiles[2],pathfileadsor=pathfiles[1],layer=5))
  elif type_of_plot == 2:
    f.write(SETTING_PLOT_PARAM.format(pathfilesclean=pathfiles[2],pathfileadsor=pathfiles[1],layer=5))

########################### Code to generate gnu #################################
with open('%s' % filename_gnuplot, 'w') as f:
  if filename_figure_output.endswith('.png'):
    print 'Terminal png'
    f.write(SETTING_TERMINA_PNG.format(
      filename_figure_output=filename_figure_output,
      width=width,
      height=height,
    ))
  elif filename_figure_output.endswith('.pdf'):
    print 'Terminal pdf'
    f.write(SETTING_TERMINAL_PDF.format(
      filename_figure_output=filename_figure_output,
      widthcm40=widthcm40,
      heightcm40=heightcm40,
    ))
  else:
    print 'Terminal tex'
    f.write(SETTING_TERMINAL_TEX.format(
      filename_figure_output=filename_figure_output,
      widthcm40=widthcm40,
      heightcm40=heightcm40,
    ))
  if panel_dist == 1:
    f.write(CANVAS_INITIAL_COLUMN)
    f.write(GENERAL_STYLE_LINES.format(
      plotransparency=plotransparency,
      bordertype=bordertype,
    ))
    f.write(SETTING_MULTIPLOT.format(
     numberrows=numberrows,
     numbercolum=numbercolum,
     xrange=xrange,
     yrange=yrange,
    ))
    f.write(PLOT_COLUMN_INDKEYS1)
    typeplot()
    f.write(PLOT_COLUMN_INDKEYS2)
    if adsorbate.endswith('CO2'):
      print 'CO2'
      f.write(LAST_PLOT_AND_END_CO2.format(
        pathadsisolated=pathfiles[0],
        pathfileadsor=pathfiles[1],
      ))
    elif adsorbate.endswith('H2O'):
      print 'H2O'
      f.write(LAST_PLOT_AND_END_H2O.format(
        pathadsisolated=pathfiles[0],
        pathfileadsor=pathfiles[1],
      ))
    elif adsorbate.endswith('H2S'):
      print 'H2S'
      f.write(LAST_PLOT_AND_END_H2S.format(
        pathadsisolated=pathfiles[0],
        pathfileadsor=pathfiles[1],
      ))
  elif panel_dist == 2:
    f.write(CANVAS_INITIAL_ROW)
    f.write(GENERAL_STYLE_LINES.format(
     plotransparency=plotransparency,
     bordertype=bordertype,
    ))
    f.write(SETTING_MULTIPLOT.format(
      numberrows=numberrows,
      numbercolum=numbercolum,
      xrange=xrange,
      yrange=yrange,
    ))
    f.write(PLOT_ROW_INDKEYS1)
    typeplot()
    f.write(PLOT_ROW_INDKEYS2)
  if adsorbate.endswith('CO2'):
    print 'CO2'
    f.write(LAST_PLOT_AND_END_CO2.format(
      pathadsisolated=pathfiles[0],
      pathfileadsor=pathfiles[1],
    ))
  elif adsorbate.endswith('H2O'):
    print 'H2O'
    f.write(LAST_PLOT_AND_END_H2O.format(
      pathadsisolated=pathfiles[0],
      pathfileadsor=pathfiles[1],
    ))
  elif adsorbate.endswith('H2S'):
    print 'H2S'
    f.write(LAST_PLOT_AND_END_H2S.format(
      pathadsisolated=pathfiles[0],
      pathfileadsor=pathfiles[1],
    ))


################## Running processes: tex and gnuplot ####################
if filename_figure_output.endswith('.tex'):
  with open('texgene.tex', 'w') as f:
    f.write(r'''\documentclass{article}
\usepackage{color}
\usepackage{graphicx}
\begin{document}
\input{%s}
\end{document}
''' % filename_figure_output)
  print 'Running gnulot and pdflatex:'
  subprocess.check_call('gnuplot %s' %filename_gnuplot , shell=True)
  subprocess.check_call('pdflatex texgene.tex', shell=True)
else:
  print 'Running gnuplot to generate png and pdf:'
  subprocess.check_call('gnuplot %s' %filename_gnuplot , shell=True)
