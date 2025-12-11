// BOJ1309(D2): 동물원
#include <iostream>
#include <vector>

using namespace std;

int dp[100001][3];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	dp[1][0] = 1;  // 첫 줄에 아무것도 안 놓는 경우
	dp[1][1] = 1;  // 첫 줄에 왼쪽에 놓는 경우
	dp[1][2] = 1;  // 첫 줄에 오른쪽에 놓는 경우

	for (int i = 2; i <= N; i++) {
		// 현재 줄에 아무것도 안 놓을 때: 윗 줄 상태 상관 없음
		dp[i][0] = (dp[i - 1][0] + dp[i - 1][1] + dp[i - 1][2]) % 9901;
		// 현재 줄에 왼쪽에 놓을 때: 윗줄이 없거나, 오른쪽에 있어야 함
		dp[i][1] = (dp[i - 1][0] + dp[i - 1][2]) % 9901;
		// 현재 줄에 오른쪽에 놓을 때: 윗줄이 없거나, 왼쪽에 있어야 함
		dp[i][2] = (dp[i - 1][0] + dp[i - 1][1]) % 9901;
	}

	int result = (dp[N][0] + dp[N][1] + dp[N][2]) % 9901;

	cout << result << "\n";

	return 0;
}