// BOJ 1253. 좋다 / G4
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int N;
	cin >> N;

	vector<long long> num(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}

	sort(num.begin(), num.end());
	int cnt = 0;

	for (int i = 0; i < N; i++) {
		int l = 0;
		int r = N-1;
		while (l < r) {
			if (l != i && r != i) {
				if (num[l] + num[r] > num[i]) {
					r--;
				}
				else if (num[l] + num[r] < num[i]) {
					l++;
				}
				else if (num[l] + num[r] == num[i]) {
					cnt++;
					break;
				}
			}
			else if (l == i) l++;
			else if (r == i) r--;
		}
	}
	cout << cnt << "\n";
}

/*
정렬 후 이분탐색으로 진행
num[l]+num[r]을 num[i]와 크기 비교해서 진행
l과 r은 i가 될 수 없다는 부분을 꼭 체크해야함.
*/