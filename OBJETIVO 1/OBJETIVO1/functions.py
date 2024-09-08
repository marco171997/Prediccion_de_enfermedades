import joblib
from sklearn import tree
import pandas as pd
import glob
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
import os


def cargar_modelo(ruta_modelo):
    """
    Carga el modelo de árbol de decisiones desde el archivo .pkl.

    :param ruta_modelo: La ruta al archivo .pkl que contiene el modelo.
    :return: El modelo cargado.
    """
    return joblib.load(ruta_modelo)


def hacer_prediccion(modelo, glucemia, sistolica, diastolica, insulina, imc, cetonas, polidipsia, poliuria, polifagia, beta, antecedentes, edad):
    """
    Realiza una predicción utilizando el modelo cargado.

    :param modelo: El modelo de árbol de decisiones cargado.
    :param glucemia_mgdL: Valor de glucemia en mg/dL.
    :param anticuerpos_betaPancreas: Valor de anticuerpos beta del páncreas.
    :return: La predicción realizada por el modelo.
    """
    prediccion = modelo.predict([[glucemia, sistolica, diastolica, insulina, imc, cetonas, polidipsia, poliuria, polifagia, beta, antecedentes, edad]])
    return prediccion[0]


def presicion_simple():
    # Obtener una lista de nombres de archivos CSV en la carpeta 'D:/carpeta_datos/'
    ruta_archivos = 'C:/Objetivos/obj1diabetes/data/'
    archivos_csv = glob.glob(ruta_archivos + '*.csv')

    # Leer y concatenar los archivos CSV
    lista_dataframes = []
    for archivo_csv in archivos_csv:
        datos = pd.read_csv(archivo_csv, delimiter=';', skiprows=1,
                            names=['glucemia_mgdL', 'presionArterialSistolica_mmHg',
                                   'presionArterialDiastolica_mmHg',
                                   'nivelInsulina_uUmL', 'indiceMasaCorporal_kgm2',
                                   'nivelCetonasUrina_mgdL', 'polidipsia',
                                   'poliuria', 'polifagia',
                                   'anticuerpos_betaPancreas',
                                   'antecedentesFamiliares', 'edad',
                                   'diagnostico'])
        lista_dataframes.append(datos)

    # Concatenar todos los DataFrames en uno solo
    datos_completos = pd.concat(lista_dataframes, ignore_index=True)

    # X contiene todas las características excepto 'diagnostico'
    X = datos_completos.drop('diagnostico', axis=1).astype(float).values

    # Y contiene solo las etiquetas 'diagnostico'
    Y = datos_completos['diagnostico']

    # Dividir los datos en conjuntos de entrenamiento y prueba (por ejemplo, 80% para entrenamiento, 20% para prueba)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

    # Crear el modelo de árbol de decisiones
    modelo_arbol = tree.DecisionTreeClassifier()

    # Entrenar el modelo con los datos de entrenamiento
    modelo_arbol.fit(X_train, Y_train)

    # Obtener las predicciones del modelo en los datos de prueba
    y_pred = modelo_arbol.predict(X_test)

    # Calcular la precisión del modelo en los datos de prueba
    precision = accuracy_score(Y_test, y_pred)
    return precision


def hacer_prediccion3(modelo, edad, genero, temperatura, plaquetas, vcm, eosinofilos, dolormuscular, vomitos):
    # Crea un nuevo DataFrame con datos para probar el modelo
    # Recuerda que los datos deben estar en el mismo formato que los datos de entrenamiento
    data = pd.DataFrame({
        'Edad': [edad],
        'Genero': [genero],
        'Temperatura': [temperatura],
        'Plaquetas': [plaquetas],
        'Volumen corpuscular medio': [vcm],
        'Eosinofilos': [eosinofilos],
        'Dolor muscular': [dolormuscular],
        'Vomitos': [vomitos]
    })

    # Usa el modelo cargado para hacer predicciones
    prediccion = modelo.predict(data)

    return prediccion[0]


def presicion_simple3():
    # Lee todos los archivos .csv en el directorio dado
    path = r'C:\RandomForest\data'  # Usa tu propio path
    all_files = glob.glob(os.path.join(path, "*.csv"))

    # Crea un DataFrame vacío para almacenar los datos
    data = pd.DataFrame()

    # Lee y concatena todos los archivos .csv
    for file in all_files:
        df = pd.read_csv(file)
        data = pd.concat([data, df], ignore_index=True)

    # Separa las características (X) de la etiqueta objetivo (y)
    X = data.drop('Dengue', axis=1)
    y = data['Dengue']

    # Divide los datos en conjuntos de entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crea el modelo de bosques aleatorios
    model = RandomForestClassifier(n_estimators=100, random_state=42)

    # Entrena el modelo
    model.fit(X_train, y_train)

    # Haz predicciones en el conjunto de prueba
    predictions = model.predict(X_test)

    # Calcula la precisión del modelo
    accuracy = accuracy_score(y_test, predictions)

    return accuracy

    

       
       






