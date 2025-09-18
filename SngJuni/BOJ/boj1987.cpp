#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int R, C, res;
vector<string> board;
bool visited[26];  // 각 알파벳이 사용되었는지 체킹하기 위한 배열

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

// 재귀적으로 호출되며 조합을 생성하는 함수
void dfs(int y, int x, int cnt) {
    res = max(res, cnt);  // 매 호출 시마다 최댓값 갱신

    for (int k = 0; k < 4; k++) {  // 델타 배열 순회하면서
        int ny = y + dy[k];
        int nx = x + dx[k];

        if (nx < 0 || nx >= C || ny < 0 || ny >= R) continue;  // 범위 벗어나면 순회 종료

        int cur = board[ny][nx] - 'A';  // 현재 알파벳의 방문 배열에서의 인덱스 값
        if (!visited[cur]) {
            visited[cur] = true;
            dfs(ny, nx, cnt + 1);  // 알파벳 갯수 1 증가시키면서 재귀적으로 조합 생성
            visited[cur] = false;  // 백트래킹
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> R >> C;

    board.assign(R, "");
    for (int i = 0; i < R; i++) {
        cin >> board[i];
    }

    visited[board[0][0] - 'A'] = true;  // (0, 0)칸 방문 체킹
    dfs(0, 0, 1);  // dfs 함수 호출

    cout << res << '\n';

    return 0;
}