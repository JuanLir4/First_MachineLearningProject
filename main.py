import tensorflow as tf
from tensorflow.keras.layers import Dense
from tensorflow.keras import Sequential
import numpy as np

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

email_teste = """
er online >

Samsung Logo
Jan. 2024

Dobradinha SSG
Tem uma oferta mais surpreendente que a outra
esperando por você na Dobradinha Samsung 10/01,
além das vantagens incríveis de Samsung.com:

EU QUERO SOUNDBAR
EU QUERO HOME APPLIANCE
DESCUBRA MAIS OFERTASDESCUBRA MAIS OFERTAS
Samsung Pay
Samsung Members
Samsung Care Plus
Samsung Shop
Eco Troca
SSG LOCKER
TENHO EMPRESA
SOU ESTUDANTE
SOU MEMBER
Samsung
Instagram	TikTok	Youtube	Twitter	Facebook
Samsung
Samsung
Consulte a nossa Política de Privacidade . Caso não queira mais receber nossos e-mails, clique aqui.

Samsung Eletrônica da Amazônia Ltda. Avenida dos Oitis, nº 1.460, Distrito Industrial II, Manaus/AM, CEP: 69.007-002

Produzido no polo industrial de Manaus - Conheça a Amazônia	
Imagens meramente ilustrativas. Cupom válido até 11/01/2024 às 23h59 ou enquanto durante os estoques. Os produtos disponíveis podem variar de acordo com o estoque da loja no momento da compra. Clique aqui e saiba em quais aparelhos o Samsung Pay está disponível. Consulte termos e condições para a contratação do Samsung Care+. O registro desse plano na SUSEP não implica, por parte da autarquia, incentivo ou rectttomendação à sua comercialização. Processo Susep 15.414.900032/2014-26. 0195 – Garantia Estendida/Extensão de Garantia – Bens em Geral e Processo Susep nº 15414.902134/2013-03. 0171 - Seguro de Aparelhos Eletrônicos - Riscos Diversos
"""

previsao = model.predict(ExtrairProp(email_teste))
if float(previsao[0]) > 0.5:
    previsao = 1
elif float(previsao[0]) < 0.5:
    previsao = 0

print(previsao)
