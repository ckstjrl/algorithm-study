#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, res;
bool broken_btn[10];
vector<int> usable_btn;

void dfs(int depth, int maxLen, int val) {
    if (depth > 0) {  // 한 자리 이상 만들어졌을 경우
        int cnt = depth + abs(N - val);  // 숫자 버튼 depth번 사용해서 val까지 이동 후, +-로 N까지 이동
        res = min(res, cnt);  // 최솟값 갱신
    }

    if (depth == maxLen) return;  // 최대 자릿수에 도달하면 종료

    for (auto& i : usable_btn) {      // 사용할 수 있는 각 숫자 버튼을 다음 자리에 추가
        int nxt = val * 10 + i;       // 현재 값 val 뒤에숫자 i 붙임.
        dfs(depth + 1, maxLen, nxt);  // 자릿수 +1 해서 재귀 호출
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> N >> M;
    
    for (int i = 0; i < M; i++) {   // 고장난 버튼
        int x;
        cin >> x;
        broken_btn[x] = true;
    }

    res = abs(N - 100);  // 숫자 버튼 안쓰고 +- 버튼만 사용했을 때 횟수

    for (int i = 0; i <= 9; i++) {  // 고장나지 않은 숫자 버튼
        if (!broken_btn[i]) {
            usable_btn.push_back(i);
        }
    }

    if (!usable_btn.empty()) {  // 고장나지 않은 숫자 버튼이 있을 때 DFS 시도
        for (int i = 1; i <= 6; i++) {  // 만들 수 있는 채널 자릿수 1~6자리 시도
            dfs(0, i, 0);
        }
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}