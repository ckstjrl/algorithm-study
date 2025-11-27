/*
BOJ 1756 - 피자굽기

문제 정의
1. N개의 피자 반죽을 오븐에 넣으려 하는데 피자 반죽의 지름은 제각각
2. 오븐의 모양도 각 깊이마다 지름이 다르다.
3. 피자 N개가 모두 오븐에 들어간 뒤 맨 위의 피자가 얼마나 깊이 있는지 궁금하다
4. 피자가 모두 들어가면 오븐의 최상단을 1로 두고 피자 위치 출력 or 안되면 0 출력

로직 생각
문제를 처음 보고 느낀 점은 그냥 하나하나 넣어가면서 stack처럼 헤드 내리거나 pop 해서 끝자리까지 다 pop하고
남은 자리까지 못들어가면 터지게
우선 스택 풀이 갑니다 숑숑

*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int D, N;

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> D >> N;

	vector<int> oven(D);
	vector<int> pizza(N);

	for (int i = 0; i < D; i++) {
		cin >> oven[i];
	}
	// 피자가 들어가는 입구도 맞춰주기
	for (int i = 1; i < D; i++) {
		oven[i] = min(oven[i - 1], oven[i]);
	}

	for (int i = 0; i < N; i++) {
		cin >> pizza[i];
	}
	
	for (int i = 0; i < N; i++) {
		bool flag = false;
		while (!flag && !oven.empty()) {
			// 피자가 들어갈 수 있으면 pop_back, flag=True
			if (oven.back() >= pizza[i]) {
				oven.pop_back();
				flag = true;
			}
			else {
				// 일단 해당 칸 팝
				oven.pop_back();
			}
		}
		// 피자가 못낑기면 0 출력 종료
		if (flag == false) {
			cout << 0;
			return 0;
		}
	}
	cout << oven.size()+1;
	return 0;
}