/*** 1325. 효율적인 해킹 ***/

#include<iostream>
#include<vector>
#include<queue>

using namespace std;

int N, M, max_cnt = 0;
vector<int> graph[10001];
vector<int> ans;

int bfs(int start);

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;

	for (int i = 0; i < M; i++) {
		int a, b;
		cin >> a >> b;
		graph[b].push_back(a);
	}

	for (int i = 1; i < N + 1; i++) {
		int cnt = bfs(i); // 각각의 컴퓨터에서 해킹 시작
		if (cnt == max_cnt) {	// 해킹 컴퓨터 수가 최대값과 같으면 컴퓨터 번호만 저장
			ans.push_back(i);
		}
		else if (cnt > max_cnt) { // 최대값보다 크면 배열 초기화 후 번호 저장, 최대값 갱신
			ans.clear();
			ans.push_back(i);
			max_cnt = cnt;
		}
	}

	for (int i = 0; i < ans.size(); i++) {
		cout << ans[i] << ' ';
	}

	return 0;
}

int bfs(int start) {
	queue<int> q;
	vector<bool> visited(N + 1, false);
	int cnt = 0; // 해킹된 컴퓨터 수
	q.push(start);
	visited[start] = 1;

	while (!q.empty()) {
		int cur = q.front(); // 현재 해킹된 컴퓨터
		q.pop();
		cnt++; // 수 증가

		for (auto& next : graph[cur]) {
			if (visited[next]) continue;
			visited[next] = true; // 다음 컴퓨터를 신뢰하면 방문
			q.push(next); // 해킹 컴퓨터에 포함
		}
	}
	return cnt;
}