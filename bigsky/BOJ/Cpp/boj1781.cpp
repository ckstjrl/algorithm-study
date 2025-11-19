#include <iostream>
#include <vector>
#include <queue>

using namespace std;

const int MAX = 200000;
vector<int> problems[MAX + 1]; // // problems[deadline] : 데드라인에 대한 문제들의 라면 수

int main() {
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int N;
	cin >> N; // N : 숙제의 개수

	for (int i = 0; i < N; i++) {
		int deadline, cup_ramen;
		cin >> deadline >> cup_ramen;
		problems[deadline].push_back(cup_ramen);
	}

	priority_queue<int> pq; // 최대 힙
	long long total = 0;

	for (int day = N; day >= 1; day--) {
		// 오늘 마감되는 문제 pq에 넣기
		for (int cup_ramen : problems[day]) {
			pq.push(cup_ramen);
		}
		// 오늘 풀 수 있는 문제들 중 가장 많이 라면 주는 것 풀기
		if (!pq.empty()) {
			total += pq.top();
			pq.pop();
		}
	}

	cout << total;
	return 0;
}