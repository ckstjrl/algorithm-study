/*** 2225. 합분해 ***/

// 1트
// dp[K][N] 배열을 만든다
// dp 배열에 값을 다 넣는다
// dp를 순회하며 dp[k-1][n] + dp[k][n-1] = N인 것을 카운트 한다

// 2트
// dp[1][N]의 모든 값은 1
// 이후 dp[k][n] = dp[k-1][n] + dp[k][n-1]
// dp[K][N]의 값을 출력

#include<iostream>
#include<vector>
using namespace std;

int main() {
	int N, K;
	cin >> N >> K;

	vector<vector<int>> dp(K+1, vector<int>(N+1, 1));

	for (int i = 2; i < K+1; i++) {
		for (int j = 1; j < N+1; j++) {
			dp[i][j] = (dp[i - 1][j] + dp[i][j-1]) % 1000000000;	// 왼쪽 값과 오른쪽 값의 합이 현재의 경우의 수
		}
	}

	cout << dp[K][N];

	return 0;
}