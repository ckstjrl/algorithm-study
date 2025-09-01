#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool comp(pair<int, int> p1, pair<int, int> p2) {  // 조건을 나눠서 정렬 기준을 정해주기 위한 comp 함수
	if (p1.first == p2.first) {
		return p1.second < p2.second;
	}
	return p1.first < p2.first;
}

int main() {
	int n, x, y;
	cin >> n;

	vector<pair<int, int>> arr;

	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		arr.push_back({ x, y });
	}
	
	sort(arr.begin(), arr.end(), comp);            // sort 의 세번째 인자로 comp 함수 넣어줌.

	for (int i = 0; i < n; i++) {
		cout << arr[i].first << " " << arr[i].second << "\n";
	}

	return 0;
}