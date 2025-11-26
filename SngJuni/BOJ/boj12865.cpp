#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N, K;
    cin >> N >> K;
    
    vector<pair<int, int>> arr(N + 1);  // 물건 정보 배열 : (W, V)
    for (int i = 1; i <= N; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    vector<vector<int>> dp(N + 1, vector<int>(K + 1, 0));
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= K; j++) {
            dp[i][j] = dp[i - 1][j];  // i번째 물건을 안넣는 경우
            if (j >= arr[i].first) {  // i번째 물건을 넣을 수 있으면
                dp[i][j] = max(dp[i][j], dp[i - 1][j - arr[i].first] + arr[i].second);  // i번째 물건을 넣는 경우와 비교
            }
        }
    }

    cout << dp[N][K] << '\n';
    
    return 0;
}