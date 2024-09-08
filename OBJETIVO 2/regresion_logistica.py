# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score, roc_curve, roc_auc_score
from sklearn.multiclass import OneVsRestClassifier
import pickle
pd.set_option('display.max_columns', None)
# Leer los datos desde un archivo CSV
data_path = "C:/Users/ACCER/Desktop/Cursos UNT-Ing. Sitemas/IX CICLO/ANALITICA DE NEGOCIO/PROYECTO/DATA/OBJ 2/data-obj2.csv"
obj2 = pd.read_csv(data_path)

# Agregar el nuevo campo "es_vulnerable"
obj2['vulnerable'] = np.where((obj2['edad'] <= 2) | (obj2['edad'] >= 65), 1, 0)

# Agregar el nuevo campo "alta_temperatura"
obj2['alta_temperatura'] = np.where((obj2['promedio_temperatura'] >= 39), 1, 0)

# Agregar el nuevo campo "enfermedad_cronica"
obj2['cronica_enfermedad'] = np.where((obj2['enfermedad_cronica'] != "NINGUNA"), 1, 0)


# Eliminar las columnas que no necesitamos
obj2.drop(['id','fecha_registro','genero','tratamiento_paralelo','edad', 'promedio_temperatura', 'enfermedad_cronica'], axis=1, inplace = True)

print(obj2.head(10))

# Filtrar los datos
obj2_final = obj2[obj2['sintomas_gripe'].notnull()]
print(obj2_final.head(10))

# Convertir variables categóricas a numéricas
categorical_columns = ['dificultad_respiratoria', 'sintomas_gripe', 'presencia_pus', 'historial_neumonia','historial_tabaquismo','vacunacion_neumonia','ubicacion_geografica','vulnerable', 'alta_temperatura','cronica_enfermedad']

encoder = OneHotEncoder()

encoder.fit(obj2_final[categorical_columns])

one_hot_encoded = encoder.transform(obj2_final[categorical_columns])
print(one_hot_encoded)

#El resultado del OneHotEncoder es una matriz dispersa, convertimos a DataFrame para visualizarlo
one_hot_df = pd.DataFrame(one_hot_encoded.toarray(), columns=encoder.get_feature_names_out(categorical_columns))
    
#Eliminamos las columnas originales que ya han sido codificadas
obj2_final = obj2_final.drop(columns=categorical_columns)

#Concatenar el DataFrame codificado con el DataFrame original
obj2_final_encoded = pd.concat([obj2_final, one_hot_df], axis=1)
    

# Dividir el conjunto de datos en entrenamiento y prueba
X = obj2_final_encoded.drop('resultado', axis=1)
y = obj2_final_encoded['resultado']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=23)
print(X.columns)
# Crear un modelo de regresión logística para clasificación
lr_modelo_clasificacion = LogisticRegression(max_iter=6000)

#PARA GRAFICAR EL MODELO DE REGRESION--------------

# Aplicar la estrategia "one-vs-all" al modelo
#ovr_model = OneVsRestClassifier(lr_modelo_clasificacion)

# Entrenar el modelo con los datos de entrenamiento
#ovr_model.fit(X_train, y_train)

# Realizar predicciones en el conjunto de datos de prueba
#prediccion = ovr_model.predict(X_test)

#------------------------------------------------------------

# Entrenar el modelo con los datos de entrenamiento
lr_modelo_clasificacion.fit(X_train, y_train)

# Realizar predicciones en el conjunto de datos de prueba
prediccion = lr_modelo_clasificacion.predict(X_test)
resultado = pd.DataFrame({'features': X_test.apply(tuple, axis=1), 'label': y_test, 'prediction': prediccion})
print(resultado.head(100))

# Calcular la precisión del modelo
precision = accuracy_score(y_test, prediccion)
print("Precisión del modelo:", precision)

# Guardar el modelo entrenado (si lo deseas)
ruta_guardado_modelo = 'C:/Users/ACCER/Desktop/Cursos UNT-Ing. Sitemas/IX CICLO/ANALITICA DE NEGOCIO/PROYECTO/MODELOS PREDICTIVOS/modelo_regresion_logistica.pkl'
with open(ruta_guardado_modelo, 'wb') as f:
    pickle.dump(lr_modelo_clasificacion, f)

def enviar_precision():
    return precision
    
def codificar_datos_nuevos(nuevos_datos):
     
    nuevos_datos_df = pd.DataFrame(nuevos_datos)
    print(nuevos_datos_df.columns)
    print("AQUI2")
    
    one_hot_encoded = encoder.transform(nuevos_datos_df[categorical_columns])

    print(one_hot_encoded)
    #El resultado del OneHotEncoder es una matriz dispersa, convertimos a DataFrame para visualizarlo
    one_hot_df = pd.DataFrame(one_hot_encoded.toarray(), columns=encoder.get_feature_names_out(categorical_columns))
    print(one_hot_df) 
    #Eliminamos las columnas originales que ya han sido codificadas
    nuevos_datos_df = nuevos_datos_df.drop(columns=categorical_columns)
    print(nuevos_datos_df) 
    #Concatenar el DataFrame codificado con el DataFrame original
    nuevos_datos_df_encoded = pd.concat([nuevos_datos_df, one_hot_df], axis=1)
    print(nuevos_datos_df_encoded) 
    
    return nuevos_datos_df_encoded


# Calcular las probabilidades de predicción para la curva ROC
#y_prob_ovr = ovr_model.predict_proba(X_test)

# Graficar la curva ROC para cada clase
#plt.figure(figsize=(10, 6))
#for i in range(len(ovr_model.classes_)):
#    y_true_class = (y_test == ovr_model.classes_[i]).astype(int)
#    y_prob_class = y_prob_ovr[:, i]
#    fpr, tpr, _ = roc_curve(y_true_class, y_prob_class)
#    roc_auc = roc_auc_score(y_true_class, y_prob_class)
#    plt.plot(fpr, tpr, label=f'Clase {ovr_model.classes_[i]} (AUC = {roc_auc:.2f})')

#plt.plot([0, 1], [0, 1], 'k--')
#plt.xlim([0.0, 1.0])
#plt.ylim([0.0, 1.05])
#plt.xlabel('Tasa de Falsos Positivos (FPR)')
#plt.ylabel('Tasa de Verdaderos Positivos (TPR)')
#plt.title('Curva ROC para el modelo de regresión logística')
#plt.legend(loc='lower right')
#plt.show()