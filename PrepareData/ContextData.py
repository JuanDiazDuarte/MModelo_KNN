#region Importaciones

import pandas as pan

#endregion

#region Declaracion de Variables

def SetHeaders():

    try:

        columns = ["Motor", "ID",
                   "Alineacion Acoplamiento", "% Demanda", "Voltaje L1", "Revoluciones a 125%", "Revoluciones a 75%",
                   "Revoluciones a 100%", "Temp a 0%", "Temp 25%", "Voltaje L2", "Revoluciones a 50%",
                   "Revoluciones 150 %", "Presion Lubricante", "Temperatura 100%", "Voltaje L3", "Revoluciones 25%", "Revoluciones 0%", 
                   "Vibracion", "Alineacion Eje ", "Flujo de Lubricante", "Flujo de Producto", "% de Torque",
                   "Temperatura 75%", "Temperatura 50%"]

        dataTable = pan.read_csv("Resources/train_FD001.txt", sep=r"\s+", header=None, names=columns)

        dataTable.to_csv("PrepareData/DataHeaders/DB_Motores.txt", sep= " ", index=False)

        print(dataTable)
        
    except Exception as ex:
        print(f"Exception in SetHeaders: {ex}")

def InitialAnalisis():
    
    try:

        sensores = [f"para({i})" for i in range(1,24)]
        columns = ["Motor", "ID",] + sensores

        dataTable = pan.read_csv("Resources/train_FD001.txt", sep=r"\s+", header=None, names=columns)

        for sensor in sensores:
            promedio = round(dataTable[sensor].mean(), 6)
            print(f"{sensor}: {promedio}")

    except Exception as xe:
        print(f"Exception in SetHeaders: {ex}")

#endregion
