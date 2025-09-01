#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int t, n, m, res;
vector<int> arr[11];
bool visited[11];

void reset() {                                   // 테스트 케이스마다 초기화를 위한 함수
    res = 0;
    for (int i = 0; i < 11; i++) { 
        arr[i].clear();
        visited[i] = false;
    }
}

void dfs(int k, int cnt) {          // dfs 로 탐색
    res = max(res, cnt);            // 최장 경로 갱신
    for (auto i : arr[k]) {         // 현재 정점 k 에 연결된 인접 정점 순회
        if (!visited[i]) {          // 아직 방문하지 않은 정점이면
            visited[i] = true;      // 방문 체킹
            dfs(i, cnt + 1);        // 다음 정점 탐색
            visited[i] = false;     // 백트래킹
        }
    }
}

int main() {
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        cin >> n >> m;

        reset();                         // 테스트 케이스마다 cnt 및 배열 초기화

        int u, v;
        for (int i = 0; i < m; i++) {    // 정점, 간선 정보 입력
            cin >> u >> v;

            arr[u].push_back(v);
            arr[v].push_back(u);
        }

        for (int i = 0; i <= n; i++) {
            visited[i] = true;           // 방문 체킹
            dfs(i, 1);                   // 정점 탐색
            visited[i] = false;          // 백트래킹

        }

        cout << "#" << tc << " " << res << "\n";
    }

    return 0;
}