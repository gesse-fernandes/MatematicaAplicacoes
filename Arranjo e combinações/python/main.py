"""
O arranjo m Elementos
o organizar de n formas 
A,m,n = m!/(m-n)!

ex 01 
bolas= vermelhas,brancas,azul
3 x 3 = 9 bolas

A_3,1 x A,3,1 = 3!/(3-1)!

A = ordem importa

######

combinacao 
M = {a1,a2....an}

C_n = m!/(m-n)!n!
ordem nao importa

ex 2 = conjunto de 10 funcionarios comissao  de 3 pessoas 

exe 3 conjunto de 10 funcionarios 10 h e 10 m de comissao 5 entre 3 h e 2 m

ex 4  5 pontos(A,B,C,D,E) quantos triangulos eu consigo formar numero total de combinacoes possiveis 12 pontos
escolher 3 subtrair do 5,3 escolher 3 deles possiveis pra formar o triangulo combinacaoComplementar


"""
def fatorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fatorial(n-1)
def arranjoRecursivo(m,n):
    if m == 0 or m ==  1 or n == 0 or n == 1:
        return 1
    else: 
        return  fatorial(m) / (fatorial(m-n))
print(arranjoRecursivo(8,2))

def combinacaoRecursiva(m, n):
    if m == 1 or m == 0 or n == 1 or n == 1:
        return 1
    else:
        return fatorial(m) / (fatorial(n) * fatorial(m-n))
