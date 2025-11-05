#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int N, res = 1;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int si, int sj, int depth, vector<vector<int>> &b, vector<vector<bool>> &v) {
    queue<pair<int, int>> q;
    q.emplace(si, sj);
    v[si][sj] = true;

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {  // 상하좌우 순회
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;  // 범위 바깥
            if (!v[ny][nx] && b[ny][nx] > depth) {  // 아직 방문하지 않았고, 해당 칸의 높이가 비의 높이보다 높을 때
                q.emplace(ny, nx);
                v[ny][nx] = true;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    vector<vector<int>> board(N, vector<int>(N, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    int max_v = -1;
    for (int i = 0; i < N; i++) {  // 가장 높은 높이 찾기
        max_v = max(max_v, *max_element(board[i].begin(), board[i].end()));
    }

    for (int d = 1; d < max_v; d++) {  // 1부터 가장 높은 높이까지 bfs 탐색
        int cnt = 0;
        vector<vector<bool>> visited(N, vector<bool>(N, false));  // 방문 배열 초기화
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (!visited[i][j] && board[i][j] > d) {  // 아직 방문하지 않았고, 해당 칸의 높이가 비의 높이보다 높을 때
                    bfs(i, j, d, board, visited);
                    cnt++;  // 안전한 영역
                }
            }
        }
        res = max(res, cnt);  // 최댓값 갱신
    }    

    cout << res << '\n';  // 결과 출력

    return 0;
}