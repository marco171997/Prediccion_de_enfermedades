from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn import tree
import pandas as pd
import glob

#datos
# Obtener una lista de nombres de archivos CSV en la carpeta 'D:/carpeta_datos/'
ruta_archivos = 'D:/'
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

print("Precisión del modelo de árbol de decisiones:", precision)
