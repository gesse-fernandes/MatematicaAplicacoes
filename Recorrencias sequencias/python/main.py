"""
Recorrencias
"""


import matplotlib.pyplot as plt
import numpy as np

"""
R = np.linspace(0.5,4,20000)

X = []
Y = []


for r in R:
    X.append(r)

    x = np.random.random()

    for l in range(1000):
        x = r*x*(1-x)
    Y.append(x)

plt.plot(X,Y,ls ='',marker = ',')
plt.show()
"""


def sequenciaFibonacci(qtd):
    if qtd is not int and qtd < 0:
        raise TypeError(f'O valor de {qtd} nao é numero inteiro positivo!')
    F_1 = 0
    F_2 = 1
    iteracao = 0
    print(f'Os termos de sequencia de Fibonnaci com {qtd} termos são: ')
    print()
    while iteracao <= qtd:
        F_3 = F_2 + F_1
        F_1 = F_2
        F_2 = F_3
        iteracao += 1
        print(F_1, end=',')


# sequenciaFibonacci(10)


def fibo(termos):
    if termos <= 2:
        return 1
    else:
        return fibo(termos-1) + fibo(termos-2)


q = 10
iteracao = 0
while(iteracao < q):
    iteracao += 1
    # print(fibo(iteracao))


# print(fibo(4))


def recorrenciaSequencia(n):
    if n <= 2:
        return 1
    else:
        return recorrenciaSequencia(n - 1) + recorrenciaSequencia(n-2)


# print()
# print(recorrenciaSequencia(10))


def seq(n):
    if n >= 2:
        return seq(n-1) + seq(n - 2)
    else:
        return n


# print(seq(4))


def Tseq(n):
    if n >= 2:
        return Tseq(n - 1) + Tseq(n-2) + Tseq(n-3)
    else:
        return n


# print(Tseq(12))


def fibbonaci(n):
    if n <= 2:
        return n
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)


# print(fibbonaci(8))


def serieSequencias(terms=50):
    soma = 0
    i = 1
    while i <= terms:
        if i % 2 == 0:
            soma += i + (i*i)
            print(i, i*i, end=' ')
        i += 1
    print(f"Soma = {soma}")


# serieSequencias()


def factoral(numero):
    #fatorial = 1
    #contador = 2
    # while contador <= numero:
    #fatorial = fatorial*contador
    #contador = contador+1
    #print(f'O valor de {numero} é igual á {fatorial}')
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * factoral(numero - 1)


# print(factoral(5))

# funcao que calcula a potencia de forma recursiva


def potencia(base, expoente):
    if expoente == 0:
        potencia = 1
    else:
        potencia = 1
        iteracao = 1
        while iteracao <= expoente:
            potencia *= base
            iteracao += 1
    print(f'O valor de {base} elevado á {expoente} é igual á {potencia}')


#potencia(5, 2)


def progressao_aritmetica(numero_termos, razao, a_1):
    contador = 1
    print(f'Progressao aritmetica com {numero_termos} e: ')
    while contador <= numero_termos:
        a_n = a_1 + (contador - 1) * razao
        contador = contador+1
        print(a_n, end=' ')


#progressao_aritmetica(8, 5, 0)


def PA(terms, r, a_1):
    cont = 1
    if terms == 0 or terms == 1:
        return 1
    else:
        while cont <= terms:
            a_n = a_1 + (cont-1) * r
            cont += 1
            print(a_n, end=' ')


#PA(100, 1, 1)


def progressao_geometrica(numero_termos, razao, a_1):
    contador = 1
    print(f'Progressao Geometrica com {numero_termos} e: ')
    while contador <= numero_termos:
        a_n = a_1 * pow(razao, (contador-1))
        contador = contador+1
        print(a_n, end=' ')


#progressao_geometrica(4, 6, 1)

def sn(a1, an, terms):
    cont = 1
    while cont <= terms:
        res = ((a1 + an) * terms)/2
        cont += 1
    print(res)


def termoGeral(a1, terms, r=1):
    an = a1 + (terms-1)*r
    sn = ((a1 + an) * terms)/2
    return sn


# print(termoGeral(1,40,4))
