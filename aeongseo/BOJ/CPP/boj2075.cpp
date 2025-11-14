/*** 2075. N번째 큰 수 ***/

#include<iostream>
#include<queue>
#include<vector>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	int N;
	cin >> N;

	priority_queue<int, vector<int>, greater<int>> pq; // 최소힙 사용
	
	for (int i = 0; i < N*N; i++) {
		int a;
		cin >> a;
		pq.push(a);
		if (pq.size() > N) pq.pop(); // 힙에 N개가 넘으면 pop
	}
	
	cout << pq.top(); // top의 값이 N번째 큰 수

	return 0;
}