#include <iostream>
#include <vector>

using namespace std;

int W, H, res;
vector<vector<int>> arr;
vector<vector<bool>> visited;


// 8방향 델타 배열
int dx[8] = {0, 0, -1, 1, -1, 1, -1, 1};
int dy[8] = {1, -1, 0, 0, 1, 1, -1, -1};

void dfs(int i, int j) {
    visited[i][j] = true;

    for (int k = 0; k < 8; k++) {
        int ny = i + dy[k];
        int nx = j + dx[k];

        if (nx < 0 || nx >= W || ny < 0 || ny >= H) continue;
        if (arr[ny][nx] && !visited[ny][nx]) {  // dfs로 재귀적으로 탐색
            dfs(ny, nx);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    while (true) {
        cin >> W >> H;

        if (!W && !H) break;

        // 매 테스트케이스마다 초기화
        res = 0;
        arr.assign(H, vector<int>(W, 0));
        visited.assign(H, vector<bool>(W, false));

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                cin >> arr[i][j];
            }
        }

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < W; j++) {
                if (arr[i][j] && !visited[i][j]) {
                    dfs(i, j);
                    res++;  // 섬 갯수 증가
                }
            }
        }
        cout << res << '\n';
    }

    return 0;
}