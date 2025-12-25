#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
vector<vector<int>> arr;
vector<vector<bool>> visited;

// 8방향 델타 배열
int dx[8] = {-1, 0, 1,-1, 1,-1, 0, 1};
int dy[8] = {-1,-1,-1, 0, 0, 1, 1, 1};

bool bfs(int si, int sj) {
    queue<pair<int, int>> q;
    q.emplace(si, sj);
    visited[si][sj] = true;

    int h = arr[si][sj];  // 현재 구역의 높이
    bool flag = true;     // 봉우리 여부

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 8; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;
            if (arr[ny][nx] > h) {  // 인접 칸이 더 높다면 봉우리 아님
                flag = false;
            }
            if (!visited[ny][nx] && arr[ny][nx] == h) {  // 아직 방문하지 않았고, 높이가 같으면 같은 구역으로 연결
                q.emplace(ny, nx);
                visited[ny][nx] = true;
            }
        }
    }

    return flag;  // 인접한 더 높은 칸이 없으면 봉우리
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> M;

    arr.assign(N, vector<int>(M, 0));           // 농장 정보 초기화
    visited.assign(N, vector<bool>(M, false));  // 방문 배열 초기화

    for (int i = 0; i < N; i++) {  // 농장 정보 입력
        for (int j = 0; j < M; j++) {
            cin >> arr[i][j];
        }
    }

    int res = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (!visited[i][j] && arr[i][j] >= 0) {  // bfs 탐색
                if (bfs(i, j)) res++;
            }
        }
    }

    cout << res << '\n';

    return 0;
}