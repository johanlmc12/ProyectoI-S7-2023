# views.py
import os
from django.db import connection
from django.shortcuts import render
from keras.preprocessing.text import tokenizer_from_json
import tensorflow as tf
from keras.utils import pad_sequences
from pqrs.forms import NewPhrasesForm
import numpy as np


def menu_principal(request):
    #results = request.session.get('results', [])
    return render(request, 'pqrs/menu.html') #{'results':results})


def solicitudes(request):
    return render(request, 'pqrs/solicitudes.html')


def editor(request):
    return render(request, 'pqrs/editor.html')


def guardar_BD(phrase, prediccion):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO tabla_modelo (frase, prediccion) VALUES (%s, %s)", [phrase, prediccion])


def classify_polarity(request):
    # Obtener la ruta absoluta del archivo views.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    if request.method == 'POST':
        form = request.POST.get('descripcion', '')  # Obtener la descripción ingresada desde el formulario
        new_phrase = form  # La frase ingresada se encuentra en 'form'

        # Cargar la arquitectura del modelo
        with open(os.path.join(current_dir, 'modelo_arquitectura.json'), 'r') as json_file:
            loaded_model_json = json_file.read()
        loaded_model = tf.keras.models.model_from_json(loaded_model_json)
        # Cargar los pesos del modelo
        loaded_model.load_weights(os.path.join(current_dir, 'modelo_pesos.h5'))
        # Cargar el tokenizador
        with open(os.path.join(current_dir, 'tokenizer.json'), 'r') as json_file:
            tokenizer_json = json_file.read()
        tokenizer = tokenizer_from_json(tokenizer_json)
        # Preprocesar la nueva frase
        max_length = 100
        padding_type = 'post'
        new_sequence = tokenizer.texts_to_sequences([new_phrase])
        new_padded = pad_sequences(new_sequence, padding=padding_type, maxlen=max_length)
        # Realizar la predicción para la nueva frase
        prediction = loaded_model.predict(new_padded)

        # Determinar si el resultado es "satisfecho" o "insatisfecho"
        if prediction[0] >= 0.75:
            opinion_final = "Muy Satisfecho"
        elif prediction[0] >= 0.50:
            opinion_final = "Satisfecho"
        elif prediction[0] >= 0.25:
            opinion_final = "Neutral"
        else:
            opinion_final = "Insatisfecho"

        # Obtener las frases y predicciones anteriores almacenadas en la sesión
        previous_results = request.session.get('results', [])
        # Agregar la nueva frase y predicción a la lista de resultados anteriores
        previous_results.append({'frase': new_phrase, 'prediccion': np.float64(prediction[0])})
        # Actualizar los resultados en la sesión
        request.session['results'] = previous_results
        #bases de datos
        guardar_BD(new_phrase, np.float64(prediction[0]))
        # Renderizar el resultado en un template
       #return render(request, 'pqrs/menu.html', {'results': previous_results, 'opinion': {'frase': new_phrase, 'prediccion': np.float64(prediction[0])}, 'opinion_final': opinion_final })
        return render(request, 'pqrs/menu.html', {'opinion_final': opinion_final})

    else:
        form = NewPhrasesForm()
        request.session.pop('results', None)
    return render(request, 'pqrs/menu.html', {'form': form})

