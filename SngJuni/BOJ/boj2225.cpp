#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, K;
    cin >> N >> K;

    vector<vector<int>> dp(N + 1, vector<int>(K + 1, 0));

    for (int i = 0; i <= K; i++) {  // 1을 i개의 자연수로 분해하는 방법은 i가지
        dp[1][i] = i;
    }

    // dp 배열 채우기
    for (int i = 2; i <= N; i++) {  
        for (int j = 1; j <= K; j++) {
            // (i - 1)을 j개의 자연수로 분해하는 방법 + i를 (j - 1)개의 자연수로 분해하는 방법 = i를 j개의 자연수로 분해하는 방법
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % 1000000000;
        }
    }

    cout << dp[N][K] << '\n';  // N을 K개의 자연수로 분해하는 방법의 수

    return 0;
}