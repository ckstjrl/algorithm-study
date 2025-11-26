/*** 20002. 사과나무 ***/

// 누적합 배열 생성 : 왼쪽 + 위쪽 - 왼쪽위대각선 + 자기자신
// 크기 k를 1부터 N까지 순회
// k에 대해 가능한 시작 좌표 순회
// 해당 정사각형의 합 구하고, 최대값 갱신

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, max_sum = -10000;
	cin >> N;

	vector<vector<int>> apple(N + 1, vector<int>(N + 1, 0));
	vector<vector<int>> sum(N + 1, vector<int>(N + 1, 0));

	for (int i = 1; i < N + 1; i++) {
		for (int j = 1; j < N + 1; j++) {
			cin >> apple[i][j];
			// 누적합 계산
			sum[i][j] = sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1] + apple[i][j];
		}
	}

	for (int k = 1; k < N + 1; k++) {
		for (int i = 1; i <= N - k + 1; i++) { // 시작좌표
			for (int j = 1; j <= N - k + 1; j++) {
				// 끝좌표
				int ei = i + k - 1;
				int ej = j + k - 1;
				// 범위를 벗어나면 continue
				if (ei > N || ej > N) continue;
				// 누적합 계산
				int subsum = sum[ei][ej] - sum[ei - k][ej] - sum[ei][ej - k] + sum[ei - k][ej - k];
				// 최대값 갱신
				max_sum = max(max_sum, subsum);
			}
		}
	}

	cout << max_sum;

	return 0;
}