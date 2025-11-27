#include <iostream>
#include <vector>
#include <deque>
#include <array>
#include <tuple>
#include <string>
#include <climits>

using namespace std;

int W, H;
int dx[4] = {0, 0, -1, 1};  // 상하좌우 델타 배열
int dy[4] = {-1, 1, 0, 0};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> W >> H;
    vector<string> board(H);
    for (int i = 0; i < H; i++) {  // 지도 정보 입력
        cin >> board[i];
    }

    vector<pair<int, int>> C;  // C 지점 2개 찾기
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W; j++) {
            if (board[i][j] == 'C') C.push_back({i, j});
        }
    }

    int si = C[0].first, sj = C[0].second;  // 출발점
    int di = C[1].first, dj = C[1].second;  // 도착점

    // (y, x) 에 dir 방향으로 도착했을 때, 설치한 거울의 최소 갯수
    vector<vector<array<int, 4>>> dist(H, vector<array<int, 4>>(W, {INT_MAX,  INT_MAX, INT_MAX, INT_MAX}));
    // 0-1 BFS를 위한 덱
    deque<tuple<int, int, int>> dq;

    // 시작점은 4 방향 모두 0으로 초기화
    for (int k = 0; k < 4; k++) {
        dist[si][sj][k] = 0;
        dq.emplace_front(si, sj, k);
    }

    // 0-1 BFS 탐색
    while (!dq.empty()) {
        auto cur = dq.front();
        dq.pop_front();

        int y = get<0>(cur);
        int x = get<1>(cur);
        int dir = get<2>(cur);

        int curCost = dist[y][x][dir];

        if (curCost > dist[y][x][dir]) continue;  // 더 비싼 경우 무시

        for (int k = 0; k < 4; k++) {  // 상하좌우 탐색
            int ny = y + dy[k];
            int nx = x + dx[k];
            
            if (nx < 0 || nx >= W || ny < 0 || ny >= H) continue;  // 범위 바깥
            if (board[ny][nx] == '*') continue;

            int add = (dir == k ? 0 : 1);  // 방향이 바뀌면 거울 1개 추가
            int newCost = curCost + add;

            // 더 적은 거울로 도착 가능하면 갱신
            if (newCost < dist[ny][nx][k]) {
                dist[ny][nx][k] = newCost;

                // 0-1 BFS : 가중치 0이면 앞, 1이면 뒤에 삽입
                if (add == 0) dq.emplace_front(ny, nx, k);
                else dq.emplace_back(ny, nx, k);
            }
        }
    }

    // 도착점에 도달했을 때 4 방향 중 최소 거울 갯수 출력
    int res = INT_MAX;
    for (int k = 0; k < 4; k++) {
        res = min(res, dist[di][dj][k]);
    }

    cout << res << '\n';

    return 0;
}