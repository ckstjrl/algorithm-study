/*** 13305. 주유소 ***/

#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
using namespace std;

int main() {
	long N;
	cin >> N;
	
	vector<long> distance(N - 1);
	vector<long> oil(N);
	for (int i = 0; i < N - 1; i++) {
		cin >> distance[i];
	}
	for (int j = 0; j < N; j++) {
		cin >> oil[j];
	}

	long min_oil = 1000000000;	// 기름 최소 가격
	long cost = 0;	// 총 비용
	for (int i = 0; i < N-1; i++) {
		min_oil = min(min_oil, oil[i]);	// 최소 가격 갱신
		cost += min_oil * distance[i];	// 비용 계산
	}

	cout << cost;

	return 0;
}