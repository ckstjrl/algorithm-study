#include <iostream>
#include <algorithm>
using namespace std;

int n;
int arr[100000];
int dp[100000];

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> n;

	for (int i = 0; i < n; i++) {
		cin >> arr[i];
	}

	dp[0] = arr[0];
	int maxSum = dp[0];

	for (int i = 1; i < n; i++) {
		dp[i] = max(arr[i], dp[i - 1] + arr[i]);
		maxSum = max(maxSum, dp[i]);
	}

	cout << maxSum << '\n';

	return 0;
}