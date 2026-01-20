// BOJ 2667. 단지번호붙이기 / S1
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	int N;
	cin >> N;

	vector<vector<int>> danji(N, vector<int>(N));
	vector<pair<int, int>> axis;
	for (int i = 0; i < N; i++) {
		string s;
		cin >> s;
		for (int j = 0; j < N; j++) {
			danji[i][j] = s[j] - '0';
			if (danji[i][j] == 1) {
				axis.push_back({ i, j });
			}
		}
	}

	vector<vector<int>> visited(N, vector<int>(N, 0));
	int di[4] = { 1, -1, 0, 0 };
	int dj[4] = { 0, 0, 1, -1 };

	int danji_num = 0;
	vector<int> danji_cnt;
	for (int i = 0; i < axis.size(); i++) {
		int x = axis[i].first;
		int y = axis[i].second;

		if (visited[x][y] == 1) continue;
		
		queue<pair<int, int>> q;
		q.push({ x, y });
		visited[x][y] = 1;
		int cnt = 1;

		while (!q.empty()) {
			int x = q.front().first;
			int y = q.front().second;
			q.pop();

			for (int d = 0; d < 4; d++) {
				int nx = x + di[d];
				int ny = y + dj[d];
				if (0 <= nx && nx < N && 0 <= ny && ny < N && visited[nx][ny] == 0 && danji[nx][ny] == 1) {
					q.push({ nx, ny });
					visited[nx][ny] = 1;
					cnt++;
				}
			}
		}
		danji_num++;
		danji_cnt.push_back(cnt);
	}
	sort(danji_cnt.begin(), danji_cnt.end());
	cout << danji_num << "\n";
	for (int n : danji_cnt) {
		cout << n << "\n";
	}
}

/*
모든 1의 좌표를 벡터에 집어 넣고
반복문을 통해 1의 좌표에 방문했다면 넘어가고 방문하지 않았다면 큐에 집어넣고 BFS를 통해 단지 내 집의 수를 세고 벡터에 넣음
이후 while 문이 종료 될때마다 단지의 수를 추가해줌
최종 반복문이 종료되면 총 단지수와 단지 내 집 수를 정렬한 백터를 출력함
*/