/*** 12865. 평범한 배낭 ***/

/*
	N: 물건 개수, W: 물건 무게, V: 물건 가치, K: 배낭 최대 무게
	====================
	i는 물건 인덱스, j는 배낭 최대 무게
	dp[i][j] = j 무게에서의 최대 가치
	item[i][2] => item[i][0] : 무게, item[i][1] : 가치
	1. item[i][0] > j (배낭 무게를 넘을 때) : 안넣음 -> 같은 무게에서 이전 물건의 최대값
	2. item[i][0] <= j (배낭 무게를 넘지 않을 때):
		2-1. 안넣음 -> 같은 무게에서 이전 물건의 최대값 dp[i-1][j]
		2-2. 넣음 -> item[i]를 넣으니까 나머지 무게에서 가장 최대값과 더함 item[i][1] + dp[i-1][j-item[i][0]]
					-> 구한 값과 이전 물건의 최대값 중에 더 큰 값 선택 max(dp[i-1][j], item[i][1] + dp[i-1][j-item[i][0]])
*/

#include <iostream>
#include <algorithm>

using namespace std;

int item[101][2], dp[101][100002] = { 0, };

int main() {
	int N, K;
	cin >> N >> K;


	for (int i = 1; i <= N; i++) {
		cin >> item[i][0] >> item[i][1];
	}

	for (int i = 1; i <= N; i++) {
		for (int j = 1; j <= K; j++) {
			auto[w, v] = item[i];

			if (w > j) {
				dp[i][j] = dp[i - 1][j];
			}
			else {
				dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w]);
			}
		}
	}

	cout << dp[N][K];

	return 0;
}