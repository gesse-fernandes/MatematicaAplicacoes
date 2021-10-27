"""
principio fundamental da contagem

ex 1  uma moeda lancada 3 vezes qual o numero
de sequencias possiveis cara ou coroa.

ex 2 quatro atletas  que participam na corrida
quantos resultados existem para o primeiro,segundo e terceiro lugar

ex 3 baralho 52 cartas considre 5 cartas 
sao escolhidas  sucessivamente 
a) quantas sao as sequencias de resultados
se a escolha é feita com reposicao?

"""


import matplotlib.pyplot as plt
import random
import numpy as np
id_para_moeda = {0: 'coroa', 1: 'cara'}
moeda_para_id = {'coroa': 0, 'cara': 1}


def jogarMoeda():
    return id_para_moeda[random.randint(0,1)]

def quantidadeVezesCaraCoroa(base,expoente):

    if expoente == 0 :
         return 1
    else:
        return base * quantidadeVezesCaraCoroa(base,expoente -1)


for i in range(3):
        print(jogarMoeda())


print(quantidadeVezesCaraCoroa(2,3))

"""
def jogar_n_vezes(n=100, imprimir=True):
    if imprimir:
        print(f'Jogando moeda {n} vezes\n')
    resultados = []
    for i in range(n):
        resultados.append(moeda_para_id[jogarMoeda()])
    
    n_caras = sum(resultados)
    n_coroas = n-n_caras
    if imprimir:
        print(f'Resultado\ncara = {n_caras} vezes\ncoroa = {n_coroas} vezes')
    return resultados, n_caras, n_coroas

_=jogar_n_vezes(200)


numero_de_rodadas = 1000
jogadas_por_rodada = 100

n_caras_rodada = []
n_coroas_rodada = []

for rodada in range(numero_de_rodadas):
    _, n_caras, n_coroas = jogar_n_vezes(jogadas_por_rodada, False)
    n_caras_rodada.append(n_caras)
    n_coroas_rodada.append(n_coroas)

_ = plt.hist(n_caras_rodada, 100)
plt.title('Frequencia do numero de caras')
plt.show()

_ = plt.hist(n_coroas_rodada, 100)
plt.title('Frequencia do numero de coroas')
plt.show()



caras_avg = np.mean(n_caras_rodada)
caras_std = np.std(n_caras_rodada)
coroas_avg = np.mean(n_coroas_rodada)
coroas_std = np.std(n_coroas_rodada)

print(f'Média de caras: {caras_avg}')
print(f'Média de coroas: {coroas_avg}')
print(f'Desvio padrão de caras {caras_std:.2f}')
print(f'Desvio padrão de coroas {coroas_std:.2f}')
"""


def exemploAtletas(qtd,possiveis):
    if qtd == 0 or qtd == 1:
        return 1
    else: 
        return exemploAtletas(qtd -1, possiveis)* qtd 


print(exemploAtletas(4,3))





