// BOJ1547(D1): 공
import java.util.Scanner;

public class boj1547 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int ball = 1; // 공이 있는 위치
        int M = sc.nextInt();
        for (int i = 0; i < M; i++) {
            int cup1 = sc.nextInt();
            int cup2 = sc.nextInt();

            // cup1에 공이 있다면 cup2로 옮기고, cup2에 공이 있다면 cup1로 옮김
            if (cup1 == ball) {
                ball = cup2;
            } else if (cup2 == ball) {
                ball = cup1;
            }
        }

        System.out.println(ball);
        sc.close();
    }
}
