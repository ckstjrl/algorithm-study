#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, L, R;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

void bfs(int si, int sj, 
         const vector<vector<int>>& b, 
         vector<vector<int>>& l,
         vector<int>& gs, vector<int>& gc,
         int s) {
    queue<pair<int, int>> q;
    q.emplace(si, sj);
    l[si][sj] = s;       // 연합 라벨
    gc[s] = 1;           // 해당 연합을 이루고 있는 칸의 갯수
    gs[s] += b[si][sj];  // 해당 연합의 인구수

    while (!q.empty()) {
        int y = q.front().first;
        int x = q.front().second;
        q.pop();

        for (int k = 0; k < 4; k++) {
            int ny = y + dy[k];
            int nx = x + dx[k];

            if (nx < 0 || nx >= N || ny < 0 || ny >= N) continue;

            int diff = abs(b[y][x] - b[ny][nx]);

            if (l[ny][nx] == 0 && diff >= L && diff <= R) {
                q.emplace(ny, nx);
                l[ny][nx] = s;
                gc[s]++;
                gs[s] += b[ny][nx];
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N >> L >> R;
    vector<vector<int>> board(N, vector<int>(N, 0));  // 인구 정보 입력

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> board[i][j];
        }
    }

    int res = 0;
    while (true) {
        vector<vector<int>> label(N, vector<int>(N, 0));     // BFS 라벨링, 연합끼리 같은 숫자
        vector<int> gsum(N * N + 1, 0), gcnt(N * N + 1, 0);  // 연합의 인구수, 연합 칸 수

        int start = 1;  // 연합 번호 1부터 시작
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (label[i][j] == 0) {
                    bfs(i, j, board, label, gsum, gcnt, start);  // bfs 탐색하면서 연합을 찾아서 라벨링
                    start++;
                }
            }
        }

        if (start == (N * N) + 1) break;  // 연합 번호가 N * N + 1이면 연합 존재 X -> 종료


        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int g = label[i][j];
                board[i][j] = gsum[g] / gcnt[g];  // 연합을 이루고 있는 각 칸의 인구수 조정
            }
        }
        
        res++;  // 1일 증가

    }

    cout << res << '\n';

    return 0;
}