#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <tuple>

using namespace std;


int n, l;               // n, l을 전역 변수로 선언
int res;                // 최종 결과를 위한 변수
vector<int> scores;     // 맛에 대한 점수들을 위한 가변 배열
vector<int> calories;   // 칼로리들을 위한 가변 배열

void reset(int n) {     // 각 테스트 케이스마다 전역 선언한 변수 및 배열 초기화
    res = 0;
    scores.resize(n);
    calories.resize(n);
}

void dfs() {                              // stack 을 활용해서 dfs로 구현
    stack<tuple<int, int, int>> stk;      // 필요한 값이 3개라서 tuple 사용
    stk.push({0, 0, 0});                  // 초기값 stack에 push

    while (!stk.empty()) {
        auto top = stk.top();
        int depth = get<0>(top);
        int total_score = get<1>(top);
        int total_cal = get<2>(top);
        stk.pop();

        if (total_cal > l) continue;      // 칼로리들의 합이 l보다 크면 아래 코드 건너뜀.

        res = max(res, total_score);      // 최대 맛 점수 갱신
        
        for (int i = depth; i < n; i++) { // 재료를 선택해서 합산하는 모든 경우의 수 계산
            stk.push({i + 1, total_score + scores[i], total_cal + calories[i]}); 
        }
    }
}

int main (int argc, char** argv) {
	int test_case;
	int T;
    cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
        cin >> n >> l;

        reset(n);

        for (int i = 0; i < n; i++) {
            cin >> scores[i] >> calories[i];
        }

        dfs();
        
        cout << "#" << test_case << " " << res << "\n";
	}

	return 0;
}