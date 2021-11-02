"""
Operações algebricas
"""


def soma(x,y):
    return x + y

def produto(x,y):
    return x*y


def  pot(x,y):
    if y == 0:
        return 1
    else: 
        return x  * pot(x,y -1)


print(pot(5,2))


def associativa():
    matriz_assoc = {
        "a": [1, 2, 3, ],
        "b": [4, 5, 6, ],
        "c": [7, 8, 9, ]
    }
    for linha in sorted(matriz_assoc.keys()):
        print(matriz_assoc[linha])


associativa()