#include <iostream>
#include <queue>

using namespace std;

int n, m;
int arr[1001][1001];  // 지도 정보를 위한 정적 배열
int res[1001][1001];  // 결과를 위한 정적 배열
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int i, int j) {
    queue<pair<int, int>> q;
    q.push({i, j});
    res[i][j] = 0;  // 목표 지점은 거리 0으로 초기화

    while (!q.empty()) {
        int cx = q.front().first;
        int cy = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = cx + dx[k];
            int ny = cy + dy[k];

            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (res[nx][ny] == -1 && arr[nx][ny] != 0) {  // 방문한 적이 없고, 벽이 아니면
                q.push({nx, ny});
                res[nx][ny] = res[cx][cy] + 1;  // 결과 배열에 거리 1 추가
            }
        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;
    
    int si, sj;
    for (int i = 0; i < n; i++) {      // 지도를 위한 배열을 입력받으면서, 결과를 위한 res 배열 -1로 초기화
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
            res[i][j] = -1;

            if (arr[i][j] == 2) {      // 출발지점 찾기
                si = i;
                sj = j;
            }
        }
    }

    bfs(si, sj);  // 출발지점으로부터 bfs 탐색

    for (int i = 0; i < n; i++) {  // 결과 배열 출력
        for (int j = 0; j < m; j++) {
            if (arr[i][j] == 0) cout << 0 << " ";
            else cout << res[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}