#include <iostream>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int n;
vector<vector<pair<int, int>>> tree;  // 트리 정보를 위한 인접리스트

pair<int, long long> bfs(int start) {   // bfs로 시작 정점에서 가장 먼 정점과 그 거리 반환
    vector<long long> dist(n + 1, -1);  // 각 정점으로의 거리 및 방문 정보를 위한 가변배열
    queue<int> q;
    q.push(start);
    dist[start] = 0;

    int farthest = start;    // 가장 먼 정점
    long long max_dist = 0;  // 가장 먼 거리

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (const auto& k : tree[cur]) {
            int next = k.first;
            int weight = k.second;

            if (dist[next] == -1) {  // 이미 방문한 정점이 아니라면
                dist[next] = dist[cur] + weight;  // 거리 추가
                q.push(next);

                if (dist[next] > max_dist) {  // 가장 먼 거리, 정점 갱신
                    max_dist = dist[next];
                    farthest = next;
                }
            }
        }
    }
    return {farthest, max_dist};
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> n;
    tree.assign(n + 1, {});  // 인접 리스트 초기화

    int u, v, w;
    for (int i = 0; i < n; i++) {
        cin >> u;
        while (cin >> v && v != -1) {
            cin >> w;
            tree[u].push_back({v, w});
        }
    }

    // 1. 임의의 정점(1번 정점)에서 가장 먼 정점 찾기
    pair<int, long long> first_bfs_res = bfs(1);
    // 2. 1에서 찾은 정점에서 가장 먼 정점 찾기 (두 정점 간의 거리 == 트리의 지름)
    pair<int, long long> second_bfs_res = bfs(first_bfs_res.first);

    cout << second_bfs_res.second << '\n';

    return 0;
}