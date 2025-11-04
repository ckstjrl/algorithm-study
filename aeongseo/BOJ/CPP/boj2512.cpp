/*** 2512. 예산 ***/

// 예산 총액 넘으면 상한액 감소
// 예산 총액 넘지 않으면 상한액 증가

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> cost;

int main() {
	int N, budget, ans;
	cin >> N;
	
	cost.assign(N, 0);

	int maxcost = 0;
	for (int i = 0; i < N; i++) {
		cin >> cost[i];
		maxcost = max(maxcost, cost[i]);
	}

	cin >> budget;

	int left = 0, right = maxcost;
	while (left <= right) {
		int mid = (left + right) / 2;
		int sum = 0;
		
		for (int i = 0; i < N; i++) {
			sum += min(cost[i], mid);
		}

		if (sum == budget) {
			ans = mid;
			break;
		}
		else if (sum < budget) {
			ans = mid; 
			left = mid + 1;
		}
		else right = mid - 1;
	}
	
	cout << ans;

	return 0;
}