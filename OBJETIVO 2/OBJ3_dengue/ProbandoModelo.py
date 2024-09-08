import pandas as pd
import numpy as np
import pickle

# Carga el modelo desde un archivo .pkl
with open('random_forest_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

# Crea un nuevo DataFrame con datos para probar el modelo
# Recuerda que los datos deben estar en el mismo formato que los datos de entrenamiento
data = pd.DataFrame({
    'Edad': [30],
    'Genero': [1],
    'Temperatura': [39.5],
    'Plaquetas': [125.1],
    'Volumen corpuscular medio': [80.1],
    'Eosinofilos': [0.01],
    'Dolor muscular': [1],
    'Vomitos': [1]
})

# Usa el modelo cargado para hacer predicciones
predictions = loaded_model.predict(data)

print(f'Predicción del modelo para los datos de prueba: {predictions[0]}')
