/*** 10472. 십자뒤집기 ***/

#include<iostream>
#include<algorithm>
#include<cstring>
#include<iterator>
using namespace std;

char board[3][3], ans[3][3];// board, ans 배열
bool cell[9];// cell 배열
int P, min_cnt;
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };

void choose(int idx, int m, char current_board[3][3]);

int main() {
	cin >> P; // 테케 입력
	// 테케 반복
	for (int tc = 0; tc < P; tc++) {
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				cin >> ans[i][j]; // ans 입력받기
				board[i][j] = '.'; // board .으로 초기화

			}
		}
		min_cnt = 10; // min_cnt 초기화

		choose(0, 0, board); // 백트랙

		cout << min_cnt << '\n';
	}

	return 0;
}

void choose(int idx, int m, char current_board[3][3]) {
	if (m == 9) { // m == 9이면
		bool flag = true; // 정답 일치 플래그
		// 정답과 비교
		for (int i = 0; i < 3; i++) {
			for (int j = 0; j < 3; j++) {
				if (current_board[i][j] != ans[i][j]) flag = false;
			}
		}

		if (flag) { // 플래그가 true면
			int cnt = count(begin(cell), end(cell), true); // 선택한 칸 개수 세기
			min_cnt = min(min_cnt, cnt); // min_cnt 갱신
		}

		return;
	}

	cell[idx] = false; // 선택 false
	choose(idx + 1, m + 1, current_board); // 현재 배열 그대로 백트랙
	cell[idx] = true; // 선택 true
	char next_board[3][3];
	memcpy(next_board, current_board, sizeof(next_board)); // current_board 복사
	// 델타 사용해 변환
	int ti = idx / 3;
	int tj = idx % 3;
	next_board[ti][tj] = (next_board[ti][tj] == '*') ? '.' : '*';
	for (int d = 0; d < 4; d++) {
		int ni = ti + di[d];
		int nj = tj + dj[d];
		if (ni < 0 || ni >= 3 || nj < 0 || nj >= 3) continue;

		next_board[ni][nj] = (next_board[ni][nj] == '*') ? '.' : '*';
	}
	
	choose(idx + 1, m + 1, next_board); // 바뀐 배열 넘겨 백트랙
}