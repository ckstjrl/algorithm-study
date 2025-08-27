/*** 10845. 큐 ***/

#include<iostream>
#include<string>
#include<deque>
using namespace std;

int main() {
	int N, num;
	cin >> N;
	string order;
	deque<int> arr;	// 덱 사용
	for (int i = 0; i < N; i++) {
		cin >> order;
	
		if (order == "push") {	// push일 때 숫자 입력받고 enque
			cin >> num;
			arr.push_back(num);
			//cout << arr.back() << '\n';
		}
		else if (order == "pop") { // pop일 때 덱이 비었으면 -1 출력, 비어있지 않다면 맨앞 숫자 출력 후 deque
			if (arr.empty()) {
				cout << -1 << '\n';
			}
			else {
			cout << arr.front() << '\n';
			arr.pop_front();
			}
		}
		else if (order == "size") { //size일 때 덱의 요소 개수 출력
			cout << arr.size() << '\n';
		}
		else if (order == "empty") {	// empty일 때 덱이 비었으면 1 출력, 비어있지 않다면 0 출력
			if (arr.empty()) {
				cout << 1 << '\n';
			}
			else {
				cout << 0 << '\n';
			}
		}
		else if (order == "front") {	// front일 때 덱이 비었다면 -1 출력, 비어있지 않다면 맨앞 숫자 출력
			if (arr.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << arr.front() << '\n';
			}
		}
		else if (order == "back") {	// back일 때 덱이 비었다면 -1 출력, 비어있지 않다면 맨뒤 숫자 출력
			if (arr.empty()) {
				cout << -1 << '\n';
			}
			else {
				cout << arr.back() << '\n';
			}
		}

	}
	return 0;
}