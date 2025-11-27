#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int t, m, n, k, cnt;
vector<vector<int>> arr;       // 배추 정보를 위한 2차원 가변배열
vector<vector<bool>> visited;  // 방문 정보를 위한 2차원 가변배열

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int i, int j) {
    queue<pair<int, int>> q;
    q.push({i, j});
    visited[i][j] = true;
    cnt++;  // 지렁이가 필요한 횟수 == bfs 함수가 호출되는 횟수

    while (!q.empty()) {
        int cy = q.front().first;  // i, j와 x, y 순서 잘 생각할 것.
        int cx = q.front().second;
        q.pop();

        for (int l = 0; l < 4; l++) {
            int ny = cy + dy[l];
            int nx = cx + dx[l];

            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (!visited[ny][nx] && arr[ny][nx]) {  // 아직 방문하지 않았고, 배추가 존재한다면 queue에 push
                q.push({ny, nx});
                visited[ny][nx] = true;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> t;
    while (t--) {
        cin >> m >> n >> k;

        cnt = 0;
        arr.assign(n, vector<int>(m, 0));           // 매 테스트케이스마다 2차원 가변배열 0으로 초기화
        visited.assign(n, vector<bool>(m, false));  // 매 테스트케이스마다 2차원 가변배열 false로 초기화

        int x, y;
        for (int i = 0; i < k; i++) {  // 배추 위치 정보 입력받음. 배열의 가로, 세로와 x, y 좌표 잘 생각할 것.
            cin >> x >> y;
            arr[y][x] = 1;
        }

        for (int i = 0; i < n; i++) {               // 2차원 배열 순회 
            for (int j = 0; j < m; j++) {
                if (!visited[i][j] && arr[i][j]) {  // 아직 방문하지 않았고, 배추가 존재한다면 bfs로 탐색
                    bfs(i, j);
                }
            }
        }
        cout << cnt << '\n';
    }

    return 0;
}