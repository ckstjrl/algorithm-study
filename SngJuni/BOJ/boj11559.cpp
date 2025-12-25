#include <iostream>
#include <vector>
#include <string>
#include <queue>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int N = 12, M = 6;
    vector<string> board(N);  // 뿌요 좌표 정보를 위한 문자열 배열
    for (int i = 0; i < N; i++) cin >> board[i];

    int dx[4] = {0, 0, -1, 1};  // 상하좌우 델타
    int dy[4] = {-1, 1, 0, 0};

    int res = 0;  // 연쇄가 일어난 횟수

    while (true) {
        vector<vector<bool>> visited(N, vector<bool>(M, false));  // 방문 정보를 위한 2차원 배열

        bool removed = false;  // 연쇄가 일어나서 뿌요가 제거되었는지 확인을 위한 flag

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == '.' || visited[i][j]) continue;  // 빈 공간이거나 이미 방문한 좌표면 넘어감.

                char cur = board[i][j];      // 현재 뿌요의 색깔
                queue<pair<int, int>> q;     // 상하좌우 bfs 탐색을 위한 queue
                queue<pair<int, int>> puyo;  // 연결된 뿌요들의 좌표
                q.emplace(i, j);
                puyo.emplace(i, j);
                visited[i][j] = true;

                while (!q.empty()) {
                    int y = q.front().first;
                    int x = q.front().second;
                    q.pop();

                    for (int k = 0; k < 4; k++) {  // 상하좌우 탐색
                        int nx = x + dx[k];
                        int ny = y + dy[k];

                        if (nx < 0 || nx >= M || ny < 0 || ny >= N || visited[ny][nx]) continue;  // 범위 밖이거나 방문한 곳이면 넘어감.
                        if (board[ny][nx] != cur) continue;  // 현재 뿌요의 색깔과 다르면 넘어감.
                        
                        visited[ny][nx] = true;  // 방문 체크
                        q.emplace(ny, nx);       // bfs queue에 push
                        puyo.emplace(ny, nx);    // 연결된 뿌요로 추가
                    }
                }

                if (puyo.size() >= 4) {  // 연결된 뿌요의 갯수가 4개 이상이면
                    removed = true;      // 연쇄 일어남.

                    while (!puyo.empty()) {
                        int y = puyo.front().first;
                        int x = puyo.front().second;
                        puyo.pop();
                        board[y][x] = '.';  // 연결된 뿌요 제거
                    }
                }
            }
        }

        if (!removed) break;  // 연쇄가 일어나지 않았으면 게임 종료

        // 뿌요 제거 이후, 중력의 영향 적용
        for (int i = 0; i < M; i++) {  // 열을 기준으로 순회
            int bottom = N - 1;        // 해당 열의 바닥
            for (int j = bottom; j >= 0; j--) {        // 맨 아래 행부터 위로 검사
                if (board[j][i] != '.') {              // 빈 칸이 아니라면
                    board[bottom][i] = board[j][i];    // 그 뿌요를 가장 아래(bottom)로 내림
                    if (bottom != j) board[j][i] = '.';// 원래 뿌요의 위치는 빈 칸으로 바꿈
                    bottom--;  // 다음 뿌요는 그 윗칸이어야 하므로 bottom을 한 칸 올림.
                }
            }
        }
        res++;  // 연쇄 1회 증가
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}