//BOJ17204(D2): 죽음의 게임
import java.io.*;
import java.util.*;

public class boj17204 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken()); // 사람 수
        int K = Integer.parseInt(st.nextToken()); // 보성이 번호

        int[] next = new int[N]; // 각 사람이 지목하는 사람
        for (int i = 0; i < N; i++) {
            next[i] = Integer.parseInt(br.readLine());
        }

        int current = 0; // 0번부터 시작
        int count = 0; // 지목 횟수
        boolean[] visited = new boolean[N]; // 방문 체크
        visited[0] = true;

        while (true) {
            current = next[current]; // 다음 사람으로 이동
            count++;

            if (current == K) {
                // K까지 도달했다면 카운트 출력
                System.out.println(count);
                break;
            }

            if (visited[current]) {
                // 이미 방문했던 곳으로 돌아왔다면 -1 출력
                System.out.println(-1);
                break;
            }

            visited[current] = true;
        }
    }
}
