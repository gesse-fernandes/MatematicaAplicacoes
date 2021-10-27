class PrincipioFundamentalContagem {
    public static int potencia(int base, int expoente) {
        if (expoente == 0) {
            return 1;
        } else {
            return base * potencia(base, expoente - 1);
        }
    }
    public static void main(String[] args) {
        System.out.println(potencia(2, 3));
    }

}


