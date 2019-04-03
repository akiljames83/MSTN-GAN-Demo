from pymol import cmd
from random import random as rand
from math import floor

'''
Author: Akil Hamilton
Description: Script to simulate the gene mutation of GAN Auto Encoder.
'''
COLORS = [
	['br9', 'br2'],
	['carbon','brightorange'],
	['deepsalmon','deeppurple'],
	['slate','firebrick'],
	['deepteal','br9'],
	['lightmagenta','lightorange'],
	#['lime','magenta'],
	['oxygen','smudge'],
	['violet','orange']
]

AXES = [
	'x',
	'y',
	'z'
]

GENE = '5f3b'
NUM_IMAGES = 12

# Fetch the gene from PDB
cmd.fetch(GENE, quiet=0)

# Clean Up gene representation
cmd.show("cartoon")
cmd.hide("lines")
cmd.set_view ([
    -0.090915471,   -0.583907545,    0.806714714,\
    -0.680931926,    0.627556562,    0.377493620,\
    -0.726678491,   -0.514997303,   -0.454657555,\
     0.000238538,    0.000451565, -545.061767578,\
  -100.496780396,   -9.033477783,   97.704284668,\
   -20.180725098, 1110.239257812,  -20.000000000 ])

for i in range(NUM_IMAGES):
	SITE = floor(rand()*200)
	AXIS = AXES[floor(rand()*(len(AXES) - 1))]
	DEG = floor(10+rand()*38)

	if (AXIS == 'y'):
		DEG %= 15

	color_index = floor(rand()*(len(COLORS) - 1))
	color1 = COLORS[color_index][0]
	color2 = COLORS[color_index][1]

	cmd.color(color1)
	cmd.do("color %s, resi %s" % (color2, SITE))
	cmd.do("show sticks, resi %s" % SITE)

	# Mutagenesis at specified site
	cmd.do('wizard mutagenesis')
	cmd.do('refresh_wizard')
	cmd.get_wizard().do_select("%d" % SITE + '/')
	cmd.get_wizard().apply()

	cmd.do("rotate %s, %d" % (AXIS, DEG))

	# Previous selection: selection="resi %d" % SITE
	cmd.zoom(selection="all", buffer=0.001, complete=0)
	cmd.zoom(selection="resi 100", buffer=25, complete=0)
	cmd.save("img/img_{}".format(i+1), format="png")
	cmd.do("rotate %s, %d" % (AXIS, -DEG))
