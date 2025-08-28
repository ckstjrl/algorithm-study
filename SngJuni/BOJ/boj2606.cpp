#include <iostream>
#include <queue>

using namespace std;

int n, m, cnt;
vector<vector<int>> arr;  // 컴퓨터 연결 정보를 위한 2차원 가변배열
vector<bool> visited;     // 컴퓨터 방문 정보를 위한 가변배열

void bfs(int i) {
    queue<int> q;
    q.push(i);
    visited[i] = true;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();
        cnt += 1;

        for (auto k : arr[cur]) {   // 해당 컴퓨터와 연결된 컴퓨터에 대해서
            if (!visited[k]) {      // 방문한 적이 없다면
                q.push(k);          // queue에 push
                visited[k] = true;  // 방문 체크
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    arr.assign(n + 1, {});  // 2차원 가변배열을 n + 1 만큼 {} 로 초기화
    visited.assign(n + 1, false);  // 가변배열을 n + 1 만큼 false 로 초기화

    int u, v;
    for (int i = 0 ; i < m; i++) {
        cin >> u >> v;
        arr[u].push_back(v);  // u에 v 연결
        arr[v].push_back(u);  // v에 u 연결
    }

    bfs(1);

    cout << cnt - 1 << '\n';  // 1 제외한 cnt 출력

    return 0;
}