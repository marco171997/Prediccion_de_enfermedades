import joblib
from sklearn import tree
import pandas as pd
import pickle
import glob
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OneHotEncoder

def cargar_modelo(ruta_modelo):
    """
    Carga el modelo de árbol de decisiones desde el archivo .pkl.

    :param ruta_modelo: La ruta al archivo .pkl que contiene el modelo.
    :return: El modelo cargado.
    """
    return joblib.load(ruta_modelo)


def hacer_prediccion_obj2(modelo,nuevos_datos_df_encoded):
    """
    Realiza una predicción utilizando el modelo cargado.

    :param modelo: El modelo de regresion lineal cargado.
    :return: La predicción realizada por el modelo.
    """
    
    prediccion = modelo.predict(nuevos_datos_df_encoded)

    
    return prediccion[0]

