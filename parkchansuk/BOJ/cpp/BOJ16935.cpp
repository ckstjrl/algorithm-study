// BOJ 16935. 배열 돌리기 3 / G5
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, M, R;
	cin >> N >> M >> R;

	vector<vector<int>> arr(N, vector<int>(M));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> arr[i][j];
		}
	}
	int op;
	while (R--) {
		cin >> op;
		if (op == 1) {
			reverse(arr.begin(), arr.end());
		}

		else if (op == 2) {
			for (int i = 0; i < N; i++) {
				reverse(arr[i].begin(), arr[i].end());
			}
		}

		else if (op == 3) {
			vector<vector<int>> n_arr(M, vector<int>(N));
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					n_arr[j][N - i - 1] = arr[i][j];
				}
			}
			arr = n_arr;
			swap(N, M);
		}

		else if (op == 4) {
			vector<vector<int>> n_arr(M, vector<int>(N));
			for (int i = 0; i < N; i++) {
				for (int j = 0; j < M; j++) {
					n_arr[M - 1 - j][i] = arr[i][j];
				}
			}
			arr = n_arr;
			swap(N, M);
		}

		else if (op == 5) {
			vector<vector<int>> n_arr(N, vector<int>(M));
			int n = N / 2;
			int m = M / 2;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					n_arr[i][j + m] = arr[i][j];
					n_arr[n + i][m + j] = arr[i][m + j];
					n_arr[n + i][j] = arr[i + n][j + m];
					n_arr[i][j] = arr[n + i][j];
				}
			}
			arr = n_arr;
		}

		else if (op == 6) {
			vector<vector<int>> n_arr(N, vector<int>(M));
			int n = N / 2;
			int m = M / 2;
			for (int i = 0; i < n; i++) {
				for (int j = 0; j < m; j++) {
					n_arr[n + i][j] = arr[i][j];
					n_arr[n + i][m + j] = arr[n + i][j];
					n_arr[i][m + j] = arr[i + n][j + m];
					n_arr[i][j] = arr[i][m + j];
				}
			}
			arr = n_arr;
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cout << arr[i][j] << ' ';
		}
		cout << "\n";
	}
}

/*
들어오는 명령에 따라 배열을 변경하는 로직 구성하여 풀이
알고리즘이나 자료구조보다는 구현에 가까움
*/