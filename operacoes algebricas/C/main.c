#include <stdio.h>

int soma(int x, int y);
int produto(int x, int y);
int pot(int x, int y);
int main(int argc, char const *argv[])
{
    /* code */
    return 0;
}

int soma(int x, int y){
    return x + y;
}

int produto(int x, int y) { 
    return x * y; 
    }

int pot(int x, int y){
    if (y== 0)
        return 1;
    else
        return x * pot(x, y - 1);
}
