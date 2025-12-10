/*** 1197. 최소 스패닝 트리 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int V, E;
long long maxW = 0;
vector<pair<int, int>> edge[10001];
bool visited[10001];

void prim(int start);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> V >> E;
	for (int i = 0; i < E; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		// MST는 양방향
		edge[u].push_back({ w, v });
		edge[v].push_back({ w, u });
	}

	prim(1);

	cout << maxW;

	return 0;
}

void prim(int start) {
	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
	pq.push({ 0, start });

	while (!pq.empty()) {
		auto [w, n] = pq.top();
		pq.pop();

		if (visited[n]) continue;
		visited[n] = true;
		maxW += w;

		for (int i = 0; i < edge[n].size(); i++) { // 현재 정점에서 다음 정점까지의 정보를 우선순위큐에 삽입
			auto [nextw, nextn] = edge[n][i];
			pq.push({ nextw, nextn });
		}
	}
}