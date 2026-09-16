from PrepareData import ContextData as conDat

def StartProcess():

    try:

        print("Starting Process...")
        CreateHeaders()

    except NameError as ne:
        print("Exception in :" + ne)


def CreateHeaders():
    print("Set Headers in Database starting...")
    conDat.SetHeaders()

def CleanData():
    print("Fix Data Process starting...")