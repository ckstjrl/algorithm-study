/*** 1781. 컵라면 ***/

// 1트
// 데드라인은 오름차순, 컵라면은 내림차순 정렬하는 우선순위 큐 생성 후 값 삽입
// 힙을 돌면서 데드라인이 현재 날짜보다 같거나 커야지만 컵라면 개수를 더한다.
// 해당일에 컵라면을 받았으면 데드라인 다음날로 이동

// 2트
// 우선순위큐 1 : 데드라인 오름차순, 컵라면 내림차순
// 우선순위큐 2 : 컵라면 오름차순. 큐의 개수가 날짜
// pq1에서 pop 하며 pq2에 삽입
// 데드라인이 날짜(pq2의 개수)에 벗어나지 않고 pq1 top의 컵라면이 pq2 top의 컵라면보다 많으면 바꿈

#include<iostream>
#include<queue>
#include<vector>
using namespace std;

int main() {
	int N;
	cin >> N;

	struct Compare { // 데드라인은 오름차순, 컵라면 수는 내림차순 정렬하기 위한 operator
		bool operator()(const pair<int, int>& x, const pair<int, int>& y) const {
			if (x.first != y.first) {
				return x.first > y.first;
			}
			return x.second < y.second;
		}
	};

	priority_queue<pair<int, int>, vector<pair<int, int>>, Compare> pq1; // 데드라인 오름차순, 컵라면 수 내림차순
	priority_queue<int, vector<int>, greater <int>> pq2; // 컵라면 수 오름차순

	for (int i = 0; i < N; i++) {
		int d, c;
		cin >> d >> c;
		pq1.push({ d, c });
	}

	// pq2 일단 값 하나 채우기
	auto [d, c] = pq1.top();
	pq1.pop();
	pq2.push(c);
	while (!pq1.empty()) {
		auto [d, c] = pq1.top();
		pq1.pop();

		if (d <= pq2.size() && c > pq2.top()) { // 데드라인이 pq2의 개수(날짜)보다 크지 않고 컵라면 수가 pq2 top의 개수보다 많으면 갱신
			pq2.pop();
			pq2.push(c);
		}
		else if (d > pq2.size()) pq2.push(c); // 데드라인이 pq2의 개수(날짜)보다 크면 그냥 pq2에 삽입
	}

	int ans = 0;
	while (!pq2.empty()) {
		int c = pq2.top();
		pq2.pop();
		ans += c;
	}

	cout << ans;

	return 0;
}
