from pymol import *
from random import random as rand
from math import floor

'''
Documentation to interact with the pymol interface:
- https://pymol.org/pymol-command-ref.html
- https://pymol.org/dokuwiki/?id=api
- https://pymol.org/dokuwiki/doku.php?id=api:cmd:alpha
- https://pymolwiki.org/index.php/Windows_Install
- https://sourceforge.net/p/pymol/mailman/message/29938948/
- https://pastebin.com/nDTZApHP
'''

gene = "5f3b"

cmd.fetch(gene, quiet=0)
cmd.show("cartoon")
cmd.hide("lines")
cmd.color("slate")
#cmd.select("")
site = '200'
cmd.do("color firebrick, resi %s" % site)
cmd.do("show sticks, resi %s" % site)
#cmd.color("slate, resi 200")
#cmd.wizard("nucmutagenesis")
#w = cmd.get_wizard()
cmd.do('wizard mutagenesis')
cmd.do('refresh_wizard')
#cmd.get_wizard().set_mode(variant)
cmd.get_wizard().do_select(site + '/')
cmd.get_wizard().apply()
w = cmd.get_wizard()
#cmd.get_wizard('sele ')
print(type(w))
# cmd.draw(300, 300, quiet=0)
cmd.set_view ([
    -0.090915471,   -0.583907545,    0.806714714,\
    -0.680931926,    0.627556562,    0.377493620,\
    -0.726678491,   -0.514997303,   -0.454657555,\
     0.000238538,    0.000451565, -545.061767578,\
  -100.496780396,   -9.033477783,   97.704284668,\
   -20.180725098, 1110.239257812,  -20.000000000 ])
cmd.zoom(selection="resi 100", buffer=20, complete=0)
cmd.save(gene, format="png")