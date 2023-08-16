# importation des modules
import os
import serial
#import serial.tools.list_ports  # pour la communication avec le port série
import re
from optparse import OptionParser
from pathlib import Path
import math
import matplotlib.pyplot as plt  # pour le tracé de graphe
import matplotlib.colors as clr
from matplotlib import animation  # pour la figure animée
import time  # gestion du temps
import pylab
from pylab import *
import matplotlib.gridspec as gridspec


parser = OptionParser(usage='usage: %prog FILE_NAME')
(options, args) = parser.parse_args()


#runnerName = re.split('[/.]', args[0])[-2]
print(args[0])
fileName = args[0]
Couleur = []



V_ampoule_1, V_ampoule2, V_moteur, V_thermo_P1, V_thermo_P2, V_thermo_batterie, V_photo_P1, V_photo_P2, BusVoltage_batterie, ShuntVoltage_batterie, Current_batterie, Power_batterie, BusVoltage_P1, ShuntVoltage_P1, Current_P1, Power_P1, BusVoltage_P2, ShuntVoltage_P2, Current_P2, Power_P2, temps = np.loadtxt(
    str(fileName), delimiter=';', unpack=True)
theta = V_photo_P1.copy() #just to get the same size as V_photo_P1


'''
#Estimation of the luminosity peak, only right for data59.txt
debut = 16500
fin = 21000
etape = (fin-debut)/6 #6 variations de couleurs, R, RG, RB, G, GB, B
#print(V_photo_P1)
for i in range(size(temps)):
    if i < debut: 
        Couleur.append((0,0,0)) #Noir au debut
    elif i < debut+etape:
        Couleur.append(((i-(debut))/etape,0,0)) #Devient rouge
    elif i < debut+2*etape:
        Couleur.append((1,(i-(debut+etape))/etape,0)) #Devient rouge+vert
    elif i < debut+3*etape:
        Couleur.append(((1-((i-(debut+2*etape))/etape)),1,0)) #devient vert
    elif i < debut+4*etape:
        Couleur.append((0,1,(i-(debut+3*etape))/etape))#devient vert+bleu
    elif i < debut+5*etape:
        Couleur.append((0,(1-((i-(debut+4*etape))/etape)),1))#devient bleu
    elif i < debut+6*etape:
        Couleur.append((((i-(debut+5*etape))/etape),0,1))#devient bleu+rouge
    else :
        Couleur.append((0.75,0.75,0.75))

#print((Couleur))

cmap = clr.LinearSegmentedColormap.from_list('Map_couleur', Couleur, N=etape)
norm=plt.Normalize(-2,2)
cmap2 = clr.ListedColormap(Couleur)
cmap3 = clr.ListedColormap(["darkorange", "gold", "lawngreen", "lightseagreen"])
test_coul=np.linspace(0,size(temps),size(temps))
'''

''' To get arrows from point A to point B 
arrow_len = 0.5
count = 0
for i in range(len(temps)-1):
    #if count%10 == 0:
    theta[i] = math.atan2(Current_P1[i+1]-Current_P1[i],V_photo_P1[i+1]-V_photo_P1[i])
    plt.arrow(V_photo_P1[i], Current_P1[i], V_photo_P1[i+1], Current_P1[i+1], head_width=.005, color=Couleur[i], lw=2)
    #plt.arrow(V_photo_P1[i], Current_P1[i], np.cos(theta[i])*arrow_len, np.sin(theta[i])*arrow_len, head_width=.1, color=Couleur[i], lw=2)

    count = count+ 1

plt.show()
'''



"""
# Création de la figure
plt.figure(1)
plt.subplot(1, 2, 1)
plt.xlabel('temps (s)')
plt.ylabel('Current P1 (mA)')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P1)))
plt.title('Courrant Total en fonction du temps')
plt.plot(temps, Current_P1)
plt.grid()


plt.subplot(1, 2, 2)
plt.xlabel('temps (s)')
plt.ylabel('Current P2 (mA)')
plt.title('Courant P2 en fonction du temps')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P2)))
plt.plot(temps, Current_P2)
plt.grid()
plt.show()
"""
#Test luminosité

