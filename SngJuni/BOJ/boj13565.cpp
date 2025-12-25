#include <iostream>
#include <vector>
#include <queue>
#include <string>

using namespace std;

int M, N;
vector<vector<int>> board;
vector<vector<bool>> visited;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int i, int j) {
    queue<pair<int, int>> q;
    q.push({i, j});
    visited[i][j] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (!visited[ny][nx] && board[ny][nx] == 0) {
                q.push({ny, nx});
                visited[ny][nx] = true;
            }
        }
    }
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> M >> N;

    board.assign(M, vector<int>(N, 0));
    visited.assign(M, vector<bool>(N, false));

    string s;
    for (int i = 0; i < M; i++) {
        cin >> s;
        for (int j = 0; j < N; j++) {
            board[i][j] = s[j] - '0';
        }
    }

    for (int i = 0; i < N; i++) {
        if (!visited[0][i] && board[0][i] == 0) {
            bfs(0, i);
        }
    }

    string res = "NO\n";
    for (int i = 0; i < N; i++) {
        if (visited[M - 1][i]) {
            res = "YES\n";
            break;
        }
    }

    cout << res;

    return 0;
}