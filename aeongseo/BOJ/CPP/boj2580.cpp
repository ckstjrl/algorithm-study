/*** 2580. 스도쿠 ***/

// 빈칸 찾기
// 가로, 세로, 3x3에 같은 수가 없으면 넣기
// 있으면 백트랙

#include<iostream>
#include<vector>
using namespace std;

bool backtrack(int cur);
bool check(int r, int c, int i);

int board[9][9];
vector<pair<int, int>> blanks;

int main() {
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cin >> board[i][j];
			if (!board[i][j]) blanks.push_back({ i, j });	// board 값이 0이면 빈칸 배열에 추가
		}
	}

	backtrack(0);	// 백트래킹으로 값 채우기

	// 스도쿠 출력
	for (int i = 0; i < 9; i++) {
		for (int j = 0; j < 9; j++) {
			cout << board[i][j] << ' ';
		}
		cout << '\n';
	}

	return 0;
}

bool backtrack(int cur) {
	if (cur == blanks.size()) return true;	// 현재 칸이 빈칸 배열의 개수와 같으면 종료 (true로 반환해 true를 타고 함수 밖으로 나가도록?)

	auto [r, c] = blanks[cur];	// 저장한 좌표를 r과 c에 할당 (C++17부터 가능)

	for (int i = 1; i < 10; i++) {
		if (check(r, c, i)) {	// check가 true면 그 값 채우기
			board[r][c] = i;
			if(backtrack(cur + 1)) return true;	// 다음 백트래킹을 했을 때 값이 true면 true 계속 반환
			else board[r][c] = 0;	// false면 겹치는 수가 발생했다는 의미이므로 다시 빈칸으로 만듦
		}
	}
	return false;
}

bool check(int r, int c, int i) {	// 겹치지 않는 숫자 찾는 함수

	// 가로
	for (int nc = 0; nc < 9; nc++) {
		if (board[r][nc] == i) return false;	// 겹치는 수 있으면 false 반환
	}

	// 세로
	for (int nr = 0; nr < 9; nr++) {
		if (board[nr][c] == i) return false;	// 겹치는 수 있으면 false 반환
	}

	// 3x3
	int sr = (r / 3) * 3;
	int sc = (c / 3) * 3;
	for (int nr = sr; nr < sr + 3; nr++) {
		for (int nc = sc; nc < sc + 3; nc++) {
			if (board[nr][nc] == i) return false;	// 겹치는 수 있으면 false 반환
		}
	}

	return true;	// 모든 경우에서 겹치는 수 없으면 true 반환
}