/*** 4949. 균형잡힌 세상 ***/

#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main() {
	string txt;
	while (getline(cin, txt)) {	// 입력이 들어오면 반복
		if (txt == ".") break;	// 종료조건인 . 하나만 들어오면 반복 종료

		string ans = "yes";	// 답 초기값 yes로 설정

		stack<int> s;
		for (int i = 0; i < txt.length(); i++) {
			if (txt[i] == '(' || txt[i] == '[') {	// 여는 괄호면 push
				s.push(txt[i]);
			}
			else if (txt[i] == ')' || txt[i] == ']') {
				if (s.size() == 0) {	// 닫는 괄호와 매치할 괄호가 없다면 no 저장, 종료
					ans = "no";
					break;
				}
				else {
					if (txt[i] == ')' && s.top() == '(') {	// 소괄호가 짝이 맞는다면 pop
						s.pop();
						continue;
					}
					else if (txt[i] == ']' && s.top() == '[') { // 대괄호가 짝이 맞는다면 pop
						s.pop();
						continue;
					}
					else {	// 짝이 맞지 않는다면 no 저장, 종료
						ans = "no";
						break;
					}
				}
			}
		}
		if (s.size() != 0) {	// 문자열이 끝났는데 스택에 괄호가 남아있다면 no 저장
			ans = "no";
		}

		cout << ans << '\n';
	}
	return 0;
}