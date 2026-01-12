// BOJ 2589. 보물섬 / G5
#include <iostream>
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
	int N, M;
	cin >> N >> M;

	vector<vector<char>> trmap(N, vector<char>(M, 'm'));
	vector<pair<int, int>> Laxis;

	for (int i = 0; i < N; i++) {
		string m;
		cin >> m;

		for (int j = 0; j < M; j++) {
			trmap[i][j] = m[j];
			if (trmap[i][j] == 'L') Laxis.push_back({ i, j });
		}
	}

	vector<int> max_vlst;

	for (int i = 0; i < Laxis.size(); i++) {
		queue<pair<int, int>> q;
		vector<vector<int>> visited(N, vector<int>(M, -1));
		int dy[4] = { 1, -1, 0, 0 };
		int dx[4] = { 0, 0, 1, -1 };
		
        q.push(Laxis[i]);

		int y = q.front().first;
		int x = q.front().second;
		
        visited[y][x] = 0;
		
        int max_v = 0;
		
		while (!q.empty()) {
			int y = q.front().first;
			int x = q.front().second;
			q.pop();

			for (int d = 0; d < 4; d++) {
				int ny = y + dy[d];
				int nx = x + dx[d];

				if (0 <= ny && ny < N && 0 <= nx && nx < M && visited[ny][nx] == -1 && trmap[ny][nx] == 'L') {
					visited[ny][nx] = visited[y][x] + 1;
					max_v = max(max_v, visited[ny][nx]);
					q.push({ ny, nx });
				}
			}
		}
		max_vlst.push_back(max_v);
	}
	cout << *max_element(max_vlst.begin(), max_vlst.end()) << "\n";
}

/*
모든 L의 좌표를 찾아서 bfs진행해서 제일 큰 값을 배열에 넣고
그 중 제일 큰 값 출력
완전탐색
*/