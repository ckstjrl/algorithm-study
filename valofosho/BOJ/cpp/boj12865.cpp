/*
BOJ 12865 - 평범한 배낭

1. 문제 정의
N개의 물건, 무게와 가치는 각각 W, V
배낭에는 K만큼 담을 수 있다.
최대로 담을 수 있는 가치 최댓값을 구하라

로직 정의
1. 물건을 하나하나 추가한다고 생각했을 때
	-> 하나의 물건이 추가되는 것을 DP 테이블로 비교
2. 점화식
	if Wi > j => DP[i][j] = DP[i-1][j] // 해당 물건을 담지 않은 경우로 넘어감(무게가 터지니까)
	else Wi <= j => max(vi+ DP[i-1][j-Wi], DP[i-1][j]) // max(해당 물건을 담고, 그 무게만큼을 뺀 이전 DP, 안담은 무게)
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, K;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> N >> K;
	// DP 테이블을 위해서 0을 채워놓아야 한다. -> N+1, K+1로 만들기!
    vector<vector<int>> dp (N + 1, (vector<int>(K + 1))); // 0부터 N까지 N+1로 만들기
	vector<int> W(N+1);
	vector<int> V(N+1);


	for (int i = 1; i < N+1; i++) {
		cin >> W[i] >> V[i]; // W, V 배열 생성
	}

	for (int i = 1; i < N+1; i++) {
		for (int j = 1; j < K+1; j++) {
			// 물건의 무게가 담을 공간보다 작은 경우
			if (W[i] > j) {
				// 해당 물건이 없을 때의 값과 동일
				dp[i][j] = dp[i - 1][j];
			}
			else {
				dp[i][j] = max(V[i] + dp[i - 1][j - W[i]], dp[i - 1][j]); // 물건을 담은 경우 vs 안담고 이전 배낭 동일하게
			}
		}
	}

	cout << dp[N][K] << '\n';

	return 0;
}