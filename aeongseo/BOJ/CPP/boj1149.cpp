/*** 1149. RGB거리 ***/


// 비용 빨 초 파 순
// dp table -> dp[i][c] : i번째 집을 c로 칠했을 때 최소 비용
// 각 색의 비용과 이전 집의 다른 색 중 최소 비용을 선택해서 합함

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<vector<int>> paint, dp;

int main() {
	int N;
	cin >> N;

	paint.assign(N, vector<int>(3, 0));
	dp.assign(N, vector<int>(3, 0));

	for (int i = 0; i < N; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		paint[i][0] = a;
		paint[i][1] = b;
		paint[i][2] = c;
	}

	dp[0][0] = paint[0][0];
	dp[0][1] = paint[0][1];
	dp[0][2] = paint[0][2];
	for (int i = 1; i < N; i++) {
		dp[i][0] = paint[i][0] + min(dp[i - 1][1], dp[i - 1][2]);
		dp[i][1] = paint[i][1] + min(dp[i - 1][0], dp[i - 1][2]);
		dp[i][2] = paint[i][2] + min(dp[i - 1][0], dp[i - 1][1]);
	}

	int min_cost = min(dp[N - 1][0], dp[N - 1][1]);

	cout << min(min_cost, dp[N - 1][2]);

	return 0;
}