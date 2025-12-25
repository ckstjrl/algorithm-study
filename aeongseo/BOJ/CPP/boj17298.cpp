/*** 17298. 오큰수 ***/

/*
	뒤부터 확인한다
	스택의 top과 현재 값을 비교한다
	top이 더 작으면 pop하고 다음 top과 비교한다
	스택이 비었으면 -1 출력
*/

#include<iostream>
#include<vector>
#include<stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

	int N;
	cin >> N;
	vector<int> num(N, 0);
	for (int i = 0; i < N; i++) {
		cin >> num[i];
	}

	stack<int> s; // 비교 스택
	stack<int> ans; // 정답 스택
	for (int i = N - 1; i >= 0; i--) {
		while (1) { // 비지 않았다면 과정 스택 순회
			if (s.empty()) { // 스택 비었으면 정답에 -1 저장, 비교에 현재값 저장
				ans.push(-1);
				s.push(num[i]);
				break;
			}
			if (num[i] >= s.top()) { // 스택의 top이 현재값보다 크지 않으면 pop 후 다음 top 비교
				s.pop();
				continue;
			}
			else { // 스택의 top이 현재값보다 크면 정답에 top 저장, 비교에 현재값 저장
				ans.push(s.top());
				s.push(num[i]);
				break;
			}
		}
	}

	while (!ans.empty()) {
		cout << ans.top() << ' ';
		ans.pop();
	}

	return 0;
}