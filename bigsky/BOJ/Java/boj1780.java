// BOJ1780(D2): 종이의 개수
import java.io.*;
import java.util.*;

public class boj1780{
    static int[][] paper;
    static int[] count = new int[3]; // -1, 0, 1의 개수

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        paper = new int[N][N];

        for (int i = 0; i < N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                paper[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        divide(0, 0, N);

        System.out.println(count[0]); // -1의 개수
        System.out.println(count[1]); // 0의 개수
        System.out.println(count[2]); // 1의 개수
    }

    static void divide(int row, int col, int size) {
        if (isSame(row, col, size)) {
            count[paper[row][col] + 1]++;
            return;
        }

        int newSize = size / 3;
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                divide(row + i * newSize, col + j * newSize, newSize);
            }
        }
    }

    static boolean isSame(int row, int col, int size) {
        int value = paper[row][col];
        for (int i = row; i < row + size; i++) {
            for (int j = col; j < col + size; j++) {
                if (paper[i][j] != value) {
                    return false;
                }
            }
        }
        return true;
    }
}