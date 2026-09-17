from B_PrepareData import ContextData as conDat

def StartProcess():

    try:

        print("Starting Process...")
        CreateHeaders()

    except Exception as ex:
        print(f"Exception in : {ex}")


def CreateHeaders():
    print("Set Headers in Database starting...")
    conDat.SetHeaders()

def CleanData():
    print("Fix Data Process starting...")
