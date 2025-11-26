#include <iostream>
#include <vector>
#include <algorithm>
#include <climits>

using namespace std;

int N;
vector<vector<int>> board;

int get_sum(int y1, int x1, int y2, int x2) {
    return board[y2][x2]               // 정사각형의 우하단 : 전체 영역의 합
            - board[y1 - 1][x2]        // 정사각형의 좌하단 : 제외될 상단 영역의 합
            - board[y2][x1 - 1]        // 정사각형의 우상단 : 제외될 좌측 영역의 합
            + board[y1 - 1][x1- 1];    // 정사각형의 좌상단 : 2번 제외된 부분 다시 더함.
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;

    board.assign(N + 1, vector<int>(N + 1, 0));  // 2차원 누적합을 위한 배열 초기화

    for (int i = 1; i <= N; i++) {  // 입력 받음.
        for (int j = 1; j <= N; j++) {
            cin >> board[i][j];
        }
    }

    for (int i = 1; i <= N; i++) {           // 행 기준 누적합
        for (int j = 2; j <= N; j++) {
            board[i][j] += board[i][j - 1];
        }
    }

    for (int i = 2; i <= N; i++) {           // 열 기준 누적합
        for (int j = 1; j <= N; j++) {
            board[i][j] += board[i - 1][j];
        }
    }

    int res = INT_MIN;

    for (int k = 1; k <= N; k++) {  // K * K 정사각형의 총이익 구하기 위해 1부터 N까지 순회
        for (int i = 1; i <= N - k + 1; i++) {
            for (int j = 1; j <= N - k + 1; j++) {
                int y2 = i + k - 1;
                int x2 = j + k - 1;
                int s = get_sum(i, j, y2, x2);  // 누적합 배열 사용해서 총이익 계산

                res = max(res, s);
            }
        }
    }

    cout << res << '\n';

    return 0;
}