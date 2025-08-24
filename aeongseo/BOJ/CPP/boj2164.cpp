/*** 2164. 카드2 ***/

#include<iostream>
#include<deque>
using namespace std;

int main() {
	int N;
	cin >> N;
	deque<int> dq;
	for (int i = 1; i < N+1; i++) {
		dq.push_back(i);	// 빈 덱에 값 추가
	}

	while(dq.size()>1) {	// 덱에 값이 1개 남을 때까지
		// 카드 버리기
		dq.pop_front();	// 맨 왼쪽 값 삭제

		// 맨 위 카드 맨 밑으로 옮기기
		dq.push_back(dq[0]);	// 맨 왼쪽 값을 맨 오른쪽에 추가
		dq.pop_front();	// 맨 왼쪽 값 삭제
	}

	cout << dq[0];

	return 0;
}