/*** 10828. 스택 (D2) ***/

#include<iostream>
#include<string>
using namespace std;

int main() {
	int N;
	cin >> N;

	int top = -1;
	int stack[10000];

	for (int i = 0; i < N; i++) {
		string order;
		int x;
		cin >> order;
		if (order == "push") {	// push일 때 정수 x를 더 받고 top 증가 후 stack에 저장
			cin >> x;
			top++;
			stack[top] = x;
		}
		else if (order == "pop") {	// pop일 때 top=-1이면(스택이 비었으면) -1을 출력, -1이 아니면 top 1 줄이고 맨위 stack 값 출력
			if (top == -1) {
				cout << -1 << '\n';
			}
			else{
				top--;
				cout << stack[top + 1] << '\n';
			}
		}
		else if (order == "size") {	// size일 때 top+1 출력
			cout << top + 1 << '\n';
		}
		else if (order == "empty") {	// empty일 때 top=-1이면(스택이 비었으면) 1 출력, -1아니면 0 출력
			if (top == -1) {
				cout << 1 << '\n';
			}
			else {
				cout << 0 << '\n';
			}
		}
		else if (order == "top") {	// top일 때 top=-1이면(스택이 비었으면) -1 출력, -1 아니면 맨위 stack 값 출력
			if (top == -1) {
				cout << -1 << '\n';
			}
			else {
				cout << stack[top] << '\n';
			}
		}
	}

	return 0;
}