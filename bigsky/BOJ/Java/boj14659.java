// BOJ14659(D1): 한조서열정리하고옴ㅋㅋ
import java.io.*;
import java.util.*;

public class boj14659 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        int[] heights = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            heights[i] = Integer.parseInt(st.nextToken());
        }

        int archer = heights[0];
        int count = 0;
        int maxCount = 0;

        for (int i = 1; i < N; i++) {
            if (heights[i] < archer) {
                count++;
            }
            else {
                maxCount = Math.max(maxCount, count);
                archer = heights[i];
                count = 0;
            }
        }

        maxCount = Math.max(maxCount, count);

        System.out.println(maxCount);
    }
}
