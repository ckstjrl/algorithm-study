#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화
    cin.tie(NULL);

    int n;
    cin >> n;

    int dp[1000001] = {0,};  // dp를 위한 정적 배열
    dp[1] = 0;
    dp[2] = 1;
    dp[3] = 1;
    
    for (int i = 4; i <= n; i++) {
        dp[i] = dp[i - 1] + 1;  // 1을 빼는 연산을 사용하는 경우

        if (!(i % 2)) dp[i] = min(dp[i], dp[(i / 2)] + 1);  // 2로 나누는 연산을 사용하는 경우와 1을 빼는 연산 중 더 작은 횟수
        if (!(i % 3)) dp[i] = min(dp[i], dp[(i / 3)] + 1);  // 3으로 나누는 연산을 사용하는 경우와 1을 빼는 연산 중 더 작은 횟수
    }

    cout << dp[n] << '\n';

    return 0;
}