#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
using namespace std;

int sumDigits(const string& s) {
	int sum = 0;
	for (char c : s) {
		if ('0' <= c && c <= '9') {
			sum += c - '0';
		}
	}
	return sum;
}

bool cmp(const string& a, const string& b) {
	// 1. 길이 비교
	if (a.size() != b.size()) 
		return a.size() < b.size();

	// 2. 숫자 합 비교
	int sa = sumDigits(a);
	int sb = sumDigits(b);
	if (sa != sb) 
		return sa < sb;

	// 3. 사전순
	return a < b;
}

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N;

	vector<string> v(N);
	for (int i = 0; i < N; i++) {
		cin >> v[i];
	}

	sort(v.begin(), v.end(), cmp);

	for (int i = 0; i < N; i++) {
		cout << v[i] << '\n';
	}

	return 0;
}