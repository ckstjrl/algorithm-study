#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

using namespace std;

vector<int> parent;

// Union-Find를 위한 Find Set 함수
int find_set(int x) {
    if (parent[x] == x) return x;
    
    return parent[x] = find_set(parent[x]);  // 경로 압축
}

// Union-Find를 위한 Union 함수
bool union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);

    if (a == b) return false;

    parent[b] = a;
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int V, E;
    cin >> V >> E;

    vector<pair<int, pair<int, int>>> edges(E);
    for (int i = 0; i < E; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        edges[i] = {c, {a, b}};  // { 가중치, { 정점1, 정점2 } } 로 저장
    }

    sort(edges.begin(), edges.end());  // 가중치 기준으로 오름차순 정렬

    parent.assign(V + 1, 0);
    iota(parent.begin(), parent.end(), 0);  // parent[i] = i 초기화

    long long res = 0;
    for (int i = 0; i < E; i++) {  // 크루스칼 알고리즘
        int w = edges[i].first;
        int u = edges[i].second.first;
        int v = edges[i].second.second;

        if (union_set(u, v)) {
            res += w;
        }
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}