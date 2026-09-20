
from Modelos import Model as mod
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

def RunKnnModel():

    try:

        knnModel = KNeighborsRegressor(n_neighbors=10000)

        knnModel.fit(mod.DATA_TRAIN, mod.Y_DATA_TRAIN)

        prediccionRul = knnModel.predict(mod.DATA_TEST)

        print(f"Prediccion KNN de RUL (DATA_TEST): [{prediccionRul[:10]}]")
        print(f"Valor real de RUL: [{mod.Y_DATA_TEST.iloc[:10].values}]")


        # ==========================
        # EVALUAR EL MODELO
        # ==========================

        for k in range(1, 21):

            modelo = KNeighborsRegressor(n_neighbors=k)

            modelo.fit(mod.DATA_TRAIN, mod.Y_DATA_TRAIN)

            prediccion = modelo.predict(mod.DATA_TEST)

            rmse = np.sqrt(
                mean_squared_error(mod.Y_DATA_TEST, prediccion)
            )

            r2 = r2_score(
                mod.Y_DATA_TEST,
                prediccion
            )
            
            print(f"K={k:2d} | RMSE={rmse:.2f} | R²={r2:.4f}")

    except Exception as ex:
        print(f"Exception in RunKnnModel: {ex}")