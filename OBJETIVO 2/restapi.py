from flask import Flask, jsonify, request
from flask_cors import CORS

from functions import *
from regresion_logistica import codificar_datos_nuevos,enviar_precision


app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas
CORS(app, origins='http://127.0.0.1:8000')


@app.route('/predecirobj2', methods=['POST'])
def get_prediccion_obj2():
    try:
        # Recibo la data request
        data = request.get_json()
        
        precision = 0
        
        # Extraer data
        dificultad_respiratoria = data.get('dificultad_respiratoria')
        sintomas_gripe = data.get('sintomas_gripe')
        presencia_pus = data.get('presencia_pus')
        historial_neumonia = data.get('historial_neumonia')
        historial_tabaquismo = data.get('historial_tabaquismo')
        vacunacion_neumonia = data.get('vacunacion_neumonia')
        ubicacion_geografica = data.get('ubicacion_geografica')
        vulnerable = data.get('vulnerable')
        alta_temperatura = data.get('alta_temperatura')
        cronica_enfermedad = data.get('cronica_enfermedad')
        
        
        nuevos_datos = {'dificultad_respiratoria': [dificultad_respiratoria], 
                'sintomas_gripe': [sintomas_gripe], 
                'presencia_pus': [presencia_pus], 
                'historial_neumonia': [historial_neumonia],
                'historial_tabaquismo': [historial_tabaquismo],
                'vacunacion_neumonia': [vacunacion_neumonia],
                'ubicacion_geografica': [ubicacion_geografica],
                'vulnerable': [vulnerable], 
                'alta_temperatura': [alta_temperatura],
                'cronica_enfermedad': [cronica_enfermedad]}
        
        nuevos_datos_df_encoded = codificar_datos_nuevos(nuevos_datos)
        
        # Ruta al archivo .pkl que contiene el modelo entrenado
        ruta_modelo = r'C:/Users/ACCER/Desktop/Cursos UNT-Ing. Sitemas/IX CICLO/ANALITICA DE NEGOCIO/PROYECTO/MODELOS PREDICTIVOS/modelo_regresion_logistica.pkl'

        # Cargar el modelo desde el archivo .pkl
        modelo = cargar_modelo(ruta_modelo)

        # Ejemplo de predicción con nuevos datos
        resultado_prediccion = hacer_prediccion_obj2(modelo,nuevos_datos_df_encoded)
        
        # Precision del modelo
        precision = enviar_precision()
        
        # Imprimir el resultado de la predicción
        return jsonify(resultado_prediccion,precision)

    except Exception as e:
        # Manejo de la excepción
        return jsonify({'error': str(e)})


@app.route('/testPost', methods=['POST'])
def recibir_datos():
    try:
        data = request.get_json()  # Obtener los datos enviados en formato JSON
        # Procesar los datos como lo desees
        # Por ejemplo, si los datos son un objeto JSON con un campo "nombre":
        nombre = data.get('nombre')
        return jsonify({'mensaje': f'Hola, {nombre}! Datos recibidos correctamente.'})
    except Exception as e:
        return jsonify({'error': f'Error al procesar los datos: {str(e)}'}, 500)


if __name__ == '__main__':
    app.run(debug=True, port=4000)
