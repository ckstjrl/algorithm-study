/*** 1520. 내리막 길 ***/

/*
	dp는 해당 칸에서 도착지까지 갈 수 있는 경로의 수 저장 (-1로 초기화)
	경로의 수는 dfs로 구함
*/

#include<iostream>
using namespace std;

int M, N;
int map[500][500];
int dp[500][500];

int dx[4] = { 0, 1, 0, -1 };
int dy[4] = { 1, 0, -1, 0 };

int dfs(int x, int y);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> M >> N;

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			dp[i][j] = -1; // 방문 여부 체크 위해 -1로 초기화
		}
	}
	
	cout << dfs(0, 0);

	return 0;
}

int dfs(int x, int y) {
	if (x == M - 1 && y == N - 1) return 1; // 도착지에 도착하면 경로 1 증가

	if (dp[x][y] != -1) return dp[x][y]; // 방문한 적 있으면 해당 칸의 경로의 수 반환

	dp[x][y] = 0; // 방문한 적 없다면 경로의 수를 0으로 초기화

	for (int d = 0; d < 4; d++) {
		int nx = x + dx[d];
		int ny = y + dy[d];

		if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
		if (map[nx][ny] < map[x][y]) dp[x][y] += dfs(nx, ny); // 상하좌우 중에 현재 위치보다 낮은 값을 갖고 있으면 재귀 실행
	}

	return dp[x][y];
}