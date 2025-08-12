#include <iostream>
#include <vector>

using namespace std;

int main() {
    int test_case;
    int T;

    cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        int n;
        cin >> n;

        vector<vector<int>> arr(n, vector<int>(n, 0));

        int num = 1;
        int left = 0, right = n - 1, top = 0, bottom = n - 1;

        while (left <= right && top <= bottom) {
            for (int i = left; i <= right; i++) {
                arr[top][i] = num++;
            }
            top++;

            for (int i = top; i <= bottom; i++) {
                arr[i][right] = num++;
            }
            right--;

            for (int i = right; i >= left; i--) {
                arr[bottom][i] = num++;
            }
            bottom--;

            for (int i = bottom; i >= top; i--) {
                arr[i][left] = num++;
            }
            left++;
        }

        cout << "#" << test_case << "\n";
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cout << arr[i][j] << " ";
            }
            cout << "\n";
        }
    }

    return 0;
}