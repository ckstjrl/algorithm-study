#include <iostream>
#include <string>
#include <queue>

using namespace std;

int n, m;
int arr[101][101];  // 미로 정보를 위한 정적 배열
int dist[101][101]; // 거리 정보를 위한 정적 배열
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int i, int j) {
    queue<pair<int, int>> q;
    q.push({i, j});
    dist[i][j] = 1;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (dist[nx][ny] == 0 && arr[nx][ny] == 1) {  // 현재 방문하지 않았고 이동할 수 있는 칸일 때
                q.push({nx, ny});
                dist[nx][ny] = dist[x][y] + 1;  // 거리 1 증가
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 속도 최적화를 위한 코드
    cin.tie(NULL);
    
    cin >> n >> m;

    string s;
    for (int i = 0; i < n; i++) {
        cin >> s;
        for (int j = 0; j < m; j++) {
            arr[i][j] = s[j] - '0';
        }
    }
    bfs(0, 0);  // bfs로 탐색
    cout << dist[n - 1][m - 1];  // (N, M) 까지의 거리 출력

    return 0;
}