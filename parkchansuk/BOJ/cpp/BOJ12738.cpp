// BOJ 12738. 가장 긴 증가하는 부분 수열 3 / G2
#include <iostream>
#include <vector>

using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin >> N;

	vector<long long> ans;
	for (int i = 0; i < N; i++) {
		long long num;
		cin >> num;
		if (ans.empty() || num > ans.back()) {
			ans.push_back(num);
		}
		else {
			int l = 0;
			int r = ans.size() - 1;
			while (l < r) {
				int m = (l + r) / 2;
				if (ans[m] >= num) r = m;
				else l = m + 1;
			}
			ans[l] = num;
		}
	}
	cout << ans.size() << "\n";
}

// 시간초과
/*
int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin >> N;

	vector<long long> ans;
	for (int i = 0; i < N; i++) {
		long long num;
		cin >> num;
		if (ans.empty()) {
			ans.push_back(num);
		}
		else {
			int n = ans.size();
			if (num > ans[n - 1]) {
				ans.push_back(num);
			}
			else {
				for (int i = 0; i < n - 1; i++) {
					if (ans[i] <= num && num <= ans[i + 1]) {
						ans[i + 1] = num;
					}
				}
			}
		}
	}
	cout << ans.size() << "\n";
}
*/

/*
vector하나를 만들고 비어있으면 그냥 숫자 넣고
비어 있지 않는 경우 맨 뒤에 있는 숫자와 비교하고 그것보다 크다면 넣고
작으면 ans[i] <= num && num <= ans[i + 1]를 만족하는 ans[i + 1]에 숫자를 넣음
이렇게 하면 계속 반복을 진행해서 시간 초과 발생

시간초과를 해결하기 위해 이분탐색 진행
이분탐색 완료 되면 ans[l]에 숫자를 넣음
*/