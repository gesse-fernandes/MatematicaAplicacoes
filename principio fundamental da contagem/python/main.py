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

b) sem reposicao


ex 4  um homem encontra-se na origem
de um sistema cartesiano ortogonal
de eixos x,y considere que ele pode caminhar
a uma unidade considere que ele pode dar 
um passo de cada vez, passo pro norte
ou para o leste
quantas trajetorias ele pode percorrer
se ele der exatamente 4 passos 

"""


from math import pi, exp, sqrt
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

cara_entre_45_e_55 = sum(45<=n<=55 for n in n_caras_rodada)
cara_entre_40_e_60 = sum(40<=n<=60 for n in n_caras_rodada)
coroa_entre_45_e_55 = sum(45<=n<=55 for n in n_coroas_rodada)
coroa_entre_40_e_60 = sum(40<=n<=60 for n in n_coroas_rodada)

print(f'Número de rodadas: {numero_de_rodadas}')
print(f'Número de jogadas de moeda por rodada {jogadas_por_rodada}')
print(f'Quantidade de rodadas que caíram cara entre 45 e 55 vezes: {cara_entre_45_e_55}')
print(f'Quantidade de rodadas que caíram cara entre 40 e 60 vezes: {cara_entre_40_e_60}')
print(f'Quantidade de rodadas que caíram coroa entre 45 e 55 vezes: {coroa_entre_45_e_55}')
print(f'Quantidade de rodadas que caíram coroa entre 40 e 60 vezes: {coroa_entre_40_e_60}')


def normal_distr(avg, std, num=50):
    def f(x): return exp(-(x-avg)**2/(2*std**2))/sqrt(2*pi*std**2)
    X = np.linspace(avg-3*std, avg+3*std, num=num)
    return X, np.array([f(x) for x in X])

X,y = normal_distr(50, 5)
_ = plt.plot(X, y)

_ = plt.hist(n_caras_rodada, 100)
_ = plt.plot(X, y*1000)

def exemploAtletas(qtd,possiveis):
    if qtd == 0 or qtd == 1:
        return 1
    else: 
        return exemploAtletas(qtd -1, possiveis)* qtd 


print(exemploAtletas(4,3))





