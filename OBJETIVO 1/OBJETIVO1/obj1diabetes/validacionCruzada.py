import numpy as np
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree
import glob
import matplotlib.pyplot as plt

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



# Supongamos que tienes tus datos en un DataFrame llamado 'datos'
X = datos_completos.drop('diagnostico', axis=1)  # Características
y = datos_completos['diagnostico']  # Etiquetas

# Define tu modelo de aprendizaje automático, por ejemplo, un árbol de decisión
modelo = DecisionTreeClassifier(max_depth=5)

# Define el número de folds (k) para la validación cruzada
k = 5  # Puedes ajustar este valor según tus necesidades

# Realiza k-fold cross-validation
kf = KFold(n_splits=k, shuffle=True, random_state=42)  # Aquí usamos el shuffle para mezclar los datos antes de dividirlos
resultados = cross_val_score(modelo, X, y, cv=kf, scoring='accuracy')  # 'accuracy' es la métrica de evaluación que queremos usar

# Muestra los resultados
print("Resultados de cada fold:", resultados)
print("Precisión promedio:", np.mean(resultados))


# Entrenar el modelo en todos los datos
modelo.fit(X, y)

# Dibujar el árbol de decisiones
plt.figure(figsize=(15, 10))
plot_tree(modelo, filled=True, feature_names=X.columns.tolist(),
          class_names=y.unique().tolist())
plt.tight_layout()  # Ajustar el diseño del gráfico para evitar superposiciones
plt.show()
