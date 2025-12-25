/*** 2504. 괄호의 값 ***/

/*
	열린 괄호면 temp 곱
	닫힌 괄호일 때 이전이 열린 괄호면 ans에 더하고 temp 나눔
	이전이 닫힌 괄호이면 temp 나눔
*/

#include<iostream>
#include<stack>
#include<string>
using namespace std;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	stack<char> s;
	string bracket;
	int temp = 1, ans = 0;

	cin >> bracket;

	for (int i = 0; i < bracket.size(); i++) {
		char cur = bracket[i];

		if (cur == '(') {
			temp *= 2;
			s.push('(');
		}
		else if (cur == '[') {
			temp *= 3;
			s.push('[');
		}
		else if (cur == ')') {
			if (s.empty() || s.top() != '(') { // 스택이 비었거나 괄호 짝이 안맞으면 break
				ans = 0;
				break;
			}
			if (bracket[i - 1] == '(') ans += temp; // 이전 괄호가 열린 괄호면  ans에 더함
			temp /= 2;
			s.pop();
		}
		else {
			if (s.empty() || s.top() != '[') { // 스택이 비었거나 괄호 짝이 안맞으면 break
				ans = 0;
				break;
			}
			if (bracket[i - 1] == '[') ans += temp; // 이전 괄호가 열린 괄호면  ans에 더함
			temp /= 3;
			s.pop();
		}
	}

	if (!s.empty()) ans = 0; // 순회 끝났는데 스택이 비어있지 않으면 올바르지 않은 괄호열

	cout << ans;

	return 0;
}