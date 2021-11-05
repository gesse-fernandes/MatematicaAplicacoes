#include <stdio.h>

void arranjo(int m, int n);
void combinacao(int m, int n);
double combinacaoHomensMulheres(int m_H, int n_H, int m_M, int n_M);
int fatorial(n);
double arranjoRecursivo(m, n);
double combinacaoComplementarRecursivo(m, p);
int main()
{
     //arranjo(8,2);
    //combinacao(11,3);
    printf("%.0lf", combinacaoHomensMulheres(11, 4, 7, 3));
    //printf("\n%.0lf", arranjoRecursivo(8, 2));
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

void arranjo(int m, int n){
    int M =1,N=1,MN =1;
    double resultado =1.0;
    if(m == 0 ||  m == 1){
        M =1;
    }else{
        for(int i=m; i >=1; i--){
            M=M*i;
        }
        if(m - n == 0  || m - n == 1){
            MN = 1;
        }else{
            for(int i = m-n; i >=1; i--){
                MN= MN*i;
            }
        }
    }
    resultado = M / MN;
    printf("%.0lf",resultado);
}

void combinacao(int m, int n){
    int M=1,N=1,MN=1;
    double result = 1.0;
    if(m == 0 || m == 1 ){
        M  = 1;
    }else{
        for(int i=m; i>=1; i--){
            M=M*i;
        }
        if(n == 0 || n == 1){
            N=1;
        }else{
            for(int i=n; i>=1; i--){
                N=N*i;
            }
        }
        if(m-n == 0 || m-n == 1){
            MN = 1;
        }else{
            for(int i = m -n; i >=1; i--){
                MN=MN*i;
            }
        }
    }
  result = (M / (MN * N));
  printf("%.0lf",result);
}

double combinacaoHomensMulheres(int m_H, int n_H, int m_M, int n_M){
    int mm_H=1,mm_M=1,nn_H=1,nn_M=1,MN_H=1,MN_M=1;
    if(m_H == 0 || m_H == 1 || m_M == 0 || m_M == 1 ){
        mm_H =1;
        mm_M =1;
    }else{
        for(int i = m_H; i>=1; i--){
            mm_H = mm_H*i;
        }
        if(n_H == 0 || n_H == 1){
            n_H = 1;
        }else{
            for(int i= n_H; i>=1; i--){
                nn_H = nn_H*i;
            }

        }
        if(m_H - n_H == 0 || m_H - n_H == 1){
            MN_H = 1;
        }else{
            for(int i = m_H - n_H; i>=1; i--){
                MN_H = MN_H*i;
            }
        }
        for(int i=m_M; i>= 1;i--){
            mm_M = mm_M*i;
        }
        if(n_M == 0 || n_M == 1){
            nn_M = 1;
        }else{
            for(int i= n_M; i>=1; i--){
                nn_M = nn_M*i;
            }
        }
        if(m_M - n_M == 0 || m_M - n_M == 1){
            MN_M =1;
        }else{
            for(int i = m_M - n_M; i>=1; i--){
                MN_M = MN_M*i;
            }
        }
    }
    double resultado_homem = mm_H  /(MN_H * nn_H);
    double resultado_mulher = mm_M / (MN_M * nn_M);

    return resultado_homem * resultado_mulher; 
}
void combinacaoComplementar(pontos, escolher, pontosPossiveis, escolherPossiveis){
    int pointer =1,es=1,p_e=1,po_possiveis=1,es_possiveis=1,p_e_p=1;

    if(pontos == 0 || pontos == 1){
        pointer = 1;
    }else{
        for(int i=pontos; i>=1;i--){
            pointer=pointer*i;
        }
        if(escolher == 0 || escolher == 1){
            es = 1;
        }
    }
}


double combinacaoComplementarRecursivo(m,p){
    if( m == 0 || m == 1 || p == 0 || p == 1){
        return 1;
    }else{
        return fatorial(m) / (fatorial(m-p) * (fatorial(p)));
    }
}