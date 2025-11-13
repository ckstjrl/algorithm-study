#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
	int n, m;  // n: 동기 수, m: 친구 관계 수
	cin >> n >> m;

	// 그래프 만들기 (인접 리스트)
	vector<int> graph[501];

	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	queue<pair<int, int>> q;
	bool visited[501] = { false };

	q.push({ 1, 0 });
	visited[1] = true;

	int count = 0;

	while (!q.empty()) {
		int current = q.front().first;  // 현재 사람
		int depth = q.front().second;  // 현재 깊이
		q.pop();

		if (depth >= 2) continue;

		for (int i = 0; i < graph[current].size(); i++) {
			int next = graph[current][i];

			if (!visited[next]) {
				visited[next] = true;
				q.push({ next, depth + 1 });
				count++;
			}
		}
	}

	cout << count << endl;

	return 0;
}