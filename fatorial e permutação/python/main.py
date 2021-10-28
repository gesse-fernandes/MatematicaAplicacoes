"""
EX 1 10!/ 8! = 90
ex 2 12!/ 9! X 3! = 220

ex 3 (n-6)! 720
    (n-6)(n-5)! = 720
    (n-6)(n-5)!=  6 . 120
    (n-6)(n-5)! = 6 . 5!

ex 4  1/n! - 1/(n+1)! = n/(n+1)!
1/n! - 1/(n+1)n! = n/(n+1)!

(n+1) -1/ n!(n+1) =  n/(n+1)!

permutacoes

seja M = {a1 ..... an} definimos a permutacao de M elementos
P_m = m!

ex  05
de quantas formas podem 5 pessoas ficar em fila
indiana! 5! = 5 . 4 . 3 . 2 .1 = P_5 

permutacoes com repeticao

MATEMATICA = P_10, 2,3,2
"""

from itertools import permutations
from typing import NoReturn, Text


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


def fatorialNumerador(numerador):
    if numerador == 0 or numerador == 1:
        return 1
    else:
        return numerador * fatorialNumerador(numerador-1)


def fatorialDenominador(denominador):
    if denominador == 0 or denominador == 1:
        return 1
    else:
        return denominador * fatorialDenominador(denominador-1)


def factorialDenominadorDireita(denominadorDireita):
    if denominadorDireita == 0 or denominadorDireita == 1:
        return 1
    else:
        return denominadorDireita * factorialDenominadorDireita(denominadorDireita-1)


def factorialNumeradorDenominador(numerador, denominador):
    if numerador == 0 or numerador == 1:
        return 1
    else:
        return numerador / denominador


def factorialNumeradorDenominadorDireita(numerador, denominador, denominadorDireita):
    if numerador == 0 or numerador == 1:
        return 1
    else:
        return (numerador / (denominador * denominadorDireita))


print(factorial(10))


print(factorialNumeradorDenominador(
    fatorialNumerador(10), fatorialDenominador(8)))


print(factorialNumeradorDenominadorDireita(
    fatorialNumerador(12), fatorialDenominador(9), factorialDenominadorDireita(3)))
# ex 5 pessoas na fila


def pessoas(people):
    if people == 0 or people == 1:
        return 1
    else:
        return people * pessoas(people - 1)


print(pessoas(5))

print(len("MATEMATICA"))


def permutations(string, step=0):

    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("".join(string))

    # everything to the right of step has not been swapped yet
    for i in range(step, len(string)):

        # copy the string (store as array)
        string_copy = [character for character in string]

        # swap the current index with the step
        string_copy[step], string_copy[i] = string_copy[i], string_copy[step]

        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)


# permutations("BANANA")

def permute(data, i, length):
    if i == length:
        print(''.join(data))
    else:
        for j in range(i, length):
            # swap
            data[i], data[j] = data[j], data[i]
            permute(data, i+1, length)
            data[i], data[j] = data[j], data[i]


#string = "BANANA"
#n = len(string)
#data = list(string)
#permute(data, 0, n)


def testPalavra(string):
    tamanho = len(string)
    test = 1
    if tamanho == 0 or tamanho == 1:
        return 1
    else:
        for i in range(tamanho, 0, -1):
            test = test * i

    print(test)


testPalavra("MATEMATICA")


test = "Python é lindo Python top"
substring = "Python"

total = test.count(substring)
print(str(total))


totM = 0
s = "MATEMATICA"
for letras in range(len(s)):
    if s[letras] == "M":
        totM += 1
print(totM)


def funcaoRetorna(string):
    tam = len(string)
    totM = 0
    totA = 0
    totT = 0
    totN = 0
    strstring = 1
    strStringM = 1
    strStringA = 1
    strSringT = 1
    strSringN = 1
    if tam == 1 or tam == 0:
        return 1
    else:
        for MRepet in range(tam):
            if string[MRepet] == "M":
                totM += 1
            elif string[MRepet] == "A":
                totA += 1
            elif string[MRepet] == "T":
                totT += 1
            elif string[MRepet] == "N":
                totN += 1

        for i in range(tam, 0, -1):
            strstring = strstring * i

        if totM == 0 or totA == 0 or totT == 0:
            return 1
        else:
            for i in range(totM, 0, -1):
                strStringM = strStringM*i
            for i in range(totA, 0, -1):
                strStringA = strStringA*i

            for i in range(totT, 0, -1):
                strSringT = strSringT*i
            for i in range(totN, 0, -1):
                strSringN = strSringN*i

        print(strstring/(strStringM * strStringA * strSringT))
    # print(strstring)


# funcaoRetorna("MATEMATICA")


def permutacaoPalavrasTotal(String):
    palavra_tam = len(String)
    fat = 1
    if palavra_tam == 1 or palavra_tam == 0:
        return 1
    else:
        for i in range(palavra_tam, 0, -1):
            fat = fat * i
    print(fat)


def permutacaoPalavrasRepetidas(String):
    totA = 0
    totB = 0
    totN = 0
    totM = 0
    totT = 0
    totG = 0
    totE = 0
    totS = 0
    permP = 1
    permA = 1
    permB = 1
    permE = 1
    permG = 1
    permN = 1
    permM = 1
    permS = 1
    permT = 1

    p = len(String)
    if p == 1 or p == 0:
        return 1
    else:
        for i in range(p):
            if String[i] == "A" or String[i] == "a":
                totA += 1
            else:
                totA = totA
        for i in range(p):
            if String[i] == "B" or String[i] == "b":
                totB += 1
            else:
                totB = totB
        for i in range(p):
            if String[i] == "E" or String[i] == "e":
                totE += 1
            else:
                totE = totE
        for i in range(p):
            if String[i] == "G" or String[i] == "g":
                totG += 1
            else:
                totG = totG

        for i in range(p):
            if String[i] == "N" or String[i] == "n":
                totN += 1
            else:
                totN = totN
        for i in range(p):
            if String[i] == "M" or String[i] == "m":
                totM += 1
            else:
                totM = totM
        for i in range(p):
            if String[i] == "S" or String[i] == "s":
                totS += 1
            else:
                totS = totS
        for i in range(p):
            if String[i] == "T" or String[i] == "t":
                totT += 1
            else:
                totT = totT

        for i in range(p, 0, -1):
            permP = permP*i

        if totA == 0 or totA == 1:
            totA = 1
        else:
            for i in range(totA, 0, -1):
                permA = permA * i
        if totB == 0 or totB == 0:
            totB = 1
        else:
            for i in range(totB, 0, -1):
                permB = permB * i
        if totE == 0 or totE == 0:
            totE = 1
        else:
            for i in range(totE, 0, -1):
                permE = permE * i

        if totG == 0 or totG == 0:
            totG = 1
        else:
            for i in range(totG, 0, -1):
                permG = permG * i

        if totN == 0 or totN == 1:
            totN = 1
        else:
            for i in range(totN, 0, -1):
                permN = permN * i
        if totM == 0 or totM == 1:
            totM = 1
        else:
            for i in range(totM, 0, -1):
                permM = permM * i
        if totS == 0 or totS == 1:
            totS = 1
        else:
            for i in range(totS, 0, -1):
                permS = permS * i
        if totT == 0 or totT == 1:
            totT = 1
        else:
            for i in range(totT, 0, -1):
                permT = permT * i

    print(permP / (permA * permB * permN * permM * permT * permE * permG * permS))


# permutacaoPalavrasTotal("ABACAXI")
permutacaoPalavrasRepetidas("FERNANDES")
