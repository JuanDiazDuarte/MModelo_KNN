
#region Importaciones

#region Importaciones Funcionales

import pandas as pan
import numpy as nup

#endregion

#region Importaciones de Proyecto

from Modelos import Model as mod

#endregion

#endregion

def DataDiagnostics():

    try:

        print("Starting Data Diagnostics...")

        onlyData = mod.FULL_DATA_DB.drop(columns=["Motor", "Ciclo", "RUL"])

        #region Analisis de Valores Nulos
        
        print("\nData null analisis...")
        dataNulls = onlyData.isnull().sum()

        print(dataNulls)  
        
        #endregion   

        #region Analisis de Datos Duplicados

        print("\nData Duplicates...")
        dataDuplicates = onlyData.duplicated().sum()

        print(dataDuplicates)

        #endregion

        #region Analisis de Dispersion de Datos

        print("\nData Dispertion...")

        desStandar = onlyData.std(axis=0)
        dataNZero = desStandar[desStandar < 0.001].index.tolist()

        print(dataNZero)
        
        #endregion

    except Exception as ex:
        print(f"Exception in: {ex}")

def CleanDB():

    try:

        print(f"Starting CleanDB...")

        mod.RUL_COLUM = mod.FULL_DATA_DB["RUL"]
        mod.DATA_DB = mod.FULL_DATA_DB.drop(Columns=["Motor", "Ciclo", "RUL"])


    except Exception as ex:
        print(f"Exception in CleanDB: {ex}")
