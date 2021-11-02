public class RecorrenciaSequencia {

    public static void sequenciaFibonacci(int qtd){
    
    if(qtd  < 0){
       System.out.printf("O valor de %d não e um numero inteiro positivo", qtd);
    }
    int f_1 = 0;
    int f_2 = 1;
    int iteracao = 0;
    System.out.printf("Os termos da sequencia de fibonnaci e %d termos sao: ", qtd);
    System.out.printf("\n");
    while(iteracao <=qtd){
        int f_3 = f_2 + f_1;
        f_1 = f_2;
        f_2 = f_3;
        iteracao += 1;
        System.out.printf(" %d ", f_1);
    }
}

    public static int fibo(int termos) {
        if (termos <= 2) {
            return 1;
        } else {
            return fibo(termos - 1) + fibo(termos - 2);
        }
    }

    public static int recorrenciaSequencia(int n) {
        if (n <= 2) {
            return 1;
        } else {
            return recorrenciaSequencia(n - 1) + recorrenciaSequencia(n - 2);
        }
    }

    public static void serieSequencias(int termos) {
        int soma = 0, i = 1;
        while (i <= termos) {
            if (i % 2 == 0) {
                soma += i + (i * i);
                System.out.printf("%d  %d ", i, i * i);
            }
            i++;
        }
        System.out.printf("\nSoma = %d", soma);
    }

public static int factoral(int n){
    if(n == 0 || n == 1){
        return 1;
    }else{
        return n * factoral(n - 1);
    }
}

    public static void potencia(int base, int expoente) {
        if (expoente == 0) {
            return;
        } else {
            int potencia = 1;
            int iteracao = 1;
            while (iteracao <= expoente) {
                potencia *= base;
                iteracao++;
            }
            System.out.printf("O valor de %d elevado a %d e igual a %d", base, expoente, potencia);
        }
    }

    public static void progressao_aritmetica(int numero_termos, int razao, int a_1) {
        int contador = 1;
        System.out.printf("Progressa aritimetica com %d: ", numero_termos);
        while (contador <= numero_termos) {
            int a_n = a_1 + (contador - 1) * razao;
            contador++;
            System.out.printf(" %d ", a_n);
        }
    }

    public static void PA(int terms, int r, int a1) {
        int cont = 1;
        if (terms == 0 || terms == 1) {
            return;
        } else {
            while (cont <= terms) {
                int an = a1 + (cont - 1) * r;
                cont++;
                System.out.printf(" %d ", an);
            }
        }
        
    }

    public static void progressao_geometrica(int numero_termos, int razao, int a1) {
        int contador = 1;
        System.out.printf("Progressao geometricas com %d e: ", numero_termos);
        while (contador <= numero_termos) {
            int an = (int) (a1 * Math.pow(razao, (contador - 1)));
            contador++;
            System.out.printf(" %d ", an);
        }
    }

    public static void sn(int a1, int an, int terms) {
        int cont = 1;
        int res = 1;
        while (cont <= terms) {
            res = ((a1 + an) * terms) / 2;
            cont++;

        }
        System.out.printf("%d", res);
    }

    public static int termoGeral(int a1, int terms, int r) {
        int an = a1 + (terms - 1) * r;
        int sn = ((a1 + an) * terms) / 2;
        return sn;
    }
    public static void main(String[] args) {
        //sequenciaFibonacci(10);
    int qtd = 10,i;
    for (i = 0; i <= qtd; i++){
        //printf(" %d ", fibo(i));
    }
    //printf("%d ", recorrenciaSequencia(4));
    //serieSequencias(50);
    //printf("%d ", factoral(5));
    //potencia(5, 2);
    //progressao_aritmetica(8,5,0);
     //PA(100,1,1);
    //progressao_geometrica(4,6,1);
    System.out.printf("%d", termoGeral(1, 40, 4));
    }
}
