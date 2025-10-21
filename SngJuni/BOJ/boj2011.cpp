#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int dp[5001];

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    string n;
    cin >> n;

    if (n[0] == '0') {  // 맨 앞자리가 0이면 해석 불가능
        cout << "0\n";
        return 0;
    }

    dp[0] = 1;  // 빈 문자열 -> 경우의 수 : 1
    dp[1] = 1;  // 첫번째 숫자가 0이 아니므로, 경우의 수 : 1

    for (int i = 2; i <= n.size(); i++) {
        // 현재 문자가 0이 아니면, 직전의 경우의 수를 받음.
        if (n[i - 1] != '0') {
            dp[i] = dp[i - 1];
        }

        int tmp = stoi(n.substr(i - 2, 2));  // 바로 앞 두 자리 수
        if (tmp >= 10 && tmp <= 26) {  // 유효한 두 자리 수라면
            dp[i] = (dp[i] + dp[i - 2]) % 1000000;  // dp[i - 2]에서 이어서 가능
        }
    }

    cout << dp[n.size()] % 1000000;  // 문자열 전체의 해석 가능한 경우의 수
    return 0;
}
