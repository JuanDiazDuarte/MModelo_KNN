from B_PrepareData import ContextData as conDat
from C_LimpiezaDatos import CleanData as clnDat

def StartProcess():

    try:

        print("Starting Process...")
        CreateHeaders()
        CleanData()

    except Exception as ex:
        print(f"Exception in : {ex}")


def CreateHeaders():
    print("Set Headers in Database starting...")
    conDat.SetHeaders()

def CleanData():
    print("Fix Data Process starting...")
    clnDat.DataDiagnostics()
    clnDat.CleanDB()
