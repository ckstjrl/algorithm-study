#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool check(string &line) { // 특정 라인의 o 갯수를 세서 오목을 판정하는 함수
    int cnt = 0;
    for (auto c : line) {
        if (c == 'o') cnt++;
        else cnt = 0;
        if (cnt >= 5) return true;
    }
    return false;
}

int main() {
    int t;
    cin >> t;

    for (int tc = 1; tc < t + 1; tc++) {
        int n;
        cin >> n;
        vector<string> arr(n);

        for (int i = 0; i < n; i++) cin >> arr[i];

        bool flag = false;

        // 가로 검사
        for (int i = 0; i < n; i++) {
            if (check(arr[i])) flag = true;
        }

        // 세로 검사
        for (int i = 0; i < n; i++) {
            string temp;
            for (int j = 0; j < n; j++) {
                temp += arr[j][i];
            }
            if (check(temp)) flag = true;
        }

        // 우하향 대각선 (왼쪽 변에서 시작) 검사
        for (int start = 0; start < n; start++) {
            string temp;
            for (int i = start, j = 0; i < n && j < n; i++, j++) {
                temp += arr[i][j];
            }
            if (check(temp)) flag = true;
        }
        // 우하향 대각선 (윗쪽 변에서 시작) 검사
        for (int start = 1; start < n; start++) {
            string temp;
            for (int i = 0, j = start; i < n && j < n; i++, j++) {
                temp += arr[i][j];
            }
            if (check(temp)) flag = true;
        }

        // 우상향 대각선 (왼쪽 변에서 시작) 검사
        for (int start = 0; start < n; start++) {
            string temp;
            for (int i = start, j = 0; i >= 0 && j < n; i--, j++) {
                temp += arr[i][j];
            }
            if (check(temp)) flag = true;
        }
        // 우상향 대각선 (아래쪽 변에서 시작) 검사
        for (int start = 1; start < n; start++) {
            string temp;
            for (int i = n - 1, j = start; i >= 0 && j < n; i--, j++) {
                temp += arr[i][j];
            }
            if (check(temp)) flag = true;
        }

        cout << "#" << tc << " ";
        cout << (flag ? "YES" : "NO") << "\n";
    }

    return 0;
}