plt.figure(1)
plt.subplot(2, 3, 1)
plt.xlabel('lum P1(lux)')
plt.ylabel('Current P1 (mA)')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P1)))
plt.title('Courrant P1 en fonction de la lum')

#If colored:
#plt.scatter(V_photo_P1, Current_P1, s=2, c=test_coul, cmap= cmap2, alpha=0.3)

#If not colored:
plt.scatter(V_photo_P1, Current_P1)


#plt.plot(V_photo_P1, Current_P1)

plt.colorbar()
plt.grid()


plt.subplot(2, 3, 2)
plt.xlabel('temps (s)')
plt.ylabel('Lum (lux)')
plt.title('Lum P1 en fonction du temps')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P2)))

#If colored:
#plt.scatter(temps, V_photo_P1,s=2, c=Couleur)

#If not colored:
plt.scatter(temps, V_photo_P1)
plt.grid()

plt.subplot(2, 3, 3)
plt.xlabel('temps (s)')
plt.ylabel('Courant (mA)')
plt.title('Courant P1 en fonction du temps')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P2)))

plt.scatter(temps, Current_P1,s=2)


plt.grid()

plt.subplot(2, 3, 4)
plt.xlabel('lum P2(lux)')
plt.ylabel('Current P2 (mA)')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P1)))
plt.title('Courrant P2 en fonction de la lum')
plt.scatter(V_photo_P2, Current_P2, s=2)
plt.grid()


plt.subplot(2, 3, 5)
plt.xlabel('temps (s)')
plt.ylabel('Lum (lux)')
plt.title('Lum P2 en fonction du temps')
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P2)))
plt.scatter(temps, ShuntVoltage_batterie,s=2)
plt.grid()

plt.subplot(2, 3, 6)
plt.xlabel('temps (s)')
plt.ylabel('Courant (mA)')
plt.title('Courant batterie en fonction du temps')#remettre P2
#xlim(0, 60)
#ylim(-10, max(10, max(Current_P2)))
plt.scatter(temps, BusVoltage_batterie,s=2)
plt.grid()



plt.show()

"""
# Création de la figure
plt.figure(2)
gs = gridspec.GridSpec(2, 2)
plt.subplot(gs[0, 0])
plt.xlabel('temps (s)')
plt.ylabel('Current Batterie (mA)')
#xlim(0, 60)
#ylim(0, 100)
plt.title('Courrant Batterie en fonction du temps')
plt.plot(temps, Current_batterie)
plt.grid()

plt.subplot(gs[0, 1])
plt.xlabel('temps (s)')
plt.ylabel('Tension Batterie (mA)')
#xlim(0, 60)
#ylim(0, 100)
plt.title('Tension Batterie en fonction du temps')
plt.plot(temps, BusVoltage_batterie)
plt.grid()

plt.subplot(gs[1, :])
plt.xlabel('temps (s)')
plt.ylabel('Puissance Batterie (mW)')
plt.title('Puissance Batterie en fonction du temps')
#xlim(0, 60)
#ylim(0, 4.2)
plt.plot(temps, Power_batterie)
plt.grid()
plt.show()


# figure Charges
plt.figure(3)
gs = gridspec.GridSpec(2, 2)
plt.subplot(gs[0, 0])
plt.xlabel('temps (s)')
plt.ylabel('Tension Ampoule 1 (V) ')
#xlim(0, 60)
ylim(0, max(1, max(V_ampoule_1)+1))
plt.title('Tension Ampoule 1 en fonction du temps')
plt.plot(temps, V_ampoule_1)
plt.grid()


plt.subplot(gs[0, 1])
plt.xlabel('temps (s)')
plt.ylabel('Tension Ampoule 2 (V) ')
#xlim(0, 60)
ylim(0, max(1, max(V_ampoule2)+1))
plt.title('Tension Ampoule 2 en fonction du temps')
plt.plot(temps, V_ampoule2)
plt.grid()


plt.subplot(gs[1, :])
plt.xlabel('temps (s)')
plt.ylabel('Tension Moteur (V)')
plt.title('Tension Moteur en fonction du temps')
#xlim(0, 60)
ylim(0, max(1, max(V_moteur)+1))
plt.plot(temps, V_moteur)
plt.grid()
plt.show()
"""