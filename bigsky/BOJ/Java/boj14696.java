//BOJ14696(D1): 딱지놀이
import java.util.Scanner;

public class boj14696 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        for (int round = 0; round < N; round++) {
            int[] count = new int[5];
            
            // A의 카드 기록(더하기)
            int a = sc.nextInt();
            for (int i = 0; i < a; i++) {
                int card = sc.nextInt();
                count[card]++;
            }

            // B의 카드 기록(빼기)
            int b = sc.nextInt();
            for (int i = 0; i < b; i++) {
                int card = sc.nextInt();
                count[card]--;
            }

            // 높은 등급부터 비교
            char result = 'D';
            for (int i = 4; i >= 1; i--) {
                if (count[i] > 0) {
                    result = 'A';
                    break;
                } else if (count[i] < 0) {
                    result = 'B';
                    break;
                }
            }

            System.out.println(result);
        }

        sc.close();
    }
}
