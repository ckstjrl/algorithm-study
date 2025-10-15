#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N, M;
vector<vector<int>> arr;
vector<vector<bool>> visited;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int i, int j) {  // bfs로 탐색하며 빙하 덩어리 판단
    queue<pair<int, int>> q;
    q.emplace(i, j);
    visited[i][j] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (!visited[ny][nx] && arr[ny][nx]) {
                q.emplace(ny, nx);
                visited[ny][nx] = true;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> N >> M;

    arr.resize(N, vector<int>(M));  // 빙산 정보를 위한 2차원 배열 초기화

    for (int i = 0; i < N; i++) {  // 빙산 정보 입력 받음
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    int res = 0;  // 결과 시간(년)
    while (true) {
        vector<vector<int>> temp_arr = arr;  // 빙산이 녹은 결과를 위한 임시 배열
        for (int i = 0; i < N; i++) {  // 빙산 정보 순회하면서
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 0) continue;  // 바다면 넘어감
                int temp = 0;  // 둘러싸인 바다 면의 수
                for (int k = 0; k < 4; k++) {
                    int ni = i + dy[k];
                    int nj = j + dx[k];

                    if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
                    if (arr[ni][nj] == 0) temp++;
                }
                temp_arr[i][j] = max(0, arr[i][j] - temp);  // 바다로 둘러싸인만큼 감소시킴. 0보다 작아지면 0으로 만듦.
            }
        }
        arr = temp_arr;  // 1년 후, 녹은 빙산의 결과 반영
        res++;  // 1년 증가

        int cnt = 0;  // 연결된 빙하 덩어리 수
        visited.assign(N, vector<bool>(M, false));  // bfs를 위한 방문배열 false로 초기화
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (!visited[i][j] && arr[i][j]) {
                    bfs(i, j);  // bfs 탐색으로 덩어리 판단
                    cnt++;  // 덩어리 수 증가
                }
            }
        }
        if (cnt == 0) {  // 덩어리가 0이라면 == 다 녹음
            res = 0;  // 다 녹을 때까지 두 덩어리 이상 분리되지 않았으므로 res에 0 넣고 반복 중단
            break;
        }
        if (cnt >= 2) break;  // 두 덩어리 이상이면 반복 중단
    }

    cout << res << '\n';  // 결과 출력
    
    return 0;
}