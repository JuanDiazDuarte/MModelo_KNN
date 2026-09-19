#region Importaciones

import pandas as pan
from Modelos import Model as mod

#endregion

#region Acondicionar Base de Datos

def SetHeaders():

    try:

        """
        Variable a Predecie es la Temperatura Devanados
        
        """
        columns = ["Motor", "Ciclo", 
                   "Alineacion Tuberias", "Alineacion Acoplamiento", "% Demanda", "Voltaje Linea 1", "Horas de Operacion", "Presion Succion",
                   "Presion Descarga", "Temperatura Acoplamiento", "Temperatura Carcaza", "Voltaje Linea 2", "Revoluciones Acoplamiento",
                   "Flujo de Producto en Succion", "Presion Lubricante", "Temperatura Devanados", "Voltaje Linea 3", "Revoluciones Eje",
                   "Flujo de Producto en Descarga", "Vibracion", "Alineacion Eje", "Flujo de Aire de Enfriamiento", "Set Point Revolucion",
                    "% de Torque", "Flujo de Entrada de Refrigerante", "Flujo de Salida de Refrigerante"]

        mod.FULL_DATA_DB = pan.read_csv("Resources/train_FD001.txt", sep=r"\s+", header=None, names=columns, skipinitialspace = True)
        GetRUL()

        #print(mod.FULL_DATA_DB[["Motor", "Ciclo", "RUL"]])
        
    except Exception as ex:
        print(f"Exception in SetHeaders: {ex}")

def GetRUL():

    try:

        max_cycles = mod.FULL_DATA_DB.groupby("Motor")["Ciclo"].transform("max")
        mod.FULL_DATA_DB["RUL"] = max_cycles - mod.FULL_DATA_DB["Ciclo"]

    except Exception as ex:
        print(f"Exception in GetRUL: {ex}")

#endregion

#region Analisis

def InitialAnalisis():
    
    try:

        sensores = [f"para({i+2})" for i in range(1,25)]
        columns = ["Motor", "ID",] + sensores

        dataTable = pan.read_csv("Resources/train_FD001.txt", sep=r"\s+", header=None, names=columns)

        for sensor in sensores:
            promedio = round(dataTable[sensor].mean(), 6)
            print(f"{sensor}: {promedio}")

    except Exception as ex:
        print(f"Exception in SetHeaders: {ex}")

#endregion
