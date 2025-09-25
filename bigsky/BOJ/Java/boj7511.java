// BOJ7511(D3): 소셜 네트워킹 어플리케이션
import java.util.*;
import java.io.*;

public class boj7511 {
    static int t, n, k, m;
    static int[] root = new int[1000001];  // 유저 수 최대 10^6

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();

        t = Integer.parseInt(br.readLine());

        for (int tc = 1; tc <= t; tc++) {
            n = Integer.parseInt(br.readLine());
            k = Integer.parseInt(br.readLine());

            // 유니온 파인드 초기화
            for (int i = 0; i < n; i++) {
                root[i] = i;
            }

            // k개의 관계 처리
            for (int i = 0; i < k; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                union(a, b);
            }

            m = Integer.parseInt(br.readLine());

            // 시나리오 출력 저장
            sb.append("Scenario ").append(tc).append(":\n");

            // k개의 쿼리 처리
            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int u = Integer.parseInt(st.nextToken());
                int v = Integer.parseInt(st.nextToken());

                if (find(u) == find(v)) {
                    sb.append("1\n");
                } else {
                    sb.append("0\n");
                }
            }
            sb.append("\n");
        }

        System.out.println(sb);
        br.close();
    }

    static int find(int x) {
        if (x == root[x]) {
            return x;
        }
        return root[x] = find(root[x]);
    }

    static void union(int x, int y) {
        x = find(x);
        y = find(y);

        if (x != y) {
            if (x < y) {
                root[y] = x;
            } else {
                root[x] = y;
            }
        }
    }
}
