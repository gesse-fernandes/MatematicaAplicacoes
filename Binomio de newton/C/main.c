#include <stdio.h>
int fatorial(int n);
double calculaBinomial(int n, int p);
int main(int argc, char const *argv[])
{
    printf("%1.lf ", calculaBinomial(10, 4));
    return 0;
}
int fatorial(int n)
{
   if(n == 0 || n == 1){
       return 1;
   }else{
       return n * fatorial(n - 1);
   }
}

double calculaBinomial(int n, int p){
    return fatorial(n) / (fatorial(p) * fatorial(n - p));
}
