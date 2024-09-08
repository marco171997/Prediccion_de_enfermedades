import glob
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

# Configurar el ambiente de Spark
spark = SparkSession.builder.appName("ModeloArbolDecision").getOrCreate()

# Leer y concatenar los archivos CSV
ruta_archivos = 'D:/'
archivos_csv = glob.glob(ruta_archivos + '*.csv')

lista_dataframes = []
for archivo_csv in archivos_csv:
    datos = spark.read.csv(archivo_csv, sep=';', header=True,
                           inferSchema=True)
    lista_dataframes.append(datos)

# Concatenar todos los DataFrames en uno solo
datos_completos = lista_dataframes[0]
for i in range(1, len(lista_dataframes)):
    datos_completos = datos_completos.union(lista_dataframes[i])

# Crear un VectorAssembler para combinar las características en una sola columna "features"
assembler = VectorAssembler(inputCols=[col for col in datos_completos.columns if col != "diagnostico"],
                            outputCol="features")

# Transformar los datos para incluir la columna "features"
datos_transformados = assembler.transform(datos_completos)

# Dividir los datos en conjuntos de entrenamiento y prueba (por ejemplo, 80% para entrenamiento, 20% para prueba)
X_train, X_test = datos_transformados.randomSplit([0.8, 0.2], seed=42)

# Crear el modelo de árbol de decisiones
modelo_arbol = DecisionTreeClassifier()

# Entrenar el modelo con los datos de entrenamiento
modelo_entrenado = modelo_arbol.fit(X_train)

# Obtener las predicciones del modelo en los datos de prueba
resultados = modelo_entrenado.transform(X_test)

# Calcular la precisión del modelo en los datos de prueba
evaluador = MulticlassClassificationEvaluator(labelCol="diagnostico", predictionCol="prediction", metricName="accuracy")
precision = evaluador.evaluate(resultados)

print("Precisión del modelo de árbol de decisiones:", precision)
