import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
import numpy as np

def IAMain(email):

    model = Sequential([Dense(units=4, input_shape=(4,), activation='sigmoid'),  # Camada de entrada
                        Dense(units=1, activation='sigmoid')])  # Camada de saída

    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

    def ExtrairProp(email):
        palavra_gratis = 1 if "gratis" in email.lower() else 0
        palavra_oferta = 1 if "oferta" in email.lower() else 0
        palavra_desconto = 1 if "desconto" in email.lower() else 0
        number_links = email.lower().count("http")
        return np.array([[palavra_gratis, palavra_oferta, palavra_desconto, number_links]])

    dados_treinoX = np.array([[0, 0, 1, 3],
                            [0, 1, 1, 0],
                            [1, 0, 1, 1],
                            [1, 1, 0, 2],
                            [1, 0, 1, 4],
                            [0, 0, 1, 3],
                            [1, 0, 0, 1],
                            [0, 0, 0, 0],
                            [0, 0, 0, 4]])
    dados_treinoY = np.array([0, 1, 0, 1, 1, 1, 1, 0, 1])

    model.fit(dados_treinoX, dados_treinoY, epochs=80)

    previsao = model.predict(ExtrairProp(email))

    
    if float(previsao[0]) > 0.5:
        previsao = 1
    elif float(previsao[0]) < 0.5:
        previsao = 0

    print(previsao)
