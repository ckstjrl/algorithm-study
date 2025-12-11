/*
BOJ1520 : 내리막 길 (G3)

해결 방법 : 
dp로 이미 계산된 값을 재사용 -> dfs 재귀로 해결하기
*/

#include <iostream>
#include <vector>
using namespace std;

int m, n;
vector<vector<int>> board;
vector<vector<int>> dp;

int dfs(int r, int c) {
    if (r == m - 1 && c == n - 1) {
        return 1;
    }

    if (dp[r][c] != -1) {
        return dp[r][c];
    }

    dp[r][c] = 0;

    vector<pair<int,int>> dir = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};

    for (auto p : dir) {
        int nr = r + p.first;
        int nc = c + p.second;

        if (0 <= nr && nr < m &&
            0 <= nc && nc < n &&
            board[nr][nc] < board[r][c]) {
            dp[r][c] += dfs(nr, nc);
        }
    }

    return dp[r][c];
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> m >> n;

    board.assign(m, vector<int>(n));
    dp.assign(m, vector<int>(n, -1));

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    cout << dfs(0, 0);
}
