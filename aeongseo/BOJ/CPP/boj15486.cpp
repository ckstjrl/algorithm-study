/*** 15486. 퇴사 2 ***/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

// dp[day] = 최대 수익
// 마지막 퇴사날의 수익 dp[N+1] 출력 
// 상담 안하면 어제와 오늘 값 중 최대값 선택
// 상담 하면 상담완료날에 저장된 값과 오늘 값에서 보상금액을 더한 값 중 최대값 선택

int main() {
	int N;
	cin >> N;

	vector<int> T(N + 1, 0), P(N + 1, 0), dp(N + 2, 0);

	for (int i = 1; i < N + 1; i++) {
		cin >> T[i] >> P[i];
	}

	for (int i = 1; i < N + 1; i++) {
		// 상담 안하면
		dp[i] = max(dp[i], dp[i - 1]);

		// 상담 하면
		if (i + T[i] > N + 1) continue;
		dp[i + T[i]] = max(dp[i + T[i]], dp[i] + P[i]);
	}

	dp[N + 1] = max(dp[N + 1], dp[N]); // 마지막 날 최대값 선택

	cout << dp[N + 1];

	return 0;
}