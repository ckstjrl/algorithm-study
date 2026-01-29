// BOJ 4485. 녹색 옷 입은 애가 젤다지? / G4
#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;
int dx[4] = { 1, -1, 0, 0 };
int dy[4] = { 0, 0, 1, -1 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	
	int t = 0;
	while (1) {
		int N;
		cin >> N;

		if (N == 0) break;

		vector<vector<int>> cave(N, vector<int>(N, 0));
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				cin >> cave[i][j];
			}
		}

		int ans = 210000000;
		vector<vector<int>> dist(N, vector<int>(N, ans));
		priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> q;
		dist[0][0] = cave[0][0];
		q.push({ cave[0][0], 0, 0 });

		while (!q.empty()) {
			int cost = get<0>(q.top());
			int x = get<1>(q.top());
			int y = get<2>(q.top());
			q.pop();

			if (cost != dist[x][y]) continue;

			if (x == N - 1 && y == N - 1) break;

			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];

				if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

				int ncost = cost + cave[nx][ny];
				if (ncost < dist[nx][ny]) {
					dist[nx][ny] = ncost;
					q.push({ ncost, nx, ny });
				}
			}
		}
		t++;
		cout << "Problem " << t << ": " << dist[N-1][N-1] << "\n";
	}
}
/*
다익스트라 활용
*/