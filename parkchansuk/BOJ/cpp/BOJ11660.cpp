// BOJ 11660. 구간 합 구하기 5 / S1
#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N, M;
	cin >> N >> M;

	vector<vector<int>> table(N + 1, vector<int>(N + 1, 0));
	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			cin >> table[i][j];
		}
	}
	vector<vector<long long>> sum(N + 1, vector<long long>(N + 1, 0));

	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + table[i][j];
		}
	}


	for (int m = 0; m < M; m++) {
		int x1, y1, x2, y2;
		cin >> x1 >> y1 >> x2 >> y2;
		cout << sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1] << "\n";
	}
}

/*
누적합 활용
*/