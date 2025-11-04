/*** 1406. 에디터 ***/

#include<iostream>
#include<string>
#include<algorithm>
#include<stack>
using namespace std;

int main() {
	stack<char> left, right;	// 커서 기준 왼쪽 문자와 오른쪽 문자 저장할 stack
	string txt, order;
	int cnt;
	cin >> txt >> cnt;

	for (int i = 0; i < txt.size(); i++) {	//입력받은 문자열 left에 모두 저장
		left.push(txt[i]);
	}
	for (int j = 0; j < cnt; j++) {	// 
		cin >> order;
		if (order == "L") {
			if (left.size() == 0) continue;	// left 스택이 비어있으면 아무것도 안함
			right.push(left.top());	// left의 top의 값을 오른쪽으로 이동 (커서 왼쪽으로 이동)
			left.pop();
		}
		else if (order == "D") {
			if (right.size() == 0) continue;	// right 스택이 비어있으면 아무것도 안함
			left.push(right.top());	// right의 top의 값을 왼쪽으로 이동 (커서 오른쪽으로 이동)
			right.pop();
		}
		else if (order == "B") {
			if (left.size() == 0) continue;	// left 스택이 비어있으면 아무것도 안함
			left.pop();	// left의 top pop
		}
		else if (order == "P") {
			char x;
			cin >> x;	// 추가할 값 입력받음
			left.push(x);	// left에 push
		}
	}
	string ans;
	while (!left.empty()) {	// left 스택이 빌 때까지
		ans.push_back(left.top());	// ans 에 값 추가
		left.pop();
	}
	reverse(ans.begin(), ans.end());	// ans reverse

	while (!right.empty()) {	// right 스택 빌 때까지
		ans.push_back(right.top());	// ans에 값 추가
		right.pop();
	}
	
	cout << ans;
	
	return 0;
}