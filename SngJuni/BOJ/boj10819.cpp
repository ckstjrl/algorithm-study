#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int N, res = INT_MIN;
vector<int> arr, num;
vector<char> visited;

void dfs(int i) {
    if (i == N) {  // depth가 N이면 -> 모든 정수를 선택했으면, 식에 따라 계산하고 최댓값 갱신
        int temp = 0;
        for (int j = 0; j < N - 1; j++) {
            temp += abs(num[j] - num[j + 1]);
        }
        res = max(res, temp);
        return;
    }
    
    for (int j = 0; j < N; j++) {  // 재귀적으로 탐색하면서 순열 num 만들기
        if (!visited[j]) {
            visited[j] = true;
            num.push_back(arr[j]);
            dfs(i + 1);
            num.pop_back();
            visited[j] = false;
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> N;

    arr.assign(N, 0);  // 정수 입력받을 배열 0으로 초기화
    visited.assign(N, false);  // 방문 배열 false 로 초기화

    for (int i = 0; i < N; i++) cin >> arr[i];  // 정수 배열 입력 받음

    dfs(0);  // dfs 탐색

    cout << res << '\n';  // 결과 출력

    return 0;
}