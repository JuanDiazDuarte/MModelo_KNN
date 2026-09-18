
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

        print("\nData Dispertion Variance...")

        desStandar = onlyData.std(axis=0)
        dataNZero = desStandar[desStandar < 0.001].index.tolist()

        print(dataNZero)
        
        #endregion

    except Exception as ex:
        print(f"Exception in: {ex}")

def CleanDB():

    try:

        print("\nStarting CleanDB...\n")

        dbToClean = mod.FULL_DATA_DB.copy()
        
        #region 1.- Datos Duplicados

        """
        2026-09-17 Segun el analisis realizado previamente no se encontraron registros duplicados,
        por lo que no se aplicara limpieza por duplicidad.

        En caso de ser requerida el comando es el siguiente:

        dbToClean = dbToClean.drop_duplicates()

        """

        #endregion

        #region 2.- Definicion del objetivo Analitico

        mod.Y_COLUMN = mod.FULL_DATA_DB["RUL"]
        mod.X_DATA = mod.FULL_DATA_DB.drop(columns=["Motor", "Ciclo", "RUL"])

        #endregion

        #region 3.- Tratamiento de Valores Nullos

        if mod.X_DATA.isnull().sum().sum() >0:

            """
            Del analisis de datos anterior se determina que no existen datos null
            en esta base de datos, por lo que esta sentencia IF no se ejecutara,
            en caso de requerirse en futuros proyectos se debe evaluar que metodo
            usar para el tratamiento de null, en este ejemplo se determina
            la mediana de la columna, puede ser el valor inmediato anterior, 
            la media, etc
            """
            
            X=X.fillna(X.median())
            
            print(f"Total de valores NULL: {mod.X_DATA.isnull().sum().sum()}")
            
        else:

            """
            No se aplicara correccion por valores NULL
            """

            print("Sin valores NULL")
            
        #endregion

        #region 4.- Eliminar Variables con Varianza Cercana a 0

        

        #endregion

        #region 5.- Normalizar Variables

        #endregion


    except Exception as ex:
        print(f"Exception in CleanDB: {ex}")
