#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, K, R;
int dx[4] = {0, 0, -1, 1};  // 상하좌우 델타 배열
int dy[4] = {-1, 1, 0, 0};

// 두 인접 칸 (r1,c1) -> (r2,c2)로 나아갈 때의 방향 인덱스 계산
int dirFromTo(int r1, int c1, int r2, int c2) {
    if (r2 == r1 - 1 && c2 == c1) return 0; // 상
    if (r2 == r1 + 1 && c2 == c1) return 1; // 하
    if (r2 == r1 && c2 == c1 - 1) return 2; // 좌
    if (r2 == r1 && c2 == c1 + 1) return 3; // 우

    return -1; // 인접하지 않음
}

// (si, sj)에서 시작해서 길(막힘)을 피해서 도달 가능한 칸들을 bfs 로 탐색
// blocked[r][c][d] == true 면 (r,c)에서 d 방향으로 이동이 막힘
void bfs(int sy, int sx, bool blocked[101][101][4], vector<vector<bool>>& vis) {
    vis.assign(N + 1, vector<bool>(N + 1, false));  // 방문 배열 초기화

    queue<pair<int,int>> q;
    q.emplace(sy, sx);   // 시작점 처리
    vis[sy][sx] = true;

    while (!q.empty()) {
        auto cur = q.front();
        q.pop();
        int y = cur.first;
        int x = cur.second;

        for (int k = 0; k < 4; k++) {  // 4 방향 탐색
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (nx < 1 || nx > N || ny < 1 || ny > N) continue; // 격자 범위 밖
            if (blocked[y][x][k]) continue;                     // 현재 방향이 막힘

            if (!vis[ny][nx]) {
                q.emplace(ny, nx);
                vis[ny][nx] = true;
            }

        }
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> K >> R;

    bool blocked[101][101][4] = {false};  // 각 칸에서 4 방향으로 이동 가능 여부

    // R개의 막힌 길 입력
    int r1, c1, r2, c2;
    for (int i = 0; i < R; i++) {
        cin >> r1 >> c1 >> r2 >> c2;

        int d1 = dirFromTo(r1, c1, r2, c2);
        int d2 = dirFromTo(r2, c2, r1, c1);
        blocked[r1][c1][d1] = true;  // (r1, c1) -> (r2, c2) 막힘
        blocked[r2][c2][d2] = true;  // (r2, c2) -> (r1, c1) 막힘
    }

    // 소 위치 입력
    vector<pair<int,int>> cows(K);
    for (int i = 0; i < K; i++) {
        cin >> cows[i].first >> cows[i].second;
    }

    long long res = 0;
    vector<vector<bool>> vis; // BFS 방문 결과 재사용

    // 각 소 i에서 bfs 후, i 보다 큰 j 인 소의 위치가 미방문이면 도달 불가
    for (int i = 0; i < K; i++) {
        int si = cows[i].first, sj = cows[i].second;

        bfs(si, sj, blocked, vis);

        for (int j = i + 1; j < K; j++) {
            int ti = cows[j].first, tj = cows[j].second;

            if (!vis[ti][tj]) res++;  // 도달 불가 -> 서로 만날 수 없음
        }
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}
