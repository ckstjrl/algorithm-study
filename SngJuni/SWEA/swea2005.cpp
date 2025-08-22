#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        int n;
        cin >> n;

        vector<vector<int>> arr(n, vector<int>(n, 0));

        for (int i = 0; i < n; i++) {
            arr[i][0] = 1;                // 각 행 첫번째 값
            arr[i][i] = 1;                // 각 행 마지막 값

            for (int j = 1; j < i; j++) { // 바로 위 행의 왼쪽 대각선 행 값 + 바로 위 행의 값
                arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
            }
        }
        cout << "#" << tc << "\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                cout << arr[i][j] << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}