class Permutacao {
    public static int fatPalavra(String palavra)
    {
        int tam = palavra.length();
        int fatP = 1;
        if(tam == 1 || tam == 0)
            return 1;
        else 
            for(int i=tam; i>=1; i--)
                fatP = fatP * i;
        return fatP;
    }
    public static void main(String[] args) {
        System.out.println(fatPalavra("GESSE"));
    }
}