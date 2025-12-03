#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N;
vector<vector<int>> board;  // 공간 정보


int sx, sy, cnt, res;  // 상어 좌표 (sx, sy), 먹은 횟수 (cnt), 총 이동 시간 (res)
int shark = 2;         // 상어의 현재 크기

// 4방향 델타 배열
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

bool bfs() {
    vector<vector<int>> dist(N, vector<int>(N, -1));  // 거리 배열
    queue<pair<int, int>> q;

    q.emplace(sy, sx);  // 현재 상어 위치에서 시작
    dist[sy][sx] = 0;

    int ty = -1, tx = -1;  // 먹을 물고기 후보 좌표
    int minDist = -1;      // 먹을 물고기까지의 최단거리

    while (!q.empty()) {
        auto [y, x] = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;  // 범위 바깥
            if (dist[ny][nx] != -1) continue;                      // 이미 방문했으면
            if (board[ny][nx] > shark) continue;                   // 상어보다 큰 물고기면

            q.emplace(ny, nx);
            dist[ny][nx] = dist[y][x] + 1;

            if (board[ny][nx] >= 1 && board[ny][nx] < shark) {
                bool flag = false;  // 최적 후보 물고기인지 판별

                if (minDist == -1) {  // 첫 물고기
                    flag = true;
                } else if (dist[ny][nx] < minDist) {  // 더 가까운 물고기
                    flag = true;
                } else if (dist[ny][nx] == minDist) {        // 거리 같으면
                    if (ny < ty || (ny == ty && nx < tx)) {  // 위쪽 -> 왼쪽 우선
                        flag = true;
                    }
                }

                if (flag) {  // 후보 물고기 갱신
                    minDist = dist[ny][nx];
                    tx = nx;
                    ty = ny;
                }
            }
        }
    }

    if (minDist == -1) return false;  // 먹을 수 있는 물고기 없음

    res += minDist;  // 이동 시간 합산
    sx = tx;         // 상어 좌표 갱신
    sy = ty;
    board[sy][sx] = 0;  // 먹은 물고기 처리
    cnt++;

    if (cnt == shark) {  // 상어 크기 성장
        shark++;
        cnt = 0;
    }

    return true;  // 이번 BFS에서는 물고기 먹기 성공
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N;

    board.assign(N, vector<int>(N));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
            if (board[i][j] == 9) {  // 상어 시작 위치
                sy = i;
                sx = j;
                board[i][j] = 0;  // 빈 칸으로 변경
            }
        }
    }

    while (bfs()) {}  // bfs()가 false를 반환할 때까지 반복

    cout << res << '\n';

    return 0;
}