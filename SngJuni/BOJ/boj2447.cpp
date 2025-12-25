#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<string> board;

// (y, x) : 현재 블록의 좌상단 좌표
// n : 현재 블록의 크기
// blank : 공백 여부
void dfs(int y, int x, int n, bool blank) {
    if (n == 1) {  // 더이상 쪼갤 수 없으면 공백 또는 * 을 채움.
        board[y][x] = blank ? ' ' : '*';
        return;
    }

    int m = n / 3;  // 현재 블록을 3 * 3으로 다시 나눔.

    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            bool nextBlank = blank || (i == 1 && j == 1);  // 부모 블럭이 이미 공백이거나 현재 불러올 블럭이 공백이면
            dfs(y + i * m, x + j * m, m, nextBlank);  // i * m, j * m 으로 나눠질 블록의 크기만큼씩 나눠줌.
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    board.assign(N, string(N, ' '));  // N * N 2차원 배열 공백으로 초기화

    dfs(0, 0, N, false);  // 27에서부터 시작 (전체 N * N 영역이고 공백 아님)

    for (int i = 0; i < N; i++) {  // 결과 출력
        cout << board[i] << '\n';
    }

    return 0;
}