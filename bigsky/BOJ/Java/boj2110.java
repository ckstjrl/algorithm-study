// BOJ2110(D3): 공유기 설치

import java.io.*;
import java.util.*;

public class boj2110 {
    public static int[] house;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        house = new int[N];
        for (int i = 0; i < N; i++) {
            house[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(house);

        int low = 1; // 최소 거리가 가질 수 있는 최솟값
        int high = house[N - 1] - house[0] + 1; // 최소 거리가 가질 수 있는 최댓값

        while (low < high) {
            int mid = (low + high) / 2;
            if (canInstall(mid) < M) {
                high = mid;
            } else {
                low = mid + 1;
            }
        }
        System.out.println(low - 1);
    }

    public static int canInstall(int distance) {
        int count = 1;
        int lastLocate = house[0];

        for (int i = 1; i < house.length; i++) {
            int locate = house[i];
            if (locate - lastLocate >= distance) {
                count++;
                lastLocate = locate;
            }
        }
        return count;
    }
}
