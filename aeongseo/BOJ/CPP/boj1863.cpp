/*** 1863. 스카이라인 쉬운거 ***/

#include<iostream>
#include<stack>
using namespace std;

int main() {
	int n, x, y;
	cin >> n;
	stack<int> s;

	int cnt = 0;
	for (int i = 0; i < n; i++) {
		cin >> x >> y;
		// 높이 감소할 때
		while (!s.empty() && s.top() > y) {
			s.pop();
			cnt++;
		}
		// 높이 증가할 때 (높이 감소에 사용된 y도 top의 값보다 크면 push)
		if (y > 0 && (s.empty() || s.top() < y)) {
			s.push(y);
		}
	}

	while (!s.empty()) {	// stack에 값이 남아있으면 pop, cnt 증가
		s.pop();
		cnt++;
	}

	cout << cnt;

	return 0;
}