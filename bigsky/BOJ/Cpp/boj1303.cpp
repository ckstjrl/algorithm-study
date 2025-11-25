#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int dx[4] = { -1, 0, 1, 0 };
int dy[4] = { 0, -1, 0, 1 };

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N, M;
	cin >> N >> M;

	vector<vector<char>> war(M, vector<char>(N));
	vector<vector<bool>> visited(M, vector<bool>(N, false));

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			cin >> war[i][j];
		}
	}

	int w_power = 0;
	int b_power = 0;

	for (int i = 0; i < M; i++) {
		for (int j = 0; j < N; j++) {
			if (visited[i][j]) continue;

			char team = war[i][j];
			int cnt = 0;

			queue<pair<int, int>> q;
			q.push({ i, j });
			visited[i][j] = true;
			cnt = 1;

			while (!q.empty()) {
				int x = q.front().first;
				int y = q.front().second;
				q.pop();

				for (int d = 0; d < 4; d++) {
					int nx = x + dx[d];
					int ny = y + dy[d];

					if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
					if (visited[nx][ny] || war[nx][ny] != team) continue;

					visited[nx][ny] = true;
					q.push({ nx, ny });
					cnt++;
				}
			}

			if (team == 'W') w_power += cnt * cnt;
			else b_power += cnt * cnt;
		}
	}

	cout << w_power << " " << b_power << "\n";
	return 0;
}