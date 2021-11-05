class ArranjoCombinacao{
    public static int fatorial(int n){
        if(n == 0 || n == 1){
            return 1;
        }else{
            return n * fatorial(n-1);
        }
    }

    public static double arranjoRecursivo(int m, int p) {
        if (m == 0 || m == 1 || p == 0 || p == 1) {
            return 1;
        } else {
            return fatorial(m) / (fatorial(m - p));
        }
    }
    
    public static double combinacaoRecursivo(int m, int p) {
        if (m == 0 || m == 1 || p == 0 || p == 1) {
            return 1;
        } else {
            return fatorial(m) / (fatorial(m-p) * (fatorial(p)));
        }
    }
    public static void main(String[] args) {
        //System.out.println(arranjoRecursivo(8,2));
        System.out.println(combinacaoRecursivo(11, 4) * combinacaoRecursivo(7,3));
    }
}