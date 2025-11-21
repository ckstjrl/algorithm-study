/*** 16398. 행성 연결 ***/

#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>
using namespace std;

vector<tuple<long long, int, int>> edges;
vector<int> parent;
vector<int> rnk;
int N;
long long cost = 0;

int find_set(int x);
void unite(int x, int y);

int main() {
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			long long w;
			cin >> w;
			if(j > i && i != j) edges.emplace_back(w, i, j);
		}
	}

	sort(edges.begin(), edges.end());

	parent.assign(N, 0);
	rnk.assign(N, 1);
	for (int i = 0; i < N; i++) {
		parent[i] = i;
	}

	int cnt = 0;
	for (auto& edge : edges) {
		long long w;
		int u, v;
		tie(w, u, v) = edge;

		if (find_set(u) != find_set(v)) {
			unite(u, v);
			cnt++;
			cost += w;
		}

		if (cnt == N - 1) break;
	}

	cout << cost;

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