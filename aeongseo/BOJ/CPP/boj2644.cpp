/*** 2644. 촌수계산 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int bfs(int start);

vector<vector<int>> graph;
vector<int> visited;
int n, a, b, m;

int main() {
	cin >> n >> a >> b >> m;

	graph.assign(n + 1, {});
	visited.assign(n + 1, 0);

	for (int i = 0; i < m; i++) {
		int x, y;
		cin >> x >> y;
		graph[x].push_back(y);
		graph[y].push_back(x);
	}

	int cnt = bfs(a);

	cout << cnt;


	return 0;
}


int bfs(int start) {
	queue<int> q;
	q.push(start);
	visited[start] = 1;

	while (!q.empty()) {
		int t = q.front();
		q.pop();

		if (t == b) return visited[t] - 1;

		for (const auto& x : graph[t]) {
			
			if (!visited[x]) {
				visited[x] = visited[t] + 1;
				q.push(x);
			}
		}

	}

	return -1;

}