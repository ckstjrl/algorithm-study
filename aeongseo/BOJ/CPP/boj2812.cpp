/*** 2812. 크게 만들기 ***/

#include<iostream>
#include<string>
#include<vector>
#include<stack>
#include<algorithm>
using namespace std;

// stack에 숫자 넣으며 top보다 값 크면 이전꺼 pop()
// 끝까지 다 돌면 남은 만큼 뒤에서 삭제

int main() {
	int N, K;
	string line;
	cin >> N >> K >> line;
	vector<int> num(N, 0);
	for (int i = 0; i < N; i++) {
		num[i] = line[i] - '0';
	}
	
	stack<int> s;	// 스택
	int cnt = K;
	s.push(num[0]);
	for (int i = 1; i < N; i++) {
		while (cnt > 0 && !s.empty() && s.top() < num[i]) {	// 빈 스택이 아니고 지울 수 있는 개수가 남아있으면 top의 값이 현재 값보다 커질 때까지 pop 
			s.pop();
			cnt--;
		}
		s.push(num[i]);	// 현재 값 push
	}
	
	if (!s.empty()) {	// 빈 스택이 아니면 
		for (int i = 0; i < cnt; i++) {	// 남은 지울 개수만큼 pop
			s.pop();
		}
	}

	string ans;	// 정답 출력을 위한 문자열
	while (!s.empty()) {	// 빈 스택이 될 때까지
		char temp = '0' + s.top();	// top 값을 문자로 바꾼 후 ans에 저장
		ans.push_back(temp);
		s.pop();
	}

	reverse(ans.begin(), ans.end());	// 스택에서 값을 뽑았으므로 뒤집어져 있음. 거꾸로 뒤집어줌

	cout << ans;

	return 0;
}