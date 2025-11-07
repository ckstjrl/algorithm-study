#include <iostream>
#include <vector>
#include <cmath>
#include <iomanip>
#include <algorithm>

using namespace std;

int parent[1001];  // union-find 위한 부모 배열

// find_set : x의 대표 노드 반환 함수
int find_set(int x) {
    if (parent[x] == x) return x;
    return parent[x] = find_set(parent[x]);
}

// union_set : 두 노드를 합치는 함수
bool union_set(int a, int b) {
    a = find_set(a);
    b = find_set(b);

    if (a == b) return false;
    parent[b] = a;
    
    return true;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<pair<double, double>> pos(N + 1);  // 각 우주선의 좌표
    for (int i = 1; i <= N; i++) {
        cin >> pos[i].first >> pos[i].second;
    }

    for (int i = 1; i <= N; i++) {  // 모든 노드의 부모를 자기 자신으로 초기화
        parent[i] = i;
    }

    int a, b;
    for (int i = 0; i < M; i++) {  // 이미 연결된 노드들 연결
        cin >> a >> b;
        union_set(a, b);
    }

    // 모든 우주신 쌍 간의 거리 계산
    vector<pair<double, pair<int, int>>> edges;
    for (int i = 1; i <= N; i++) {
        for (int j = i + 1; j <= N; j++) {
            double dx = pos[i].first - pos[j].first;
            double dy = pos[i].second - pos[j].second;

            double dist = sqrt(dx * dx + dy * dy);
            edges.push_back({dist, {i, j}});
        }
    }

    // 거리를 기준으로 오름차순 정렬
    sort(edges.begin(), edges.end());

    double res = 0;  // MST 길이
    for (auto& e : edges) {
        double w = e.first;
        int u = e.second.first, v = e.second.second;

        if (union_set(u, v)) res += w;  // 아직 연결되지 않았으면 연결하고 거리 더하기
    }

    // 소수점 둘째 자리까지 출력
    cout << fixed << setprecision(2) << res << '\n';

    return 0;
}