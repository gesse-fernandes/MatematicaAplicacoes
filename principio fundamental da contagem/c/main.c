/*
principio fundamental da contagem

ex  uma moeda lancada 3 vezes qual o numero
de sequencias possiveis cara ou coroa.
*/

#include <stdio.h>
int potencia(base, expoente);
int exemploAtletas(int qtd, int possiveis);
int cartasBaralho(int base, int expoente);
int cartasBaralhosSemReposicao(int qtd, int possiveis);
int main(int argc, char const *argv[])
{
    int qtd,caraCoroa;
    printf("Quantidade de vezes de cara ou coroa: ");
    scanf("%d", &qtd);
    printf("quantidade que posso escolher de cara ou coroa: ");
    scanf("%d", &caraCoroa);
    printf("Numero de sequencias: %d", potencia(caraCoroa, qtd));

    printf("\nQuantidade possiveis = %d", exemploAtletas(4, 3));
    printf("\n Cartas com reposicao = %d", cartasBaralho(52, 5));
    printf("\n Cartas sem reposicao = %d", cartasBaralhosSemReposicao(52,5));

     
}


int potencia(int base, int expoente)
{
    if(expoente == 0)
    {
        return 1;
    }else{
        return base * potencia(base, expoente -1);
    }
}

int exemploAtletas(int qtd, int possiveis)
{
    if(qtd == 0 ){
        return 1;
    }
    else{
        return exemploAtletas(qtd - 1, possiveis) * qtd;
    }
}
int cartasBaralho(int base, int expoente)
{
    if (expoente == 0)
    {
        return 1;
    }else{
        return base * cartasBaralho(base, expoente - 1);
    }
}
int cartasBaralhosSemReposicao(int qtd, int possiveis)
{
    int i,test;

    for (i = 1; i <= possiveis; i++)
    {
        test *= qtd;
        qtd--;

    }

    return test;
}



