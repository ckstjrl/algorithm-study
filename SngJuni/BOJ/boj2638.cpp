#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
vector<vector<int>> board;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

// 공기의 좌표들을 상하좌우 bfs 탐색하면서
// 각 치즈가 공기에 닿는 면의 수를 확인해서 2 이상이면 녹임.
int bfs(int si, int sj) {
    vector<vector<int>> air(N, vector<int>(M, 0));            // 각 치즈가 공기와 접촉한 면 수
    vector<vector<bool>> visited(N, vector<bool>(M, false));  // 방문 배열
    
    queue<pair<int, int>> q;
    q.emplace(si, sj);       // 시작점 설정
    visited[si][sj] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {  // 4방향 탐색
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;  // 범위 바깥

            if (!visited[ny][nx]) {
                if (board[ny][nx] == 0) {  // 공기라면 queue에 push
                    q.emplace(ny, nx);
                    visited[ny][nx] = true;
                } else if (board[ny][nx] == 1) {  // 치즈라면
                    air[ny][nx] += 1;             // 공기와 접촉한 면 수 1 증가
                }
            }
        }
    }

    int cnt = 0;  // 녹을 치즈의 수
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 1 && air[i][j] >= 2) {  // 해당 칸이 치즈 이고, 공기와 접촉한 면 수가 2 이상이면
                board[i][j] = 0;  // 치즈 녹이고
                cnt++;            // 녹을 치즈의 수 1 증가
            }
        }
    }

    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    board.assign(N, vector<int>(M, 0));  // 치즈 위치 입력 받음.
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }

    int res = 0;
    while (true) {  // 치즈가 모두 다 녹을 때까지 (0, 0) 칸에서부터 bfs 탐색
        int cnt = bfs(0, 0);

        if (cnt == 0) break;  // 치즈가 모두 다 녹으면 종료
        res++;
    }

    cout << res << '\n';

    return 0;
}