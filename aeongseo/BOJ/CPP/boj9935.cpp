/*** 9935. 문자열 폭발 ***/

// stack에 넣고 top의 값이 폭발 문자열의 마지막 글자면 stack의 폭발 문자열 크기만큼 일치하는지 확인
// 아니면 계속 push, 맞으면 pop

#include<iostream>
#include<string>
#include<vector>
using namespace std;

int main(){
	string s, bomb;
	cin >> s >> bomb;
	vector<char> stack;

	int bl = bomb.size();

	for (char c : s) {
		stack.push_back(c);	// 일단 문자 stack에 push
		int sl = stack.size();	// stack의 길이가 변하므로 for문을 돌 때마다 새로 정의
		if (c == bomb[bl - 1] && sl >= bl) {
			bool flag = true;	// 모든 문자열이 일치하는지 확인하기 위한 플래그
			for (int i = 0; i < bl; i++) {
				if (stack[sl - 1 - i] != bomb[bl - 1 - i]) {	// stack의 문자와 폭발의 문자가 다르면 플래그 false 후 종료
					flag = false;
					break;
				}
			}
			if (flag) {	// 모든 문자열이 일치하면 폭발 문자열 길이만큼 pop
				for (int i = 0; i < bl; i++) {
					stack.pop_back();
				}
			}
		}
	}

	if (!stack.empty()) {	// stack이 비지 않았다면 stack의 문자열 출력
		for (int i = 0; i < stack.size(); i++) cout << stack[i];
	}
	else cout<< "FRULA";	// 비었다면 FRULA 출력

	return 0;
}