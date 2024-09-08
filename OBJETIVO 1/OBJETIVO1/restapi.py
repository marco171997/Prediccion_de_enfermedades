from flask import Flask, jsonify, request
from flask_cors import CORS



from functions import *


app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas
#CORS(app, origins='http://127.0.0.1:8000')

@app.route('/predecir3', methods=['POST'])
def get_prediccion3():

    try:
        # Recibo la data request
        data = request.get_json()

        # Extraer data
        edad = data.get('edad')
        genero = data.get('genero')
        temperatura = data.get('temperatura')
        plaquetas = data.get('plaquetas')
        vcm = data.get('vcm')
        eosinofilos = data.get('eosinofilos')
        dolormuscular = data.get('dolormuscular')
        vomitos = data.get('vomitos')

        # Ruta al archivo .pkl que contiene el modelo entrenado
        ruta_modelo = 'C:/Objetivos/obj2-dengue/random_forest_model.pkl'

        # Cargar el modelo desde el archivo .pkl
        modelo = cargar_modelo(ruta_modelo)

        # Ejemplo de predicción con nuevos datos
        resultado_prediccion = hacer_prediccion3(modelo, edad, genero,
                                                temperatura, plaquetas, vcm, eosinofilos,
                                                dolormuscular, vomitos)
        # Convertir int64 a int estándar
        resultado_prediccion = int(resultado_prediccion)

        # Calcular la precisión del modelo
        presicion = presicion_simple3()

        # Combinar el resultado de la predicción y la precisión en un diccionario
        respuesta = {
            'resultado_prediccion': resultado_prediccion,
            'precision': presicion
        }

        # Enviar la respuesta JSON con el resultado de la predicción y la precisión
        return jsonify(respuesta)

    except Exception as e:
        # Manejo de la excepción
        return jsonify({'error': str(e)})



    
@app.route('/predecir', methods=['POST'])
def get_prediccion():
    try:
        # Recibo la data request
        data = request.get_json()

        # Extraer data
        glucemia = data.get('glucemia')
        sistolica = data.get('sistolica')
        diastolica = data.get('diastolica')
        insulina = data.get('insulina')
        imc = data.get('imc')
        cetonas = data.get('cetonas')
        edad = data.get('edad')
        polidipsia = data.get('polidipsia')
        poliuria = data.get('poliuria')
        polifagia = data.get('polifagia')
        beta = data.get('beta')
        antecedentes = data.get('antecedentes')

        # Ruta al archivo .pkl que contiene el modelo entrenado
        ruta_modelo = 'C:/Objetivos/obj1diabetes/modelo_arbol.pkl'

        # Cargar el modelo desde el archivo .pkl
        modelo = cargar_modelo(ruta_modelo)

        # Ejemplo de predicción con nuevos datos
        # nueva_glucemia = 80
        # nuevos_anticuerpos = 1
        resultado_prediccion = hacer_prediccion(modelo, glucemia, sistolica,
                                                diastolica, insulina, imc, cetonas,
                                                polidipsia, poliuria, polifagia,
                                                beta, antecedentes, edad)
        # Calcular la precisión del modelo
        presicion = presicion_simple()

        # Combinar el resultado de la predicción y la precisión en un diccionario
        respuesta = {
            'resultado_prediccion': resultado_prediccion,
            'precision': presicion
        }

        # Enviar la respuesta JSON con el resultado de la predicción y la precisión
        return jsonify(respuesta)

    except Exception as e:
        # Manejo de la excepción
        return jsonify({'error': str(e)})





if __name__ == '__main__':
    app.run(debug=True, port=4000)

