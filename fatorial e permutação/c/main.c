#include <stdio.h>

int factorialNumerador(int numerador);
int factorialDenominador(int denominador);
double factorialDivisor(int numerador, int denominador);
void permuta(int vetor[], int inf, int sup);
void troca(int vetor[], int i, int j);
int main(int argc, char const *argv[])
{
    printf(" numerador = %d", factorialNumerador(10));
    printf("\ndenominador = %d", factorialDenominador(8));
    printf("\n divisor %.0lf\n", factorialDivisor(factorialNumerador(10), factorialDenominador(8)));
    int v[] = {1, 2, 3, 4};
    int tam_v = sizeof(v) / sizeof(int);
    permuta(v, 0, tam_v - 1);
    return 0;
}

int factorialNumerador(int numerador){
    if(numerador == 1)
    {
        return 1;
    }else{
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

double factorialDivisor(int numerador, int denominador)
{
    if(numerador == 0){
        return 0;
    }
    else{
        return numerador / denominador;
    }
}


void troca(int vetor[],int i, int j)
{
    int aux = vetor[i];
    vetor[i] = vetor[j];
    vetor[j] = aux;
}

void permuta(int vetor[],int inf , int sup)
{
    if(inf == sup)
    {
        for (int i = 0; i <= sup; i++)
        {
            printf(" %d ", vetor[i]);
        }
        printf("\n");
    }else{
        for (int i = 0; i <= sup; i++)
        {
            troca(vetor, inf, i);
            permuta(vetor, inf + 1,sup);
            troca(vetor, inf, i);
        }
    }
}
