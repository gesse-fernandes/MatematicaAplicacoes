import java.lang.reflect.Type;

class Permutacao {
    public static int fatPalavra(String palavra)
    {
        int tam = palavra.length();
        int fatP = 1;
        if (tam == 1 || tam == 0)
            return 1;
        else
            for (int i = tam; i >= 1; i--)
                fatP = fatP * i;
        return fatP;
    }

    public static int fatorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * fatorial(n - 1);
        }
    }
    
    public static int factorialNumerador(int numerador) {
        if (numerador == 1) {
            return 1;
        } else {
            return numerador * factorialNumerador(numerador - 1);
        }
    }

    public static int factorialDenominador(int denominador) {
        if (denominador == 1) {
            return 1;
        } else {
            return denominador * factorialDenominador(denominador - 1);
        }
    }
    
    public static int factorialDenominadorDireita(int denominadorDireita) {
        if (denominadorDireita == 1) {
            return 1;
        } else {
            return denominadorDireita * factorialDenominadorDireita(denominadorDireita - 1);
        }
    }
    
    public static double factorialDivisor(int numerador, int denominador) {
        if (numerador == 0) {
            return 0;
        } else {
            return numerador / denominador;
        }
    }
    
    public static double factorialNumeradorDenominadorDireita(int numerador, int denominador, int denominadorDireita) {
        if (numerador == 0) {
            return 0;
        } else {
            return numerador / (denominador * denominadorDireita);
        }
    }
    
    public static int pessoas(int people) {
        if (people == 0 || people == 1) {
            return 1;
        } else {
            return people * pessoas(people - 1);
        }
    }
    
    public static void troca(int vetor[], int i, int j) {
        int aux = vetor[i];
        vetor[i] = vetor[j];
        vetor[j] = aux;
    }

    public static void permuta(int vetor[], int inf, int sup) {
        if (inf == sup) {
            for (int i = 0; i <= sup; i++) {
                System.out.printf(" %d ", vetor[i]);
            }
            System.out.printf("\n");
        } else {
            for (int i = 0; i <= sup; i++) {
                troca(vetor, inf, i);
                permuta(vetor, inf + 1, sup);
                troca(vetor, inf, i);
            }
        }
    }

    public static int permutaPalavra(int palavra) {
        if (palavra == 1 || palavra == 0)
            return 1;
        else
            return palavra * permutaPalavra(palavra - 1);
    }

 public static void testPermutacaoPalavra(String String){
    int tam = String.length();
    int p = 1;
    if(tam == 1 || tam == 0){
        System.out.printf("%d",1);
    }else{
        for (int i = tam; i >= 1; i--){
            p = p * i;
        }
        System.out.printf("%d", p);
    }
}

    public static void main(String[] args) {
        //System.out.println(fatPalavra("GESSE"));
       //testPermutacaoPalavra("GESSEX");
       int v[] = {1, 2, 3, 4};
   
        permuta(v, 0, 4 - 1);
    }
}