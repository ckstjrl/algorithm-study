/*
BOJ1912. 연속합

[문제]
n개의 정수로 이루어진 임의의 수열이 주어진다.
우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.
예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자.
여기서 정답은 12+21인 33이 정답이 된다.

[입력]
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

[출력]
첫째 줄에 답을 출력한다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // n: 수열의 정수 개수 (1 ≤ n ≤ 100,000)
    int n;
    cin >> n;

    // 입력받을 정수 배열
    vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    // dp[i]: i번째 원소를 반드시 포함하는 연속된 부분합의 최대값
    vector<int> dp(n);

    // 초기값: 첫 번째 원소가 곧 첫 번째 경우의 최대 연속합
    dp[0] = arr[0];

    // 점화식: dp[i] = max(arr[i], dp[i-1] + arr[i])
    for (int i = 1; i < n; i++) {
        dp[i] = max(arr[i], dp[i - 1] + arr[i]);
    }
    /*  
        점화식:
        - dp[i] = max(arr[i], dp[i-1] + arr[i])

        이유:
        - 현재 원소(arr[i]) 하나만으로 시작하는 것이 더 큰 경우가 있고,
        - 이전까지의 최대 연속합(dp[i-1])에 arr[i]를 이어붙이는 것이 더 큰 경우가 있음.
    */

    // dp 배열 중 가장 큰 값이 정답 (전체 중 최대 연속합)
    cout << *max_element(dp.begin(), dp.end());
    return 0;
}