/*** 1655. 가운데를 말해요 ***/

// 작은 수를 저장할 최대힙과, 큰 수를 저장할 최소힙을 만든다
// 일단 최대힙에 넣고 최대힙의 원소 개수가 같거나 최소힙 + 1 보다 크다면 최소힙으로 top 값을 옮긴다
// 최대힙의 top을 출력한다

#include<iostream>
#include<queue>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	priority_queue<int> lo;
	priority_queue<int, vector<int>, greater<int>> hi;

	for(int i = N; i > 0; i--) {
		int a;
		cin >> a;
		lo.push(a);

		hi.push(lo.top());
		lo.pop();

		if (lo.size() < hi.size()) {
			lo.push(hi.top());
			hi.pop();
		}

		cout << lo.top() << '\n';
	}

	return 0;
}