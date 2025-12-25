#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;

	for (int tc = 0; tc < T; tc++) {
		int n, m;
		cin >> n >> m;

		vector<int> A(n), B(m);

		for (int i = 0; i < n; i++) cin >> A[i];
		for (int i = 0; i < m; i++) cin >> B[i];

		sort(B.begin(), B.end());

		long long result = 0;
		for (int i = 0; i < n; i++) {
			int cnt = lower_bound(B.begin(), B.end(), A[i]) - B.begin();
			result += cnt;
		}

		cout << result << '\n';
	}

	return 0;
}