#include <iostream>
#include <vector>
#include <queue>
#include <tuple>

using namespace std;

int m, n, h, res;
vector<vector<vector<int>>> tomato;  // 각 토마토 상자 정보를 위한 3차원 가변 배열
vector<vector<vector<int>>> day;     // 각 토마토가 익는데 걸리는 일수를 위한 3차원 가변 배열

int dz[6] = {-1, 1, 0, 0, 0, 0};     // 3차원 델타
int dx[6] = {0, 0, 0, 0, -1, 1};
int dy[6] = {0, 0, -1, 1, 0, 0};

void bfs() {
    queue<tuple<int, int, int>> q;  // x, y, z 좌표를 위한 queue

    int cnt = 0;  // 익지 않은 토마토의 갯수를 세기 위한 변수 
    for (int k = 0; k < h; k++) {            // 3차원 배열 순회하면서 
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (tomato[k][i][j] == 1) {  // 익은 토마토의 좌표 queue에 넣고 
                    q.emplace(k, i, j);
                } else if (tomato[k][i][j] == 0) {  // 익지 않은 토마토의 갯수 셈
                    cnt++;
                }
            }
        }
    }

    if (cnt == 0) {  // 토마토가 이미 모두 다 익었다면
        res = 0;
        return;
    }

    while (!q.empty()) {
        int z, y, x;
        tie(z, y, x) = q.front();  // g++17 이상부터는 구조적 바인딩 사용 가능
        q.pop();

        for (int i = 0; i < 6; i++) {
            int nz = z + dz[i];
            int ny = y + dy[i];
            int nx = x + dx[i];

            if (nz < 0 || nz >= h || ny < 0 || ny >= n || nx < 0 || nx >= m) continue;  // 상자 범위 벗어나면
            if (tomato[nz][ny][nx] != 0) continue;  // 토마토가 익었거나 들어있지 않으면

            tomato[nz][ny][nx] = 1;  // 토마토 익히고
            cnt--;  // 익지 않은 토마토 갯수 1 감소
            day[nz][ny][nx] = day[z][y][x] + 1;  // 토마토가 익는데 걸리는 일수 증가
            q.emplace(nz, ny, nx);  // 익은 토마토 좌표 queue에 넣고
            res = max(res, day[nz][ny][nx]);  // 토마토가 익는데까지 걸리는 일자 갱신
        }
    }
    if (cnt > 0) {
        res = -1;
        return;
    }
}

int main() {
    ios_base::sync_with_stdio(false); // 입출력 최적화 코드
    cin.tie(NULL);
    
    cin >> m >> n >> h;
    
    tomato.assign(h, vector<vector<int>>(n, vector<int>(m, 0)));  // m, n, h 길이로 3차원 가변 배열 0으로 초기화
    day.assign(h, vector<vector<int>>(n, vector<int>(m, 0)));     // m, n, h 길이로 3차원 가변 배열 0으로 초기화

    for (int k = 0; k < h; k++) {    // 토마토 상자 정보 입력받음.
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                cin >> tomato[k][i][j];
            }
        }
    }

    bfs();  // bfs로 탐색

    cout << res << '\n';

    return 0;
}