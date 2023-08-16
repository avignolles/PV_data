import os
import serial
#import serial.tools.list_ports  # pour la communication avec le port série
import re
import numpy as np
from optparse import OptionParser
from pathlib import Path
import matplotlib.pyplot as plt  # pour le tracé de graphe
from matplotlib import animation  # pour la figure animée
import time  # gestion du temps
import pylab
from pylab import *
import matplotlib.gridspec as gridspec

X=[1,1.5,2,2.5]
Y=[1,1.5,2,2.5]
AUR = u'$\u2197$'
AUL = u'$\u2196$'
ALL = u'$\u2198$'
ALR = u'$\u2198$'
M=[AUR,AUL,ALL,ALR]

C=[(1,0,0),(2/3,0,1/3),(1/3,0,2/3),(0,0,1)]
print(size(Y))
plt.figure(1)
plt.scatter(X,Y, c=C, marker = AUL)
plt.show()
#C.append(('Z','Z','Z'))
#print(C)