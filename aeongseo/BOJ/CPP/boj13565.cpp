/*** 13565. 침투 ***/

#include<iostream>
#include<vector>
#include<queue>
#include<string>
using namespace std;

vector<vector<int>> arr;
vector<vector<int>> visited;
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };
int M, N;

void bfs();

int main() {
	bool flag = false;	// 안쪽에 도달했는지 확인을 위한 플래그
	cin >> N >> M;
	arr.assign(N, vector<int>(M, 0));
	visited.assign(N, vector<int>(M, 0));

	for (int i = 0; i < N; i++) {
		string line;
		cin >> line;
		for (int j = 0; j < M; j++) {
			arr[i][j] = line[j] - '0';
		}
	}

	bfs();	// bfs 실행

	for (int k = 0; k < M; k++) {	// 끝 줄의 어느 한 지점이라도 방문한 적이 있으면 flag true
		if (visited[N - 1][k]) {
			flag = true;
			break;
		}
	}

	if (flag) cout << "YES";
	else cout << "NO";

	return 0;
}

void bfs() {
	queue<pair<int, int>> q;

	for (int j = 0; j < M; j++) {	// 시작 지점 모두 큐에 삽입
		if (!arr[0][j]) {
			q.push({ 0, j });
			visited[0][j] = 1;
		}
	}

	while (!q.empty()) {
		int ti = q.front().first;
		int tj = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ni = ti + di[i];
			int nj = tj + dj[i];
			if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
			if (visited[ni][nj] || arr[ni][nj]) continue;
			q.push({ ni, nj });
			visited[ni][nj] = 1;
		}
	}
}
