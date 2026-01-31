// BOJ 5972. 택배 배송 / G5
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int INF = 210000000;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N, M;
	cin >> N >> M;

	vector<vector<pair<int, int>>> adj(N + 1);
	vector<int> dist(N + 1, INF);

	for (int i = 0; i < M; i++) {
		int a, b, c;
		cin >> a >> b >> c;
		adj[a].push_back({ b, c });
		adj[b].push_back({ a, c });
	}

	int start = 1;
	dist[start] = 0;

	priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

	pq.push({ 0, start });

	while (!pq.empty()) {
		int cost = pq.top().first;
		int cur = pq.top().second;
		pq.pop();

		if (dist[cur] < cost) continue;

		for (int i = 0; i < adj[cur].size(); i++) {
			int nxt = adj[cur][i].first;
			int w = adj[cur][i].second;

			int nxtcost = cost + w;
			if (dist[nxt] > nxtcost) {
				dist[nxt] = nxtcost;
				pq.push({ nxtcost, nxt });
			}
		}
	}
	cout << dist[N] << "\n";
}

/*
다익스트라 사용
*/