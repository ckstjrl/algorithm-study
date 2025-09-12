#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    string s1, s2;  // 문자열 2개
    cin >> s1 >> s2;

    int n = s1.size();  // 각 문자열의 길이
    int m = s2.size();
    vector<vector<int>> dp(n + 1, vector<int>(m + 1, 0));  // (문자열 길이 + 1) * (문자열 길이 + 1) 만큼의 2차원 가변배열 0으로 초기화
    for (int i = 1; i <= n; i++) {  // dp 배열의 맨 윗줄과 맨 왼쪽줄은 0으로 두고 (1, 1) 인덱스부터 (n, m)까지 순회
        for (int j = 1; j <= m; j++) {
            if (s1[i - 1] == s2[j - 1]) {  // 같은 문자면 테이블에서 왼쪽 대각선 윗값에 1 증가해서 저장
                dp[i][j] = dp[i - 1][j - 1] + 1;
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);  // 다른 문자면 바로 왼쪽과 윗값 중 더 큰 값 저장
            }
        }
    }

    cout << dp[n][m] << '\n';  // 결과 출력

    return 0;
}