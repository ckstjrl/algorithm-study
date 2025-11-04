/*** 3085. 사탕 게임 ***/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void checkboard();

vector<vector<char>> board;
int di[2] = { 0, 1 };	// 오른쪽, 아래쪽만 확인 (왼쪽, 위쪽은 이전 칸에서 확인함)
int dj[2] = { 1, 0 };
int N;
int maxcnt = 1;

int main() {
	cin >> N;
	board.assign(N, vector<char>(N));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> board[i][j];
		} 
	}

	for (int i = 0; i < N; i++) {	// 모든 칸 확인
		for (int j = 0; j < N; j++) {
			for (int d = 0; d < 2; d++) {
				int ni = i + di[d];
				int nj = j + dj[d];

				if (ni < 0 || ni >= N || nj < 0 || nj >= N) continue;	// 인덱스 벗어나면 continue
				swap(board[i][j], board[ni][nj]);	// 두 칸 swap
				checkboard();	// 최대 길이 확인
				swap(board[i][j], board[ni][nj]);	// 두 칸 원상복구
			}
		}
	}

	cout << maxcnt;

	return 0;
}

void checkboard() {
	// 행 확인
	for (int row = 0; row < N; row++) {
		int cnt = 1;
		for (int col = 1; col < N; col++) {
			if (board[row][col] == board[row][col - 1]) cnt++;	// 같으면 cnt 증가
			else cnt = 1;	// 다르면 cnt 1로 초기화
			maxcnt = max(maxcnt, cnt);
		}
	}

	// 열 확인
	for (int col = 0; col < N; col++) {
		int cnt = 1;
		for (int row = 1; row < N; row++) {
			if (board[row][col] == board[row - 1][col]) cnt++;	// 같으면 cnt 증가
			else cnt = 1;	// 다르면 cnt 1로 초기화
			maxcnt = max(maxcnt, cnt);
		}
	}
}
