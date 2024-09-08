from sklearn import tree
import pandas as pd
import pickle
import glob
from sklearn.metrics import accuracy_score


#creamos arbol decision
arbol = tree.DecisionTreeClassifier()
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



#variables predictoras['glucosa','colesterol malo','trigliceridos']
#X = data[['glucemia_mgdL','anticuerpos_betaPancreas']].astype(float).values
X = datos_completos.drop('diagnostico', axis=1).astype(float).values


#salida de data
Y = datos_completos['diagnostico']

#ENTRENA
arbol= arbol.fit(X,Y)

# Guardar el modelo en un archivo .pkl
with open('modelo_arbol.pkl', 'wb') as archivo:
    pickle.dump(arbol, archivo)

# Cargar el modelo desde el archivo .pkl
with open('modelo_arbol.pkl', 'rb') as archivo:
    modelo_cargado = pickle.load(archivo)


# Realizar predicciones con el modelo cargado
prediccion = modelo_cargado.predict([[140,120,80,10,27,4,1,0,0,1,0,17]])
print(prediccion)  # Salida: [0]



# Obtener las predicciones del modelo en los datos de prueba
y_pred = modelo_cargado.predict(X)

# Calcular la precisión del modelo
accuracy = accuracy_score(Y, y_pred)

print("Precisión del modelo de árbol de decisiones: {:.2f}".format(accuracy))
