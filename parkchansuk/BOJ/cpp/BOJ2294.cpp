// BOJ 2294. 동전 2 / G5
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, k;
	cin >> n >> k;

	vector<int> coins(n);
	for (int i = 0; i < n; i++) {
		cin >> coins[i];
	}

	vector<int> dp(k + 1, k + 1);
	dp[0] = 0;
	for (int coin : coins) {
		dp[coin] = 1;
		for (int x = coin+1; x <= k; x++) {
			if (x - coin > 0) {
				dp[x] = min(dp[x], dp[x - coin] + 1);
			}
		}
	}
	if (dp[k] > k) dp[k] = -1;
	cout << dp[k] << "\n";
}

/*
다이나믹프로그래밍 활용
일단 dp 생성하고 k를 만드는 최악의 경우의 수로 채움 = 1원으로 k원 만들기 + 1
이후 동전 한개만 생각하면서 dp를 채우고
이 dp를 가지고 다음 동전들 값을 1로 두고 dp과정을 반복하면서 완성
dp완성 후 만약 dp[k]가 k보다 크다면 불가능한 경우 이므로 dp[k] = -1로 하고 출력
*/