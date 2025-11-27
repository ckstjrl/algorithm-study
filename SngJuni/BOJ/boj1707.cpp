#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<vector<int>> graph;  // 인접리스트로 그래프 정보를 받기 위한 2차원 가변배열
vector<int> visited;        // 각 그래프의 방문정보 및 이분할 수 있는지 판단하기 위한 1차원 가변배열
bool flag;  // 이분 그래프인지 아닌지 판별을 위한 flag

void bfs(int start) {
    queue<int> q;
    q.push(start);
    visited[start] = 1;  // 첫번째 방문한 정점을 1로 표시
    
    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (const auto& i : graph[cur]) {
            if (visited[i] == 0) {
                q.push(i);
                visited[i] = -visited[cur];  // 현재 방문한 정점과 이분된다는 의미를 위해 -1로 바꿔가며 방문 체크
            } else if (visited[i] == visited[cur]) {  // 만약 방문 정보가 같다면 이분 그래프가 아니므로
                flag = false;                         // flag를 false로 바꾸고 함수 종료
                return;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int T, V, E;
    cin >> T;
    while (T--) {
        cin >> V >> E;

        graph.assign(V + 1, {});
        visited.assign(V + 1, 0);

        int u, v;
        for (int i = 0; i < E; i++) {  // 그래프 간선 정보 입력 받기
            cin >> u >> v;
            graph[u].push_back(v);
            graph[v].push_back(u);
        }

        flag = true;
        for (int i = 1; i < V + 1; i++) {  // 정점을 순회하며
            if (visited[i] == 0) {         // 방문하지 않은 정점이고
                if (flag) bfs(i);          // 아직 flag가 true라면 bfs 탐색
            }
        }
        
        if (flag) cout << "YES\n";  // 결과 출력
        else cout << "NO\n";
    }

    return 0;
}