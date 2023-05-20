# views.py
import os

from django.shortcuts import render
from keras.preprocessing.text import tokenizer_from_json
import tensorflow as tf
from keras.utils import pad_sequences
from pqrs.forms import NewPhrasesForm



def menu_principal(request):
    return render(request, 'pqrs/menu.html')


def solicitudes(request):
    return render(request, 'pqrs/solicitudes.html')


def editor(request):
    return render(request, 'pqrs/editor.html')

import numpy as np

def classify_polarity(request):
    # Obtener la ruta absoluta del archivo views.py
    current_dir = os.path.dirname(os.path.abspath(__file__))

    if request.method == 'POST':
        form = NewPhrasesForm(request.POST)
        if form.is_valid():
            new_phrase = form.cleaned_data['phrases']  # Obtener la frase ingresada

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

            # Obtener las frases y predicciones anteriores almacenadas en la sesión
            previous_results = request.session.get('results', [])
            # Agregar la nueva frase y predicción a la lista de resultados anteriores
            previous_results.append({'frase': new_phrase, 'prediccion': np.float64(prediction[0][0])})
            # Actualizar los resultados en la sesión
            request.session['results'] = previous_results

            # Renderizar el resultado en un template
            return render(request, 'tensorflow/classify_polarity.html', {'results': previous_results})
    else:
        form = NewPhrasesForm()

    return render(request, 'tensorflow/classify_polarity.html', {'form': form})


