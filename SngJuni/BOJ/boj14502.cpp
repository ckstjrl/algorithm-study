#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N, M, res;
vector<vector<int>> board;
vector<vector<int>> temp;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs() {
    queue<pair<int, int>> q;

    temp = board;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (temp[i][j] == 2) {
                q.emplace(i, j);
            }
        }
    }

    while (!q.empty()) {
        auto [y, x] = q.front();
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (temp[ny][nx] == 0) {
                q.emplace(ny, nx);
                temp[ny][nx] = 2;
            }
        }
    }

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (temp[i][j] == 0) {
                cnt++;
            }
        }
    }
    res = max(res, cnt);
}

void dfs(int cnt) {
    if (cnt == 3) {
        bfs();
        return;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (board[i][j] == 0) {
                board[i][j] = 1;
                dfs(cnt + 1);
                board[i][j] = 0;
            }
        }
    }
}

int main() {
    cin >> N >> M;

    board.assign(N, vector<int>(M, 0));
    temp.assign(N, vector<int>(M, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> board[i][j];
        }
    }

    dfs(0);

    cout << res << '\n';

    return 0;
}