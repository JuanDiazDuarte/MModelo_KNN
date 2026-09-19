
from Modelos import Model as mod
from sklearn.neighbors import KNeighborsRegressor

def RunKnnModel():

    try:

        knnModel = KNeighborsRegressor(n_neighbors=10)

        knnModel.fit(mod.DATA_TRAIN, mod.Y_DATA_TRAIN)

        prediccionRul = knnModel.predict(mod.DATA_TEST)

        print(f"Prediccion KNN de RUL (DATA_TEST): [{prediccionRul[:5]}]")
        print(f"Valor real de RUL: [{mod.Y_DATA_TEST.iloc[:5].values}]")

    except Exception as ex:
        print(f"Exception in RunKnnModel: {ex}")