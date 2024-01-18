# Detecção de Spam de E-mails usando IA Simples e Automação Web

Este projeto combina técnicas de aprendizado de máquina, especificamente uma rede neural simples usando TensorFlow e Keras, com automação web usando o Selenium para criar uma solução simples de detecção de spam de e-mails. A "IA" é treinada para reconhecer padrões com base em palavras-chave e links nos e-mails, enquanto o Bot interage com o navegador.

## Sobre o Aprendizado de Máquina (Machine Learning)

O script `main.py` contém o modelo de aprendizado de máquina. A rede neural escolhida é uma rede densa com ativação sigmoide. As características de entrada incluem palavras-chave como "gratis", "oferta", "desconto" e a contagem de links. Essas características são extraídas dos e-mails para treinar o modelo.

```python 
      import tensorflow as tf
      from tensorflow.keras.layers import Dense
      from tensorflow.keras import Sequential
      import numpy as np
      
      def IAMain(email):
          # Definindo o modelo
          model = Sequential([
              Dense(units=4, input_shape=(4,), activation='sigmoid'),  # Camada de entrada
              Dense(units=1, activation='sigmoid')  # Camada de saída
          ])
```


 # Compilando o modelo
    model.compile(optimizer='sgd', loss='binary_crossentropy', metrics=['accuracy'])

# Função para extrair características
    
    
   ```python
    
        def ExtrairProp(email):
            palavra_gratis = 1 if "gratis" in email.lower() else 0
            palavra_oferta = 1 if "oferta" in email.lower() else 0
            palavra_desconto = 1 if "desconto" in email.lower() else 0
            number_links = email.lower().count("http")
            return np.array([[palavra_gratis, palavra_oferta, palavra_desconto, number_links]])
    
        # Dados de treino
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
   ```

 # Treinando o modelo
    model.fit(dados_treinoX, dados_treinoY, epochs=80)

 # Fazendo previsão
    previsao = model.predict(ExtrairProp(email))

 # Classificando a previsão
    if float(previsao[0]) > 0.5:
        resultado_final = 1
    elif float(previsao[0]) < 0.5:
        resultado_final = 0

    return resultado_final
O modelo é treinado com dados de treino que incluem características extraídas de e-mails marcados como spam ou não.

# Automação Web com Selenium
O script main.py utiliza o Selenium para interagir com a interface web do Gmail. Ele faz login, navega na caixa de entrada e utiliza a IA treinada para classificar e-mails como spam ou não.


# Exemplo de utilização da IA
respostaIA = IAMain(email_i)

if respostaIA == 1:
    # Se a IA reconhece como spam, move o e-mail para a lixeira
    time.sleep(2)
    nav.find_element('xpath', '//*[@id=":4"]/div[2]/div[1]/div/div[2]/div[3]/div').click()
else:
    # Se não é spam, volta para a página inicial para o próximo e-mail
    time.sleep(2)
    nav.find_element('xpath', '//*[@id="gb"]/div[2]/div[1]/div[4]/div/a/img').click()
    i += 1
