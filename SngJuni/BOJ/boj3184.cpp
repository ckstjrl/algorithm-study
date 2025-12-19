#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

int R, C;
int resO, resV;
vector<string> board;
vector<vector<bool>> visited;

// 4방향 델타 배열
int dx[4] = {-1, 1, 0, 0};
int dy[4] = {0, 0, -1, 1};

void bfs(int sx, int sy) {
    queue<pair<int, int>> q;
    q.emplace(sx, sy);  // 시작 좌표 처리
    visited[sx][sy] = true;

    int cntO = 0, cntV = 0;

    while (!q.empty()) {
        int x = q.front().first;
        int y = q.front().second;
        q.pop();

        // 현재 칸이 양이면
        if (board[x][y] == 'o') cntO++;
        // 현재 칸이 늑대면
        else if (board[x][y] == 'v') cntV++;

        for (int d = 0; d < 4; d++) {
            int nx = x + dx[d];
            int ny = y + dy[d];

            if (nx < 0 || nx >= R || ny < 0 || ny >= C) continue;
            if (visited[nx][ny]) continue;
            if (board[nx][ny] == '#') continue;

            q.emplace(nx, ny);
            visited[nx][ny] = true;
        }
    }

    // 영역 내에서 양이 더 많으면 양만 생존
    if (cntO > cntV) resO += cntO;
    // 그렇지 않으면 늑대만 생존
    else resV += cntV;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> R >> C;

    board.assign(R, "");
    for (int i = 0; i < R; i++) {
        cin >> board[i];
    }

    visited.assign(R, vector<bool>(C, false));

    resO = 0;
    resV = 0;

    for (int i = 0; i < R; i++) {
        for (int j = 0; j < C; j++) {
            // 아직 방문 X, 울타리가 아니면 BFS 탐색
            if (!visited[i][j] && board[i][j] != '#') {
                bfs(i, j);
            }
        }
    }

    cout << resO << ' ' << resV << '\n';

    return 0;
}
