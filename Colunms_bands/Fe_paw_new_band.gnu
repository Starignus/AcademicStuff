 set xzeroaxis linetype 0 linewidth 2.5
 set ylabel "Energy (eV)" font "Helvetica,20"
 set ytics font "Helvetica,16"
 set xtics font "Helvetica,16"
 set mytics 5
set style data lines
set nokey
set xrange [0:11.41566]
set yrange [-70.83560 : 59.11570]
set arrow from  2.21824, -70.83560 to  2.21824,  59.11570 nohead
set arrow from  3.78678, -70.83560 to  3.78678,  59.11570 nohead
set arrow from  5.35531, -70.83560 to  5.35531,  59.11570 nohead
set arrow from  7.27636, -70.83560 to  7.27636,  59.11570 nohead
set arrow from  8.38548, -70.83560 to  8.38548,  59.11570 nohead
set arrow from  9.49460, -70.83560 to  9.49460,  59.11570 nohead
set xtics (" G "  0.00000," H "  2.21824," N "  3.78678," G "  5.35531," P "  7.27636," N "  8.38548," P "  9.49460," H " 11.41566)
 plot "Fe_paw_new_band.dat" u 1:($2-18.2755),"Fe_paw_new_band.dat" u 1:($3-18.2755) lt 3
 plot "Merge_crystal_scalex.dat" u 1:($2),"Merge_crystal_scalex.dat" u 1:($3) lt 2
 set xzeroaxis linetype 0 linewidth 2.5
 set ylabel "Energy (eV)" font "Helvetica,20"
 set ytics font "Helvetica,16"
 set xtics font "Helvetica,16"
 set mytics 5
 set term postscript enhance color "Helvetica" 13
 set output "Fe_paw_new_band.ps"
 replot
 replot
 set term png enhanced font "Helvetica" 13  size 1280,1024
 set output "Fe_paw_new_band.png"
 replot
