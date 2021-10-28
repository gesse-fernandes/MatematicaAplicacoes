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
from typing import Text


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
        totM +=1
print(totM)


def funcaoRetorna(string):
    tam = len(string)
    totM = 0
    totA = 0
    totT = 0
    strstring = 1
    if tam == 1 or tam == 0:
        return 1
    else: 
        for MRepet in range(tam):
            if string[MRepet] == "M":
                totM+=1
            elif string[MRepet] == "A":
                totA+=1
            elif string[MRepet] == "T":
                totT+=1
        for i in range(tam,0,-1):
             strstring = strstring * i

        if totM == 1 or totM == 0 or totA == 1 or totA == 0 or totT == 1 or totT ==0:
            return 1
        else: 
             
        
        
        

funcaoRetorna("MATEMATICA")
            


