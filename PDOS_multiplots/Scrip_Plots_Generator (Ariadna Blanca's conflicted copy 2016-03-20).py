#!/usr/bin/env python

### Script for Gnuplot template for LDOS & PDOS with 5 or 6 rows and 1 column

import subprocess
import os
import sys
# parser = parser.ArgumentParser("Ploting Density of States gnuplot")
#parser.add_argument('-x', nargs='+') # nargs allows to pass one or more arguments
# args = parser.parse_args()

#args.x ## is a list of the arguments passed

######################## Variables ###########################################
filename_figure_output = raw_input('Name of the figure (ext: png, tex or pdf; e.g. temultipleplots_6sc.png):')
filename_gnuplot = raw_input('Name of the gnuplot file (ext: gnu, e.g. graphs_ldos_Feads.gnu):')
# clean: 110 or 100; surfadso: 110CO2, 110H2O, 100H2S;
surface = raw_input('Surface to be ploted (clean: 110 or 100; adsorbates: 110CO2, 110H2O, 110H2S, 100CO2, 100H2O, 100H2S):')
# Adsorbate
adsorbate = surface[3:]
print adsorbate
# modes: dissociative, molecular
modeoptions = int(raw_input('Asdoerptopn type 1) dissociative 2) molecular 3) clean surface:'))
numberboxes = 0
if modeoptions == 1:
  mode = 'dissociative'
  numberboxes = 6
elif  modeoptions == 2:
  mode = 'molecular'
  numberboxes = 6
elif  modeoptions == 3:
  mode = ''
  numberboxes = 5
type_of_plot = int(raw_input('1) Plot Total LDOS, 2)Plot PLDOS: '))


######### Figure Size ###############
width = 1400
height = 950
pixelincm = 0.026458333
# 40 % of the size in pixels
widthtocm_40porcent = (width * pixelincm) * 0.40
heightocm_40porcent = (height * pixelincm) * 0.40
widthcm40 = '{0:0.4}'.format(widthtocm_40porcent)
heightcm40 = '{0:0.4}'.format(heightocm_40porcent)

### Variables to calculate divison of canvas for stacking graphs
bottotopmargin = 0.05
topmargin = 0.1
heightboxes = (1 - (bottotopmargin + topmargin )) / numberboxes
ysize = float('{0:0.2}'.format(heightboxes))

# Estimation of the quantity missing to be added to topmargin
topsum = ( 1 - ((ysize * numberboxes) + topmargin + bottotopmargin))
topmargin = topmargin + topsum

margins_tb = []

for i in range(numberboxes):
  tmargin =  topmargin + (i + 1) * ysize
  bmargin =  topmargin + i * ysize
  margins_tb.append({'tmargin': tmargin, 'bmargin': bmargin})

######## gnuplot varaibles
plotransparency = 0.9
xrange = "[-10:8]"
yrange = "[-3:3]"
bordertype = 'border'

######### Searching for Input files
WORK_DIR = os.getcwd()
print 'Working directory:'
print WORK_DIR
clean_layers = {}
adsorbate_layers = {}
molecule = {}
pathfiles = [] # List to append paths source files [ADSORBATE, SURFADSORBATE, CLEANSURF]

# Function that finds files ending with "shifted.dat" where we store the
# names of our inputfiles to plot graph
def findata(dirname):
  files = os.listdir(dirname)
  files = [f for f in files if f.endswith('shifted.dat')]
  return files

# Function that builds the directories with the names of input files for plotting.
# This dictionaries are constructed if the case is a clan surface or surface + ads
def dictionaryconstruction(adsor,pathfiles):
  # If adsorbate exist builds molecule and adsorbate_layers directories
  if adsor:
    if adsor.endswith('H2O'):
      atomspecie = '/O_states'
      index1 = 'O'
      index2 = 'H'
    elif adsor.endswith('H2S'):
      atomspecie = '/S_states'
      index1 = 'S'
      index2 = 'H'
    elif adsor.endswith('CO2'):
      atomspecie = '/C_states'
      index1 = 'C'
      index2 = 'O'
    try:
      print ' -------------------------------------------------'
      print 'Path fiels isolated adsorbate:', pathfiles
      print ' '
      print 'Seting up files:'
      molecule[index1] = findata(pathfiles[0]+ atomspecie)
      molecule[index2] = findata(pathfiles[0])
      print molecule
      print ' -------------------------------------------------'
      print 'Seting up files for plotting surface with adsorbate'
      print ' '
      print 'Path fiels system + adsrobate:', pathfiles[1]
      print ' '
      for i in range(5):
        adsorbate_layers['L' + str(i + 1)] = findata(pathfiles[1] + '/L' + str(i + 1))
        adsorbate_layers['L' + index1] = findata(pathfiles[1] + '/LA' + atomspecie)
        adsorbate_layers['L' + index2] = findata(pathfiles[1] + '/LA')
      print adsorbate_layers
      print ' '
      print ' -------------------------------------------------'
      print 'Path fiels clean:', pathfiles[2]
      print ' '
      print 'Seting up files for plotting clean surface'
      print ' '
      for i in range(5):
        clean_layers['L' + str(i + 1)] = findata(pathfiles[2] + '/L' + str(i + 1))
      print clean_layers
    except OSError:
      print 'The path was not found; There is not data to plot'
      sys.exit(0)
  # If adsorbates does not exit we take just into account the clean surface
  else:
    try:
      print ' -------------------------------------------------'
      print 'Path:', pathfiles[2]
      print ' '
      print 'Seting up files for plotting clean surface'
      print ' '
      for i in range(5):
        clean_layers['L' + str(i + 1)] = findata(pathfiles[2] + '/L' + str(i + 1))
      print clean_layers
    except OSError:
      print 'The path was not found; There is not data to plot'
      sys.exit(0)



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
  dictionaryconstruction(adsorbate, pathfiles)

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
  dictionaryconstruction(adsorbate, pathfiles)

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
  dictionaryconstruction(adsorbate, pathfiles)

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
  dictionaryconstruction(adsorbate, pathfiles)


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

CANVAS_INITIAL = '''
# Canvas size and initial position variables
#===========================================
xsize= 0.95    # Plot width in relation with canvas
ysize= {ysize}   # Plot height in relation with canvas

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

set arrow nohead front from 0, -3 to 0, 3 ls 12
set xzeroaxis ls 12

'''

SETTING_MULTIPLOT = '''
#=======================================================
#'       Settings of multiplot'
#=======================================================
set xlabel 'Energy [eV]' font "Times-New-Roman, 30" offset 0, 0.4
set multiplot layout {numberboxes},1 columnsfirst

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

FIRST_PLOT_WITH_KEYS = r'''
# Setting individual keys
#========================
 set size xsize, ysize
 set tmargin at screen {tentry} # Controls the y final position
 set bmargin at screen {bentry}  # Controls the y initial position
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L1" at -9.5,-2.2
'''


NUMBER_OF_PLOT = '''
#================================================================
#     {number} plot
#================================================================
'''

RESET_KEYS_NEXT_PLOTS = '''
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
 unset ytics
 set ytics format " "

'''

SETTINGS_NEXT_PLOTS_KEYS = '''
# Set individual keys
 set size xsize, ysize
 set tmargin at screen {tentry}
 set bmargin at screen {bentry}
 set lmargin at screen 0.1
 set rmargin at screen 0.90
 set label "L{layer}" at -9.5,-2.2
'''

if type_of_plot == 1 and numberboxes == 6:
  SETTING_PLOT_PARAM = r'''
  plot "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:2 title "Total DOS clean sueface" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:3 title "" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent pattern 4 border ls 11, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:2 title "Total DOS  sueface ads" with lines ls 10, \
       "{pathfileadsor}/L{layer}/Fe_tot_L{layer}_shifted.dat"  using 1:3 title "" with lines ls 10;
 '''

elif type_of_plot == 1 and numberboxes == 5:
  SETTING_PLOT_PARAM = r'''
  plot "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:2 title "Total DOS clean sueface" with filledcurve y1=0 fs solid 0.7 ls 10 , \
       "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:3 title "" with filledcurve y1=0 fs solid 0.7 ls 10;
  '''

elif type_of_plot == 2 and numberboxes == 6:
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

elif type_of_plot == 2 and numberboxes == 5:
  SETTING_PLOT_PARAM = r'''
  plot "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:2 title "Total DOS clean sueface" with filledcurve y1=0 fs solid 0.7 ls 10 , \
       "{pathfilesclean}/L{layer}/Fe_tot_L{layer}_shifted.dat"   using 1:3 title "" with filledcurve y1=0 fs solid 0.7 ls 10, \
       "{pathfilesclean}/L{layer}/Fe_d_tot_L{layer}_shifted.dat"  using 1:2 title "3d clean" with filledcurve y1=0 fs transparent solid 0.8 ls 4 , \
       "{pathfilesclean}/L{layer}/Fe_d_tot_L{layer}_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.8 ls 4, \
       "{pathfilesclean}/L{layer}/Fe_p_tot_L{layer}_shifted.dat"  using 1:2 title "3d clean" with filledcurve y1=0 fs transparent solid 0.8 ls 8, \
       "{pathfilesclean}/L{layer}/Fe_p_tot_L{layer}_shifted.dat"  using 1:3 title "" with filledcurve y1=0 fs transparent solid 0.8 ls 8;
  '''

LAST_SECTION_5LAYER = '''
 unset multiplot
 reset
 '''

YLABEL = '''
 set ylabel "LDOS [states/eV]" font "Times-New-Roman, 30" offset -1,-2

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
def typeplot(number):
  if type_of_plot == 1 and numberboxes == 5:
    f.write(SETTING_PLOT_PARAM.format(pathfilesclean=pathfiles[2],layer=number))
  elif type_of_plot == 1 and numberboxes == 6:
    f.write(SETTING_PLOT_PARAM.format(pathfilesclean=pathfiles[2],pathfileadsor=pathfiles[1],layer=number))
  elif type_of_plot == 2 and numberboxes == 6:
    f.write(SETTING_PLOT_PARAM.format(pathfilesclean=pathfiles[2],pathfileadsor=pathfiles[1],layer=number))
  elif type_of_plot == 2 and numberboxes == 5:
    f.write(SETTING_PLOT_PARAM.format(pathfilesclean=pathfiles[2],layer=number))

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
  f.write(CANVAS_INITIAL.format(
    ysize=ysize,
  ))
  f.write(GENERAL_STYLE_LINES.format(
    plotransparency=plotransparency,
    bordertype=bordertype,
  ))
  f.write(SETTING_MULTIPLOT.format(
    numberboxes=numberboxes,
    xrange=xrange,
    yrange=yrange,
  ))
  f.write(FIRST_PLOT_WITH_KEYS.format(
    tentry=margins_tb[0]['tmargin'],
    bentry=margins_tb[0]['bmargin'],
  ))
  ### First plot
  typeplot(1)
  for i in range(numberboxes-1):
    f.write(NUMBER_OF_PLOT.format(
    number=i+2
    ))
    f.write(RESET_KEYS_NEXT_PLOTS)
    f.write(SETTINGS_NEXT_PLOTS_KEYS.format(
         tentry=margins_tb[i+1]['tmargin'],
         bentry=margins_tb[i+1]['bmargin'],
         layer=i+2,
       ))
    if i < 2:
      typeplot(i+2)
    if i == 2:
      f.write(YLABEL)
      typeplot(i+2)
    elif i == 3 and numberboxes == 5:
      typeplot(i+2)
      f.write(LAST_SECTION_5LAYER)
    elif i == 3 and numberboxes == 6:
      typeplot(i+2)
    elif i == 4 and adsorbate:
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
       else:
         print 'Clean surface'

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

