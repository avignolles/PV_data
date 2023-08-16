# importation des modules
import os
import serial
import serial.tools.list_ports  # pour la communication avec le port série
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt  # pour le tracé de graphe
from matplotlib import animation  # pour la figure animée
import time  # gestion du temps
import pylab
from pylab import *


datafileNameBase = r"/Users/moustapha/Downloads/Python/"

OutputFileName = "/Users/moustapha/Downloads/Python/Donnees_concatenes.xlsx"


def Concatener(OutputFileName, list_datafiles):

    df = pd.DataFrame(columns=["V_ampoule_1", "V_ampoule_2", "V_moteur", "V_thermo_P1", "V_thermo_P2", "V_thermo_batterie", "V_photo_P1", "V_photo_P2", "BusVoltage_batterie", "ShuntVoltage_batterie",
                               "Current_batterie", "Power_batterie", "BusVoltage_P1", "ShuntVoltage_P1", "Current_P1", "Power_P1", "BusVoltage_P2", "ShuntVoltage_P2", "Current_P2", "Power_P2", "temps", "dataNumber"])

    excel = pd.ExcelFile(OutputFileName)

    frame = excel.parse(excel.sheet_names[0], index_col=None)
    print(frame)

    Header_OK = (frame.columns.values.tolist() == df.columns.values.tolist())
    if Header_OK:
        pass
    else:
        with pd.ExcelWriter(OutputFileName, mode="w", engine="openpyxl") as writer:
            df.to_excel(writer, index=False, header=True, startrow=0)

    for dataX in list_datafiles:

        datafileName = datafileNameBase + dataX
        dataName = datafileName.split("/")[-1]
        print(dataName)
        dataNumber = int(dataName.split("data")[-1].split(".txt")[0])
        print("dataNumber=", dataNumber)

        V_ampoule_1, V_ampoule_2, V_moteur, V_thermo_P1, V_thermo_P2, V_thermo_batterie, V_photo_P1, V_photo_P2, BusVoltage_batterie, ShuntVoltage_batterie, Current_batterie, Power_batterie, BusVoltage_P1, ShuntVoltage_P1, Current_P1, Power_P1, BusVoltage_P2, ShuntVoltage_P2, Current_P2, Power_P2, temps = np.loadtxt(
            str(datafileName), delimiter=';', unpack=True)

        df["V_ampoule_1"] = V_ampoule_1
        df["V_ampoule_2"] = V_ampoule_2
        df["V_moteur"] = V_moteur
        df["V_thermo_P1"] = V_thermo_P1
        df["V_thermo_P2"] = V_thermo_P2
        df["V_thermo_batterie"] = V_thermo_batterie
        df["V_photo_P1"] = V_photo_P1
        df["V_photo_P2"] = V_photo_P2
        df["BusVoltage_batterie"] = BusVoltage_batterie
        df["ShuntVoltage_batterie"] = ShuntVoltage_batterie
        df["Current_batterie"] = Current_batterie
        df["Power_batterie"] = Power_batterie
        df["BusVoltage_P1"] = BusVoltage_P1
        df["ShuntVoltage_P1"] = ShuntVoltage_P1
        df["Current_P1"] = Current_P1
        df["Power_P1"] = Power_P1
        df["BusVoltage_P2"] = BusVoltage_P2
        df["ShuntVoltage_P2"] = ShuntVoltage_P2
        df["Current_P2"] = Current_P2
        df["Power_P2"] = Power_P2
        df["temps"] = temps
        df["dataNumber"] = [dataNumber for t in temps]
        with pd.ExcelWriter(OutputFileName, mode="a", engine="openpyxl", if_sheet_exists='overlay') as writer:

            df.to_excel(writer, index=False, header=False,
                        startrow=writer.sheets['Sheet1'].max_row)


Concatener(OutputFileName, ['data46.txt'])

# Suite : Fonction pour supprimer les dataX du fichier Excel
