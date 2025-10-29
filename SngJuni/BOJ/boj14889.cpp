#include <iostream>
#include <vector>
#include <cmath>
#include <climits>
#include <algorithm>

using namespace std;

int N, res = INT_MAX;
vector<vector<int>> arr;
vector<bool> used;

void dfs(int start, int cnt) {
    if (cnt == N / 2) {  // N / 2의 사람이 선택되었으면
        int start = 0, link = 0;  // 각 팀 능력치
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                if (used[i] && used[j]) {  // 둘 다 선택된 경우
                    start += arr[i][j] + arr[j][i];
                } else if (!used[i] && !used[j]) {  // 둘 다 선택되지 않은 경우
                    link += arr[i][j] + arr[j][i];
                }
            }
        }
        res = min(res, abs(start - link));  // 최솟값 갱신
    }

    for (int i = start; i < N; i++) {
        if (!used[i]) {  // 선택되지 않은 사람
            used[i] = true;
            dfs(i + 1, cnt + 1);  // 선택하고 다음으로 이동
            used[i] = false;      // 백트래킹
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    arr.assign(N, vector<int>(N, 0));
    used.assign(N, false);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    used[0] = true;  // 첫번째 팀원 표시 
    dfs(1, 1);  // dfs 함수로 완전탐색

    cout << res << '\n';

    return 0;
}