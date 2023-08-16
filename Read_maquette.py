# importation des modules
import os
import serial
import serial.tools.list_ports  # pour la communication avec le port série

from pathlib import Path
import matplotlib.pyplot as plt  # pour le tracé de graphe
from matplotlib import animation  # pour la figure animée
import time  # gestion du temps
import pylab
from pylab import *

# initialisation des listes

liste_temps_mesure = []  # liste pour stocker le temps machine absolu
liste_temps = []  # liste pour stocker les valeurs de temps normalisé à t=0
liste_V_ampoule_1 = []  # liste tension ampoule 1
liste_V_ampoule_2 = []  # liste tension ampoule 2
liste_V_moteur = []  # liste tension moteur
liste_V_termo_P1 = []  # liste temperature panneau 1 (gauche)
liste_V_termo_P2 = []  # liste temperature panneau 2 (droite)
liste_V_termo_batterie = []  # liste temperature batterie
liste_V_photo_P1 = []  # liste luminosité panneau 1 (gauche)
liste_V_photo_P2 = []  # liste luminosité panneau 2 (droite)
liste_BusVoltage_batterie = []  # liste tension batterie
liste_ShuntVoltage_batterie = []  # liste shunt batterie
liste_Current_batterie = []  # liste courant batterie
liste_Power_batterie = []  # liste puissance batterie
liste_BusVoltage_P1 = []  # liste tension panneau 1 (gauche)
liste_ShuntVoltage_P1 = []  # liste shunt panneau 1 (gauche)
liste_Current_P1 = []  # liste courant panneau 1 et panneau 2
liste_Power_P1 = []  # liste puissance panneau 1 et panneau 2
liste_BusVoltage_P2 = []  # liste tension panneau 2 (droite)
liste_ShuntVoltage_P2 = []  # liste shunt panneau 2 (droite)
liste_Current_P2 = []  # liste courant panneau 2 (droite)
liste_Power_P2 = []  # liste puissance panneau 2 (droite)

# temps de l'acquisition que l'on souhaite (en seconde)
# t_acquisition = 60*60*3   \\ 3 heures
t_acquisition = 60*60*72
distancemax = 5  # en mm
V_ampoule_1 = 0
V_ampoule_2 = 0

# Fonction utilisées


def recup_port_Arduino():
    ports = list(serial.tools.list_ports.comports())
    for p in ports:
        if 'Arduino' in p.description:
            mData = serial.Serial(p.device, 9600)
    # Affiche et vérifie que le port est ouvert
    print("Port ouvert: "+str(mData.is_open))
    print("Nom du port: "+str(mData.name))  # Affiche le nom du port
    return mData


def nettoie(L):  # L est une liste
    newL = []  # Déclaration de la liste en fin de netoyage
    temp = L[2:]      # On retire les deux premiers caractères
    # On retire les 5 derniers caractères et on ajoute le resultat à newL
    newL.append(temp[:-5])
    return newL  # On retourne la liste nettoyée


def mesure_temps():
    tempsmes = time.time()  # Temps système
    # Sauvegarde du temps au lancement du programme
    liste_temps_mesure.append(tempsmes)
    # Temps écoulé depuis le lancement du programme
    tempsreel = tempsmes - liste_temps_mesure[0]
    return tempsreel


def Creation_save():
    cpt = 0
    fileNameBase = r"/home/avignolles/Desktop/N7/Projet_Long_2023/Recup_data/Python/data"
    fileName = r"/home/avignolles/Desktop/N7/Projet_Long_2023/Recup_data/Python/data.txt"
    while os.path.exists(fileName):
        cpt += 1
        fileName = fileNameBase + str(cpt) + ".txt"
        #print("Tentative de créer: " + str(fileName))

    #print("Fichier crée = " + str(fileName))
    file = open(str(fileName), mode="w")
    file.close()
    return fileName


def Save(FileName, cleandata):
    # c ouverture du fichier en mode écriture (ajout)
    file = open(str(FileName), mode="a")
    file.write(cleandata[0] + ';' + cleandata[1] + '\n')
    file.close()


# Comportement principale

FileName = Creation_save()  # Création d'un fichier txt
print("Fichier de sauvegarde: "+str(FileName))
Data = recup_port_Arduino()  # Lecture des données sur le port serie
temps_actuel = 0
while temps_actuel <= t_acquisition:

    # Stockage de la lecture en cours dans rawdata[0]
    rawdata = str(Data.readline())
    print("data BRUT= "+str(rawdata))
    # Nettoyage des données et stockage dans cleandata[0]
    cleandata = nettoie(rawdata)
    print("data CLEAN:"+str(cleandata))
    # Mesure du temps actuel avec 3 chiffres significatifs
    temps_actuel = round(mesure_temps(), 3)
    #print("temps actuel = " + str(temps_actuel))
    cleandata.append(str(temps_actuel))  # Ajout du temps dans cleandata[1]
    print("data CLEAN et TEMPS= "+str(cleandata))
    # Sauvegarde du jeu de valeurs dans le fichier txt
    Save(FileName, cleandata)

V_ampoule_1, V_ampoule2, V_moteur, V_termo_P1, V_termo_P2, V_termo_batterie, V_photo_P1, V_photo_P2, BusVoltage_batterie, ShuntVoltage_batterie, Current_batterie, Power_batterie, BusVoltage_P1, ShuntVoltage_P1, Current_P1, Power_P1, BusVoltage_P2, ShuntVoltage_P2, Current_P2, Power_P2, temps = np.loadtxt(
    str(FileName), delimiter=';', unpack=True)

# Création de la figure
plt.subplot(1, 2, 1)
plt.xlabel('Temps (s)')
plt.ylabel('Courant Total (mA)')
plt.title('Courant Total en fonction du temps ')
plt.plot(temps, Current_P1)
plt.grid()

plt.subplot(1, 2, 2)
plt.xlabel('Temps (s)')
plt.ylabel('Courant P2 (mA)')
plt.title('courrant P2 en fonction de photo 2')
plt.plot(temps, Current_P2)
plt.grid()
plt.show()

Data.close()
