#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int M, N, K;
vector<vector<int>> arr;
vector<vector<bool>> visited;
vector<int> res;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int bfs(int i, int j) {
    queue<pair<int, int>> q;
    q.emplace(i, j);
    visited[i][j] = true;
    int cnt = 1;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= M) continue;
            if (!visited[ny][nx] && !arr[ny][nx]) {
                q.emplace(ny, nx);
                visited[ny][nx] = true;
                cnt++;
            }
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> M >> N >> K;
    
    arr.assign(M, vector<int>(N, 0));
    visited.assign(M, vector<bool>(N, false));

    int x1, y1, x2, y2;
    for (int i = 0; i < K; i++) {
        cin >> x1 >> y1 >> x2 >> y2;

        for (int y = y1; y < y2; y++) {
            for (int x = x1; x < x2; x++) {
                arr[y][x] = 1;
            }
        }
    }
    for (int i = 0; i < M; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j] && !arr[i][j]) {
                res.push_back(bfs(i, j));
            }
        }
    }

    sort(res.begin(), res.end());
    cout << res.size() << '\n';
    for (int i = 0; i < res.size(); i++) {
        cout << res[i] << ' ';
    }
    cout << '\n';

    return 0;
}