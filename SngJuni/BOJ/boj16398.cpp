#include <iostream>
#include <vector>
#include <tuple>

using namespace std;

int parent[1001];

// Union-Find 의 find_set
int find_set(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find_set(parent[x]);
}

// Union-Find 의 union_set
void union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);
    if (a != b) parent[b] = a;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    // 간선 리스트 (w, u, v)
    vector<tuple<int, int, int>> edges;
    edges.reserve(N * N);

    vector<vector<int>> cost(N + 1, vector<int>(N + 1));

    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= N; j++) {  
            cin >> cost[i][j];
        }
    }

    for (int i = 1; i <= N; i++) {
        for (int j = i + 1; j <= N; j++) {
            edges.push_back({cost[i][j], i, j});
        }
    }

    // Union-Find 초기화
    for (int i = 1; i <= N; i++) parent[i] = i;

    // 비용 기준 오름차순 정렬
    sort(edges.begin(), edges.end(),
        [](const tuple<int, int, int>& a, const tuple<int, int, int>& b) {
            return get<0>(a) < get<0>(b);
        });

    long long res = 0;

    // 크루스칼 알고리즘
    for (auto& e : edges) {
        int w = get<0>(e);
        int u = get<1>(e);
        int v = get<2>(e);

        // 같은 집합이 아니면 연결
        if (find_set(u) != find_set(v)) {
            union_set(u, v);

            res += w;
        }
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}