#include <iostream>
#include <vector>

using namespace std;

int board[9][9];
bool flag = false;  // 스도쿠가 완성되면 더 이상 탐색하지 않기 위한 전역 플래그

// (r, c)에 숫자 v를 넣을 수 있는지 검사
bool check(int r, int c, int v) {
    // 행, 열 검사
    for (int i = 0; i < 9; ++i) {
        if (board[r][i] == v) return false; // 같은 행에 같은 숫자 존재
        if (board[i][c] == v) return false; // 같은 열에 같은 숫자 존재
    }

    // 3 * 3 박스 검사
    int rs = (r / 3) * 3, cs = (c / 3) * 3;
    for (int i = rs; i < rs + 3; ++i)
        for (int j = cs; j < cs + 3; ++j)
            if (board[i][j] == v) return false;

    return true;
}


// DFS + 백트래킹으로 스도쿠 완전탐색
void dfs(int n) {
    if (flag) return;  // 이미 정답을 찾았으면
    if (n == 81) {     // 9 * 9 칸을 모두 채웠으면 정답
        flag = true;
        return;
    }

    int r = n / 9, c = n % 9;  // n번째 행/열
    if (board[r][c] != 0) {    // 이미 채워진 칸이면 다음으로 이동
        dfs(n + 1);
        return;
    }

    for (int i = 1; i <= 9; i++) {      // 1부터 9까지 숫자 순회하면서
        if (!check(r, c, i)) continue;  // 불가능하면 continue

        board[r][c] = i;  // 숫자 넣고
        dfs(n + 1);       // 다음으로 이동

        if (flag) return; // 정답을 찾았으면 종료

        board[r][c] = 0;  // 숫자 되돌림 (백트래킹)
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    // 입력 받기
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cin >> board[i][j];
        }
    }

    dfs(0);  // 0번째 칸부터 dfs로 완전탐색

    // 결과 출력
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << board[i][j] << ' ';
        }
        cout << '\n';
    }

    return 0;
}