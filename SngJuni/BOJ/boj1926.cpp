#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int n, m;
vector<vector<int>> arr;
vector<vector<bool>> visited;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int bfs(int i, int j) {
    int cnt = 0;
    queue<pair<int, int>> q;
    q.emplace(i, j);
    visited[i][j] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();
        cnt++;

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
            if (!visited[ny][nx] && arr[ny][nx]) {
                q.emplace(ny, nx);
                visited[ny][nx] = true;
            }
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    arr.assign(n, vector<int>(m, 0));
    visited.assign(n, vector<bool>(m, false));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    int res = 0, max_res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!visited[i][j] && arr[i][j]) {
                res++;
                max_res = max(max_res, bfs(i, j));
            }
        }
    }  

    cout << res << '\n';
    cout << max_res << '\n';

    return 0;
}