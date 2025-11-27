#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M, p1, p2;
vector<vector<int>> graph;
vector<int> dist;

int res = -1;
vector<int> visited;

void bfs(int start) {  // queue 사용해서 bfs 탐색하면서 무가중치 그래프에 대한 거리 구함.
    queue<int> q;
    q.emplace(start);
    dist[start] = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (auto& i : graph[cur]) {
            if (dist[i] == -1) {
                q.emplace(i);
                dist[i] = dist[cur] + 1;
            }
        }
    }
}

void dfs(int cur, int depth) {  // 재귀적으로 dfs 탐색하면서 두번째 사람을 만나면 탐색 종료.
    if (cur == p2) {
        res = depth;
        return;
    }
    
    visited[cur] = 1;

    for (auto& i : graph[cur]) {
        if (!visited[i]) {
            dfs(i, depth + 1);
            if (res != -1) return;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    graph.assign(N + 1, {});  // 가족 관계를 인접리스트로 받음
    dist.assign(N + 1, -1);   // 촌수(방문배열)를 -1로 초기화
    // visited.assign(N + 1, 0);

    cin >> p1 >> p2;

    cin >> M;

    int u, v;
    for (int i = 0; i < M; i++) {
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    bfs(p1);        // 첫번째 사람을 시작으로 bfs 탐색
    // dfs(p1, 0);  // dfs 시에는 첫번째 사람과 depth 0으로 탐색

    cout << dist[p2] << '\n';
    // cout << res << '\n';

    return 0;
}