/*** 1926. 그림 ***/

#include<iostream>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std;

void bfs(int si, int sj);

vector<vector<int>> visited;
vector<vector<int>> arr;
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };
int max_size = 0;
int n, m;

int main() {
	int cnt = 0;	// 그림 개수
	cin >> n >> m;
	visited.assign(n, vector<int>(m, 0));
	arr.assign(n, vector<int>(m, 0));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
		}
	}

	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			if (!visited[i][j] && arr[i][j]) {	// 방문한 적 없고 그림이라면 개수 증가 및 bfs 수행
				cnt++;
				bfs(i, j);
			}
		}
	}

	cout << cnt << '\n' << max_size;

	return 0;
}

void bfs(int si, int sj) {
	queue<pair<int, int>> q;
	int size = 1;	// 시작 위치부터 사이즈 시작하므로 1로 초기화
	q.push({ si, sj });
	visited[si][sj] = 1;

	while (!q.empty()) {
		int ti = q.front().first;
		int tj = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ni = ti + di[i];
			int nj = tj + dj[i];
			if (ni < 0 || ni >= n || nj < 0 || nj >= m) continue;
			if (visited[ni][nj] || !arr[ni][nj]) continue;
			q.push({ ni, nj });
			visited[ni][nj] = visited[ti][tj] + 1;
			size++;	// 그림 사이즈 증가
		}
	}
	max_size = max(max_size, size);	// 사이즈 최대값 갱신
}