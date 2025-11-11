/*** 1774. 우주신과의 교감 ***/

#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>
#include<cmath>
#include<iomanip>
using namespace std;

int find_set(int x);
void unite(int x, int y);

vector<int> parent, rnk;
vector<tuple<double, int, int>> edges;

int main() {
	int N, M;
	cin >> N >> M;
	parent.assign(N + 1, 0); rnk.assign(N + 1, 1);
	vector<pair<int, int>> pos(N + 1);

	// 신의 좌표 저장
	for (int i = 1; i < N + 1; i++) {
		int x, y;
		cin >> x >> y;
		pos[i] = { x, y };
		parent[i] = i;
	}

	// 연결된 신 unite
	for (int i = 0; i < M; i++) {
		int x, y;
		cin >> x >> y;
		unite(x, y);
	}

	// 신들과의 거리 계산 후 저장
	for (int i = 1; i < N + 1; i++) {
		for (int j = i + 1; j < N + 1; j++) {
			double w = hypot(pos[i].first - pos[j].first, pos[i].second - pos[j].second);
			edges.emplace_back(w, i, j);
		}
	}

	// 오름차순 정렬
	sort(edges.begin(), edges.end());

	// 간선 선택
	int cnt = 0;
	double ans = 0;
	for (auto& edge : edges) {
		double w;
		int u, v;
		tie(w, u, v) = edge;

		if (find_set(u) != find_set(v)) {
			unite(u, v);
			cnt++;
			ans += w;

			if (cnt == N - 1) break;
		}
	}

	cout << fixed << setprecision(2) << ans;

	return 0;
}

int find_set(int x) {
	if (x == parent[x]) return x;
	return parent[x] = find_set(parent[x]);
}

void unite(int x, int y) {
	x = find_set(x);
	y = find_set(y);

	if (x == y) return;
	if (rnk[x] > rnk[y]) swap(x, y);
	parent[x] = y;
	if (rnk[x] == rnk[y]) rnk[y]++;
}