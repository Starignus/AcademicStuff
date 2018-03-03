

'''
Note for plots page 142 manual:
Syntax:
set style line <index> default
set style line <index> {{linetype | lt} <line_type> | <colorspec>}
{{linecolor | lc} <colorspec>}
{{linewidth | lw} <line_width>}
{{pointtype | pt} <point_type>}
{{pointsize | ps} <point_size>}
{{pointinterval | pi} <interval>}
{palette}
unset style line
show style line

Syntax (p132):
too see palette:
set palette

set palette {
{ gray | color }
{ gamma <gamma> }
{ rgbformulae <r>,<g>,<b>
| defined { ( <gray1> <color1> {, <grayN> <colorN>}... ) }
| file ’<filename>’ {datafile-modifiers}
| functions <R>,<G>,<B>
}
{ model { RGB | HSV | CMY | YIQ | XYZ } }
{ positive | negative }
{ nops_allcF | ps_allcF }
{ maxcolors <maxcolors> }
}
show palette
show palette palette <n> {{float | int}}
show palette gradient
show palette fit2rgbformulae
show palette rgbformulae
show colornames

gnuplot> set palette defined
gnuplot> show colornames

Syntax (p142):
set style fill {empty
| {transparent} solid {<density>}
| {transparent} pattern {<n>}}
{border {lt} {lc <colorspec>} | noborder}

'''

Functions and data may be displayed in one of a large number of styles. The with keyword provides
the means of selection.
Syntax: (p 85)
with <style> { {linestyle | ls <line_style>}
| {{linetype | lt <line_type>}
{linewidth | lw <line_width>}
{linecolor | lc <colorspec>}
{pointtype | pt <point_type>}
{pointsize | ps <point_size>}
{fill | fs <fillstyle>}
{nohidden3d} {nocontours} {nosurface}
{palette}}
}
where <style> is one of
lines dots steps errorbars xerrorbar xyerrorlines
points impulses fsteps errorlines xerrorlines yerrorbars
linespoints labels histeps financebars xyerrorbars yerrorlines
vectors
86 gnuplot 4.4 65 PLOT
or
boxes candlesticks image circles
boxerrorbars filledcurves rgbimage
boxxyerrorbars histograms rgbalpha pm3d


Syntax: (p 141)
set style fill {empty
| {transparent} solid {<density>}
| {transparent} pattern {<n>}}
{border {lt} {lc <colorspec>} | noborder}
