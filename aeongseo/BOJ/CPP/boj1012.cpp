/*** 1012. 유기농 배추 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

void bfs(int si, int sj);

vector<vector<int>> field;
vector<vector<bool>> visited;
int M, N, K;

int di[4] = { -1, 1, 0, 0 };
int dj[4] = { 0, 0, -1, 1 };

int main() {
	//freopen("input.txt", "r", stdin);

	int T;
	cin >> T;

	for (int tc = 1; tc < T + 1; tc++) {
		cin >> M >> N >> K;

		field.assign(N, vector<int>(M, 0));
		visited.assign(N, vector<bool>(M, false));

		int cnt = 0;
		
		for (int i = 0; i < K; i++) {
			int X, Y;
			cin >> X >> Y;
			field[Y][X] = 1;
		}

		for (int i = 0; i < N; i ++ ) {
			for (int j = 0; j < M; j++) {
				if (field[i][j] == 1 && !visited[i][j]) {
					bfs(i, j);
					cnt++;
				}
			}
		}

		cout << cnt << '\n';
	}

	return 0;
}

void bfs(int si, int sj) {
	queue<pair<int, int>> q;

	visited[si][sj] = true;
	q.emplace(si, sj);

	while (!q.empty()) {
		int ti, tj;
		ti = q.front().first;
		tj = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ni = ti + di[i];
			int nj = tj + dj[i];
			if (ni < 0 || ni >= N || nj < 0 || nj >= M || visited[ni][nj] || !field[ni][nj]) {
				continue;
			}
			visited[ni][nj] = true;
			q.emplace(ni, nj);
		}
	}
}