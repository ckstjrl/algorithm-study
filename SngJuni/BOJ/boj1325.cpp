#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
vector<vector<int>> graph;

int bfs(int start) {  // 각 정점에서 방문할 수 있는 컴퓨터 갯수 BFS로 탐색해서 반환
    int cnt = 0;
    vector<bool> visited(N + 1, false);
    queue<int> q;
    q.emplace(start);
    visited[start] = true;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        cnt++;

        for (auto& i : graph[cur]) {
            if (!visited[i]) {
                q.emplace(i);
                visited[i] = true;
            }
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    graph.assign(N + 1, {});

    for (int i = 0; i < M; i++) {  // B -> A 이므로 간선 정보 뒤집어서 받기 (중요!)
        int u, v;
        cin >> u >> v;
        graph[v].push_back(u);
    }

    int max_res = -1;
    vector<int> res;
for (int i = 1; i <= N; i++) {  // 1 ~ N 순회하면서 max_res, res 갱신
        int temp = bfs(i);  // bfs로 각 컴퓨터에서 해킹할 수 있는 컴퓨터 갯수 반환
        if (temp > max_res) {
            res.clear();
            res.push_back(i);
            max_res = temp;
        } else if (temp == max_res) {
            res.push_back(i);
        }
    }

    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << ' ';
    }
    
    cout << '\n';

    return 0;
}