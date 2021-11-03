public class OperacoesAlgebricas {
    public static int soma(int x, int y){
    return x + y;
}

public static  int produto(int x, int y) { 
    return x * y; 
    }

    public static  int pot(int x, int y){
    if (y== 0)
        return 1;
    else
        return x * pot(x, y - 1);
}
    public static void main(String[] args) {
        
    }
}
