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

def arranjo(m, n):
    M = 1
    N = 1
    MN = 1
    if m == 1 or m == 0:
        M = 1
    else:
        for i in range(m, 0, -1):
            M = M*i

        if m - n == 0 or m - n == 1:
            MN = 1
        else:
            for i in range(m-n, 0, -1):
                MN = MN*i

    resultado = M / MN
    result = 1
    # for i in range(MN):
    #result *= resultado
    print(resultado)


arranjo(8, 2)

def arranjoRecursivo(m,n):
    if m == 0 or m ==  1 or n == 0 or n == 1:
        return 1
    else: 
        return  fatorial(m) / (fatorial(m-n))


print(arranjoRecursivo(8,2))

def combinacao(m, n):
    M = 1
    N = 1
    MN = 1
    if m == 1 or m == 0:
        M = 1
    else:
        for i in range(m, 0, -1):
            M = M*i
        if n == 1 or n == 0:
            N = 1
        else:
            for i in range(n, 0, -1):
                N = N*i

        if m - n == 0 or m - n == 1:
            MN = 1
        else:
            for i in range(m-n, 0, -1):
                MN = MN*i
    print(M)
    #print(M / (MN * N))


#combinacao(11, 3)


# combinacao de homens e mulheres
def combinacaoHomensMulheres(m_H, n_H, m_M, n_M):
    mm_H = 1
    mm_M = 1
    nn_H = 1
    nn_M = 1
    MN_H = 1
    MN_M = 1
    if m_H == 1 or m_H == 0 or m_M == 1 or m_M == 0:
        mm_H = 1
        mm_M = 1
    else:
        for i in range(m_H, 0, -1):
            mm_H = mm_H*i
        if n_H == 1 or n_H == 0:
            nn_H = 1

        else:
            for i in range(n_H, 0, -1):
                nn_H = nn_H*i

        if m_H - n_H == 0 or m_H - n_H == 1:
            MN_H = 1
        else:
            for i in range(m_H-n_H, 0, -1):
                MN_H = MN_H*i

        for i in range(m_M, 0, -1):
            mm_M = mm_M*i
        if n_M == 1 or n_M == 0:
            nn_M = 1
        else:
            for i in range(n_M, 0, -1):
                nn_M = nn_M*i

        if m_M - n_M == 0 or m_M - n_M == 1:
            MN_M = 1
        else:
            for i in range(m_M-n_M, 0, -1):
                MN_M = MN_M*i

    resultado_homem = mm_H / (MN_H * nn_H)
    resultado_mulher = mm_M/(MN_M * nn_M)
    #print(resultado_homem * resultado_mulher)
    return resultado_homem * resultado_mulher

# print(combinacaoHomensMulheres(11,4,7,3))
#print(combinacaoHomensMulheres(3, 1, 8, 4)* combinacaoHomensMulheres(10, 4, 6, 2))

# adaptada

"""
def combinacaoComplementar(pontos, escolher, pontosPossiveis, escolherPossiveis):
    pounter = 1
    es = 1
    p_e = 1
    po_possiveis = 1
    es_possiveis = 1
    p_e_p = 1
    if pontos == 0 or pontos == 1:
        pounter = 1
    else:
        for i in range(pontos, 0, -1):
            pounter = pounter*i
        if escolher == 1 or escolher == 0:
            es = 1
        else:
            for i in range(escolher, 0, -1):
                es = es * i

        if pontos - escolher == 0 or pontos - escolher == 1:
            p_e = 1
        else:
            for i in range(pontos-escolher, 0, -1):
                p_e = p_e*i

    resultP = pounter/(p_e * es)

    if pontosPossiveis == 0 or pontosPossiveis == 1:
        po_possiveis = 1
    else:
        for i in range(pontosPossiveis, 0, -1):
            po_possiveis = po_possiveis*i
        if escolherPossiveis == 1 or escolherPossiveis == 0:
            es_possiveis = 1
        else:
            for i in range(escolherPossiveis, 0, -1):
                es_possiveis = es_possiveis * i

        if pontosPossiveis - escolherPossiveis == 0 or pontosPossiveis - escolherPossiveis == 1:
            p_e_p = 1
        else:
            for i in range(pontosPossiveis-escolherPossiveis, 0, -1):
                p_e_p = p_e_p*i

    resultP_E_P = po_possiveis/(p_e_p * es_possiveis)
    final = resultP - resultP_E_P
    print(final)
"""

#combinacaoComplementar(11, 4, 7, 3)





def combinacaoTest(m, n):
    if m == 1 or m == 0 or n == 1 or n == 1:
        return 1
    else:
        return fatorial(m) / (fatorial(n) * fatorial(m-n))



#print(combinacaoTest(11,4) - combinacaoTest(7,3))
