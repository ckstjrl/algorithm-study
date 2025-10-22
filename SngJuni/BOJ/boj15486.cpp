#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<int> T(N + 2);
    vector<int> P(N + 2);
    for (int i = 1; i <= N; i++) {
        cin >> T[i] >> P[i];
    }

    vector<int> dp(N + 2);  // 1일부터 시작하고 i일까지의 최대 수익
    for (int i = 1; i <= N; i++) {
        // i일에 아무것도 하지 않는 경우
        dp[i] = max(dp[i], dp[i - 1]);  // i일에 상담을 하지 않은 수익과 그 전날까지의 최대 수익 중 최댓값

        // i일에 상담 시작하는 경우 -> 상담이 끝나는 날에 최댓값 반영
        int next = i + T[i];  // i일의 상담이 끝나는 날의 인덱스
        if (next <= N + 1) {
            dp[next] = max(dp[next], dp[i] + P[i]);  // 최댓값 갱신
        }
    }

    dp[N + 1] = max(dp[N + 1], dp[N]);  // 마지막 날 최대 수익 갱신

    cout << dp[N + 1] << '\n';

    return 0;
}