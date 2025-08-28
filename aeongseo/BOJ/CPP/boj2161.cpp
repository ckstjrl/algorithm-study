/*** 2161. 카드1 ***/

#include<iostream>
#include<deque>
using namespace std;

int main() {
	int N;
	cin >> N;
	deque<int> card;
	for (int i = 1; i < N + 1; i++) {	//1부터 N까지 카드 생성
		card.push_back(i);
	}
	while (card.size() > 1) {	// 카드가 한장 남을 때까지
		cout << card.front() << ' ';	// 가장 앞에 있는 카드 출력
		card.pop_front();	// 가장 앞에 있는 카드 버림
		card.push_back(card.front());	// 가장 앞에 있는 카드 뒤에 추가
		card.pop_front();	// 가장 앞에 있는 카드 버림
	}
	cout << card.front();	// 마지막에 남은 카드 출력
	return 0;
}