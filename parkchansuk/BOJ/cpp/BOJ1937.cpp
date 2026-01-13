// BOJ 1937. 욕심쟁이 판다 / G3
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N;
vector<vector<int>> dp;
vector<vector<int>> bamboo;
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

int dfs(int x, int y) {
	if (dp[x][y] != 0) return dp[x][y];

	int best = 1;

	for (int d = 0; d < 4; d++) {
		int nx = x + dx[d];
		int ny = y + dy[d];

		if (0 <= nx && nx < N && 0 <= ny && ny < N && bamboo[x][y] < bamboo[nx][ny]) {
			best = max(best, 1 + dfs(nx, ny));
		}
	}

	return dp[x][y] = best;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	cin >> N;

	bamboo.assign(N, vector<int>(N));
	dp.assign(N, vector<int>(N));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> bamboo[i][j];
		}
	}
	int ans = 0;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			ans = max(ans, dfs(i, j));
		}
	}
	cout << ans << "\n";
}

/*
DP + DFS 합쳐서 활용
x, y에서 시작했을 때의 최대경로를 구하기 위해 DFS 활용,
같은 칸에서 시작하는 경우가 반복되어 결과저장 DP를 함께 활용
*/