// BOJ 2448. 별 찍기 - 11 / G4
#include <iostream>

using namespace std;

char star[3 * 1024][3 * 2048 - 1];

void point_star(int r, int c, int n) {
	if (n == 3) {
		star[r][c] = '*';
		star[r + 1][c - 1] = '*';
		star[r + 1][c + 1] = '*';
		for (int i = -2; i <= 2; i++) {
			star[r + 2][c + i] = '*';
		}
		return;
	}

	point_star(r, c, n / 2);
	point_star(r + n / 2, c - n / 2, n / 2);
	point_star(r + n / 2, c + n / 2, n / 2);
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 2 * N - 1; j++){
			star[i][j] = ' ';
		}
	}

	point_star(0, N - 1, N);

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < 2 * N - 1; j++) {
			cout << star[i][j];
		}
		cout << '\n';
	}
}

/*
N = 3일 때 모양만 처음에 잡아 놓고
재귀를 통해 계속 복사하는 느낌으로 진행
배열을 ' '로 초기화 하지 않으면 제대로 별이 찍히지 않음.
*/