#include <stdio.h>
int fatorial(n);
double arranjoRecursivo(m, n);
double combinacaoComplementarRecursivo(m, p);
int main()
{
    printf("\n%.0lf", combinacaoComplementarRecursivo(11, 4) * combinacaoComplementarRecursivo(7,3));
}

int fatorial(n){
    if(n == 0 || n == 1){
        return 1;
    }else{
        return n * fatorial(n - 1);
    }
}

double arranjoRecursivo(m,n){
    if(m == 0 || m == 1 || n == 0 || n == 1){
        return 1;
    }else{
        return fatorial(m) / (fatorial(m-n));
    }

}
double combinacaoComplementarRecursivo(m,p){
    if( m == 0 || m == 1 || p == 0 || p == 1){
        return 1;
    }else{
        return fatorial(m) / (fatorial(m-p) * (fatorial(p)));
    }
}