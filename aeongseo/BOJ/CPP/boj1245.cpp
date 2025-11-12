/*** 1245. 농장 관리 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

void bfs(int si, int sj);

vector<vector<int>> mountain, visited;
int di[8] = { 0, 0, 1, 1, 1, -1, -1, -1 };	// 8방향 확인
int dj[8] = { 1, -1, 0, 1, -1, 0, 1, -1 };
int N, M, peak = 0;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;

	mountain.assign(N, vector<int>(M, 0));
	visited.assign(N, vector<int>(M, 0));	// 같은 높이의 봉우리 집합 다시 방문하지 않기 위해 visited 사용

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> mountain[i][j];
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (!visited[i][j]) bfs(i, j);	// 방문한 적 없으면 bfs
		}
	}

	cout << peak;

	return 0;
}

void bfs(int si, int sj) {
	bool is_peak = true;	// 봉우리가 맞는지 확인하기 위한 플래그
	queue<pair<int, int>> q;	// 같은 높이의 봉우리 좌표
	q.push({ si, sj });
	visited[si][sj] = 1;

	while (!q.empty()) {
		auto[ti, tj] = q.front();
		q.pop();

		for (int d = 0; d < 8; d++) {
			int ni = ti + di[d];
			int nj = tj + dj[d];

			if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
			if (mountain[ni][nj] == mountain[ti][tj] && !visited[ni][nj]) {	// 봉우리 높이가 같고 방문한 적 없으면 q에 추가
				q.push({ ni, nj });
				visited[ni][nj] = 1;
			}
			else if (mountain[ni][nj] > mountain[ti][tj]) is_peak = false;	// 봉우리보다 인접 격자의 높이가 더 높으면 봉우리 아님
		}
	}
	if (is_peak) peak++;
}