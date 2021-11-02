class PrincipioFundamentalContagem {
    public static int potencia(int base, int expoente) {
        if (expoente == 0) {
            return 1;
        } else {
            return base * potencia(base, expoente - 1);
        }
    }

    public static int exemploAtletas(int qtd, int possiveis) {
        if (qtd == 0 || qtd == 1) {
            return 1;
        } else {
            return exemploAtletas(qtd - 1, possiveis) * qtd;
        }
    }

    public static int cartasBaralho(int base, int expoente) {
        if (expoente == 0) {
            return 1;
        } else {
            return base * cartasBaralho(base, expoente - 1);
        }
    }

    public static int cartasBaralhosSemReposicao(int qtd, int possiveis) {
        int baralho = 1;
        for (int i = 1; i <= possiveis; i++) {
            baralho *= qtd;
            qtd--;
        }
        return baralho;
    }

    public static int cartesianoOrtogonal(int eixos, int passos) {
        if (passos == 0) {
            return 1;
        } else {
            return eixos * cartesianoOrtogonal(eixos,passos-1);
        }
    }
    public static void main(String[] args) {
        //System.out.println(potencia(2, 3));
        //System.out.println(exemploAtletas(4, 3));
        //System.out.println(cartasBaralho(52,5));
        // System.out.println(cartasBaralhosSemReposicao(52, 5));
        System.out.println(cartesianoOrtogonal(2, 4));
    }

}


