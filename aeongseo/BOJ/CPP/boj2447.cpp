/*** 2447. 별 찍기 - 10 ***/

// 별 찍을 배열을 공백으로 만듦
// 별 찍어야 할 자리에 *로 채우면 자동으로 공백과 * 로 구분됨
// 3x3으로 구역을 나누고, (1, 1)이면 공백으로 둠
// 함수의 매개변수로 좌표와 한 블록의 크기를 받음

#include<iostream>
#include<vector>
using namespace std;

void star(int r, int c, int n);

vector<vector<char>> board;
int N;

int main() {
	cin >> N;
	board.assign(N, vector<char>(N, ' '));	// 공백으로 별 찍을 판 만듦
	star(0, 0, N);
	
	// 별 출력
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cout << board[i][j];
		}
		cout << '\n';
	}
	return 0;
}

void star(int r, int c, int n) {
	if (n == 1) {	// 블록의 크기가 1이면 * 저장
		board[r][c] = '*';
		return;
	}

	// 3x3으로 나눔
	int block = n / 3;

	for (int i = 0; i < 3; i++) {	// 3x3 좌표
		for (int j = 0; j < 3; j++) {
			if (i == 1 && j == 1) continue; // 가운데면 pass
			else star(r + i * block, c + j * block, block); // 아니면 재귀
		}
	}
}