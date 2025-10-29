import java.util.Scanner;

public class boj30456 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int L = sc.nextInt();

        System.out.println("1".repeat(L - 1) + String.valueOf(N));

        sc.close();
    }
}
