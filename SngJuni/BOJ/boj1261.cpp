#include <iostream>
#include <vector>
#include <queue>       // priority_queue
#include <string>
#include <functional>  // greater<>
#include <climits>     // INT_MAX

using namespace std;

int M, N;
vector<vector<int>> maze;  // 미로 정보를 위한 2차원 가변배열
vector<vector<int>> dist;  // 최소 비용을 위한 2차원 가변배열

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void dijkstra(int i, int j, int c) {
    // 다익스트라를 위한 최소 힙을 pair를 중첩해서 사용 - {현재까지의 비용, {y 좌표, x 좌표}} 
    priority_queue<
        pair<int, pair<int, int>>,
        vector<pair<int, pair<int, int>>>,
        greater<pair<int, pair<int, int>>>
    > pq;
    pq.push({c, {i, j}});
    dist[i][j] = c;

    while (!pq.empty()) {
        int w = pq.top().first;         // 중첩한 pair에 주의해서 값 빼내기
        int y = pq.top().second.first;
        int x = pq.top().second.second;
        pq.pop();

        for (int k = 0; k < 4; k++) {
            int nx = x + dx[k];
            int ny = y + dy[k];
            
            if (nx < 0 || nx >= M || ny < 0 || ny >= N) continue;  // 미로 벗어나면 순회 종료

            int cw = maze[ny][nx] + w;         // 현재 경로의 비용 계산
            if (dist[ny][nx] <= cw) continue;  // 현재 경로의 비용이 더 크면 순회 종료

            pq.push({cw, {ny, nx}});
            dist[ny][nx] = cw;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> M >> N;

    maze.assign(N, vector<int>(M, 0));        // 미로 정보 배열 초기화
    dist.assign(N, vector<int>(M, INT_MAX));  // 최소 비용 배열 초기화

    string s;
    for (int i = 0; i < N; i++) {
        cin >> s;
        for (int j = 0; j < M; j++) {
            maze[i][j] = s[j] - '0';
        }
    }

    dijkstra(0, 0, maze[0][0]);  // (0, 0)에서 시작칸의 비용 포함해서 다익스크라 함수 호출

    cout << dist[N - 1][M - 1] << '\n';  // (N, M) 까지의 최소 비용 결과 출력

    return 0;
}