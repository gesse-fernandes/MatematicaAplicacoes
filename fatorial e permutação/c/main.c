#include <stdio.h>
#include <string.h>
int factorialNumerador(int numerador);
int factorialDenominador(int denominador);
double factorialDivisor(int numerador, int denominador);
void permuta(int vetor[], int inf, int sup);
void troca(int vetor[], int i, int j);
int permutaPalavra(int palavra);
int factorialDenominadorDireita(int denominadorDireita);
double factorialNumeradorDenominadorDireita(int numerador, int denominador, int denominadorDireita);
void testPermutacaoPalavra(char *String);
int pessoas(int people);
int main(int argc, char const *argv[])
{
   /* printf(" numerador = %d", factorialNumerador(10));
    printf("\ndenominador = %d", factorialDenominador(8));
    printf("\n divisor %.0lf\n", factorialDivisor(factorialNumerador(10), factorialDenominador(8)));
    int v[] = {1, 2, 3, 4};
    int tam_v = sizeof(v) / sizeof(int);
    //permuta(v, 0, tam_v - 1);
    int teste = strlen("BANANA");
    printf("%d ", permutaPalavra(teste));*/
   testPermutacaoPalavra("MATEMATICA");
   return 0;
}

int factorialNumerador(int numerador)
{
    if (numerador == 1)
    {
        return 1;
    }
    else
    {
        return numerador * factorialNumerador(numerador - 1);
    }
}

int factorialDenominador(int denominador)
{
    if (denominador == 1)
    {
        return 1;
    }
    else
    {
        return denominador * factorialDenominador(denominador - 1);
    }
}

int factorialDenominadorDireita(int denominadorDireita)
{
    if (denominadorDireita == 1)
    {
        return 1;
    }
    else
    {
        return denominadorDireita * factorialDenominadorDireita(denominadorDireita - 1);
    }
}

double factorialDivisor(int numerador, int denominador)
{
    if (numerador == 0)
    {
        return 0;
    }
    else
    {
        return numerador / denominador;
    }
}

double factorialNumeradorDenominadorDireita(int numerador,int denominador,int denominadorDireita){
    if(numerador ==0 ){
        return 0;
    }else{
        return numerador / (denominador * denominadorDireita);
    }
}

int pessoas(int people){
    if (people == 0 || people == 1)
    {
        return 1;
    }
    else
    {
        return people * pessoas(people - 1);
    }
}

void troca(int vetor[], int i, int j)
{
    int aux = vetor[i];
    vetor[i] = vetor[j];
    vetor[j] = aux;
}

void permuta(int vetor[], int inf, int sup)
{
    if (inf == sup)
    {
        for (int i = 0; i <= sup; i++)
        {
            printf(" %d ", vetor[i]);
        }
        printf("\n");
    }
    else
    {
        for (int i = 0; i <= sup; i++)
        {
            troca(vetor, inf, i);
            permuta(vetor, inf + 1, sup);
            troca(vetor, inf, i);
        }
    }
}

int permutaPalavra(int palavra)
{
    if (palavra == 1 || palavra == 0)
        return 1;
    else
        return palavra * permutaPalavra(palavra - 1);
}


void testPermutacaoPalavra(char* String){
    int tam = strlen(String);
    int p = 1;
    if(tam == 1 || tam == 0){
        printf("%d",1);
    }else{
        for (int i = tam; i >= 1; i--){
            p = p * i;
        }
        printf("%d", p);
    }
}