#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int M, N, res;
vector<vector<int>> tomato;
vector<vector<int>> days;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs() {
    queue<pair<int, int>> q;

    int cnt = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (tomato[i][j] == 1) {
                q.emplace(i, j);
            } else if (tomato[i][j] == 0) {
                cnt++;
            }
        }
    }

    if (cnt == 0) {
        res = 0;
        return;
    }

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            
            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            
            if (tomato[ny][nx] == 0) {
                tomato[ny][nx] = 1;
                cnt--;
                days[ny][nx] = days[y][x] + 1;
                q.emplace(ny, nx);
                res = max(res, days[ny][nx]);
            }
        }
    }
    if (cnt > 0) {
        res = -1;
        return ;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> M >> N;
    
    tomato.resize(N, vector<int>(M, 0));
    days.resize(N, vector<int>(M, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            cin >> tomato[i][j];
        }
    }

    bfs();

    cout << res << '\n';

    return 0;
}