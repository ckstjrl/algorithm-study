//BOJ2644(D2): 촌수계산
import java.io.*;
import java.util.*;

public class boj2644 {
    static  List<Integer>[] relation;
    static boolean[] checked;
    static int result = -1;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        relation = new ArrayList[n+1];
        checked = new boolean[n+1];
        for (int i = 0; i < n+1; i++) {
            relation[i] = new ArrayList<>();
        }

        StringTokenizer st = new StringTokenizer(br.readLine());

        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());

        int l = Integer.parseInt(br.readLine());
        for (int i = 0; i < l; i++) {
            st = new StringTokenizer(br.readLine());
            int p = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            relation[p].add(c);
            relation[c].add(p);
        }

        dfs(x, y, 0);
        System.out.println(result);
    }

    static void dfs(int start, int end, int cnt) {
        if (start == end) {
            result = cnt;
            return;
        }

        checked[start] = true;
        for (int i = 0; i < relation[start].size(); i++) {
            int next = relation[start].get(i);
            if (!checked[next]) {
                dfs(next, end, cnt + 1);
                if (result != -1) return;
            }
        }
    }
}
