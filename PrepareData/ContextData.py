#region Importaciones

import pandas as pan

#endregion

#region Declaracion de Variables

def SetHeaders():

    try:

        columns = ["Motor", "ID",
                   "Alineacion Eje", "Demanda", "Temp Entrada", "Temp Devanados", "Temp Carcasa",
                   "Temp Rodamiento", "Presion Producto", "Presion Lubricante", "Voltaje L1", "Velocidad Campo",
                   "Velocida Campo", "Sobrecarga", "Vibracion", "Voltaje L2", "Velocidad Estimada", 
                   "Par", "Relacion Deslizamiento", "Desvalance Fases", "Flujo Masico", "Velocidad Consigna", "% Consigna Velocidad"
                   "Flujo Entrada Refrigerante", "Flujo Salida Refrigerante"]

        dataTable = pan.read_csv("Resources/train_FD001.txt", sep=r"\s+", header=None, names=columns)

        dataTable.to_csv("PrepareData/DataHeaders/DB_Motores.txt", sep= " ", index=False)

        print(dataTable)
        
    except Exception as xe:
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
