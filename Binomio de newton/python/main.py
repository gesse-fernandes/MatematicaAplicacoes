def triangulo_pascal(numero_linhas=1):
    linha_atual = [1]
    triangulo = [linha_atual

                 ]
    for linha in range(1, numero_linhas):
        linha_anterior = triangulo[linha - 1]
        linha_atual = [1]
        for i in range(1, len(linha_anterior)):
            linha_atual.append(linha_anterior[i-1] + linha_anterior[i])

        linha_atual.append(1)

        triangulo.append(linha_atual)
    return triangulo


print(triangulo_pascal(2))
def fatorial(n):
   fatorial = 1

   while n >= 1:
      fatorial = fatorial * n
      n = n - 1
   return fatorial

def calculaBinomial(n,p):
       return fatorial(n) / (fatorial(p) * fatorial(n-p))



print(calculaBinomial(10,4))
