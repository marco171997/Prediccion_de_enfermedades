import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
import os
import glob
import pickle

# Lee todos los archivos .csv en el directorio dado
path = r'C:\RandomForest\data' # Usa tu propio path
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

print(f'La precisión del modelo de bosques aleatorios es: {accuracy}')

# Guarda el modelo en un archivo .pkl
with open('random_forest_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Modelo guardado en random_forest_model.pkl")

