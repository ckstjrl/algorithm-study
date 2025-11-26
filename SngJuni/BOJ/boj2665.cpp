#include <iostream>
#include <vector>
#include <deque>
#include <string>
#include <climits>

using namespace std;

int N;
vector<string> board;      // 미로 정보 배열
vector<vector<int>> dist;  // 시작방에서부터 각 방까지의 최단거리를 위한 배열

// 4방향 델타 배열
int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int si, int sj) {
    deque<pair<int, int>> dq;  // 0-1 BFS 탐색을 위한 deque
    dq.emplace_front(si, sj);  // 시작점 초기화
    dist[si][sj] = 0;

    while (!dq.empty()) {
        auto cur = dq.front();
        dq.pop_front();

        int x = cur.second;
        int y = cur.first;

        for (int k = 0; k < 4; k++) {  // 4방향 순회
            int nx = x + dx[k];
            int ny = y + dy[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;  // 범위 바깥

            int cost = (board[ny][nx] == '1' ? 0 : 1);  // 흰 방 : 0, 검은 방 : 1

            if (dist[ny][nx] > dist[y][x] + cost) {  // 현재 거리가 더 짧으면
                dist[ny][nx] = dist[y][x] + cost;    // 최단거리 갱신

                if (cost == 0) dq.emplace_front(ny, nx); // 가중치가 0인 곳부터 먼저 탐색하기 위해 deque의 앞에 push
                else dq.emplace_back(ny, nx);            // 가중치 0인 곳 다 탐색하고 탐색하기 위해 deque의 뒤에 push
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    
    board.assign(N, "");
    dist.assign(N, vector<int>(N, INT_MAX));  

    for (int i = 0; i < N; i++) {
        cin >> board[i];
    }

    bfs(0, 0);  // 0-1 BFS 탐색

    cout << dist[N - 1][N - 1];  // 결과 출력

    return 0;
}