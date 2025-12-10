#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;
    vector<int> arr(N);  // 수열

    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    vector<int> inc(N, 1);  // inc[i] = i에서 끝나는 가장 긴 증가 부분 수열 길이
    vector<int> dec(N, 1);  // dec[i] = i에서 시작하는 가장 긴 감소 부분 수열 길이

    // 왼쪽 → 오른쪽으로 보며 증가 부분 수열 길이 채우기
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                inc[i] = max(inc[i], inc[j] + 1);
            }
        }
    }

    // 오른쪽 → 왼쪽으로 보며 감소 부분 수열 길이 채우기
    for (int i = N - 1; i >= 0; i--) {
        for (int j = N - 1; j > i; j--) {
            if (arr[j] < arr[i]) {
                dec[i] = max(dec[i], dec[j] + 1);
            }
        }
    }

    int res = 0;

    // i를 꼭짓점으로 하는 바이토닉 수열 길이 = 증가 + 감소 - 1
    for (int i = 0; i < N; i++) {
        res = max(res, inc[i] + dec[i] - 1);
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}
