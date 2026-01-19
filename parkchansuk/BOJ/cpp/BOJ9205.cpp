// BOJ 9205. 맥주 마시면서 걸어가기 / G5
#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int T;
	cin >> T;

	while (T--) {
		int n;
		cin >> n;
		string ans = "happy";

		vector<pair<int, int>> mapp;
		for (int i = 0; i < n + 2; i++) {
			int x, y;
			cin >> x >> y;
			mapp.push_back({ x, y });
		}

		vector<vector<int>> graph(n + 2);
		for (int i = 0; i < n + 1; i++) {
			for (int j = 1; j < n + 2; j++) {
				int x1, y1, x2, y2;
				x1 = mapp[i].first;
				y1 = mapp[i].second;
				x2 = mapp[j].first;
				y2 = mapp[j].second;

				int leng = abs(x1 - x2) + abs(y1 - y2);
				if (leng <= 1000) {
					graph[i].push_back(j);
					graph[j].push_back(i);
				}

			}
		}

		queue<int> q;
		vector<int> visited(n + 2, 0);
		q.push(0);
		visited[0] = 1;

		while (!q.empty()) {
			int cur = q.front();
			q.pop();

			for (int nxt : graph[cur]) {
				if (visited[nxt] == 0) {
					q.push(nxt);
					visited[nxt] = 1;
				}
			}
		}
		if (visited[n + 1] == 1) {
			cout << "happy" << "\n";
		}
		else {
			cout << "sad" << "\n";
		}
	}
}

/*
처음에 아무생각없이 인접한 인덱스사이 거리만 계산했는데
집에서 편의점 1은 못가지만 편의점 2는 갈 수 있고, 집 -> 편의점 2 -> 편의점 1 -> 페스티벌 이렇게 갈 수 있는 경우를 고려하지 못함.
모든 인덱스 사이 거리를 구해 그 거리가 1000이하인 경우에는 graph에 연결된 노드로 생각하고 graph 구현
이를 통해 BFS 방식으로 페스티벌에 도착할 수 있는지 없는지 확인 후 출력
*/