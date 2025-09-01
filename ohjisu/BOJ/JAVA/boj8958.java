/*

# [Bronze II] OX퀴즈 - 8958 

[문제 링크](https://www.acmicpc.net/problem/8958) 

### 성능 요약

메모리: 14292 KB, 시간: 104 ms

### 분류

구현, 문자열

### 제출 일자

2025년 8월 26일 21:34:02

### 문제 설명

"OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.

"OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.

OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

### 입력 

 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.

### 출력 

 각 테스트 케이스마다 점수를 출력한다.


*/

import java.io.*; /* IOException 처리해야 함 */

public class boj8958 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); /* sout보다 빠르다고 함 */
        int n = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < n ; i++) {
            String oxString = br.readLine();
            int len_ox = oxString.length();
            int result = 0;
            int j = 0; // idx 돌리는 j
            int k = 1; // 가중치 업데이트하는 k
            while (j < len_ox) {
                if ( oxString.charAt(j) == 'O') { /* charAt을 써야 한다고 함 */
                    result += k;
                    k += 1;
                } else {
                    k = 1;
                }
                j += 1;
            }
            System.out.println(result);

        }
    }
}