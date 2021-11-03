public class BinomioNewton {
    public static int fatorial(int n) {
        if (n == 0 || n == 1) {
            return 1;
        } else {
            return n * fatorial(n - 1);
        }
    }

    public static double calculaBinomial(int n, int p) {
        return fatorial(n) / (fatorial(p) * fatorial(n - p));
    }
    public static void main(String[] args) {
        System.out.println(calculaBinomial(10, 4));
    }
}
