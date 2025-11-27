/*** 1707. 이분 그래프 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

void bfs(int start);

vector<vector<int>> graph;
vector<bool> visited;
vector<int> check;
bool flag = true;	// 이분 그래프 판별을 위한 플래그

int main() {
	int K;
	cin >> K;
	for (int tc = 1; tc < K + 1; tc++) {
		int V, E, start;
		cin >> V >> E;

		// 테스트케이스 새로 실행될 때마다 크기 재정의, 초기화
		graph.clear();
		graph.resize(V + 1);
		visited.assign(V + 1, false);
		check.assign(V + 1, 0);

		for (int i = 0; i < E; i++) {
			int u, v;
			cin >> u >> v;
			if (i == 0) start = u;
			graph[u].push_back(v);	// 양방향으로 인접리스트 저장
			graph[v].push_back(u);
		}

		for (int j = 1; j < V + 1; j++) {
			if (!visited[j]) bfs(j);	// 방문한 기록이 없으면 bfs 수행
			if (!flag) break;
		}
		if (flag) cout << "YES" << '\n';
		else cout << "NO" << '\n';
		flag = true;    // 다음 테스트 케이스에서 플래스 사용을 위해 초기화
	}


	return 0;
}

void bfs(int start) {
	queue<int> q;
	q.push(start);
	visited[start] = true;
	check[start] = 1;

	while (!q.empty()) {
		int t = q.front();
		q.pop();
		
		for (const auto& n : graph[t]) {
			// 인접 정점을 방문한 적 없으면 현재 정점과 다른 숫자 저장
			if (!visited[n]) {
				visited[n] = true;
				q.push(n);
				if (check[t] == 1) check[n] = 2;
				else check[n] = 1;
			}
			// 모두 방문했는데 색이 같으면 이분 그래프 아님
			else if (visited[t] && visited[n]) {
				if (check[t] == check[n]) {
					flag = false;
					return;
				}
			}
		}
	}
}