#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main (int argc, char** argv) {
	int test_case;
	int T;
	cin >> T;

    for (test_case = 1; test_case <= T; ++test_case) {
        int n;
        cin >> n;

        vector<vector<int>> arr(n, vector<int>(n, 0));
        string s;
        for (int i = 0; i < n; i++) {
            cin >> s;
            for (int j = 0; j < n; j++) {
                arr[i][j] = s[j] - '0';
            }
        }

        int res = 0;
        int mid = n / 2;
        for (int i = 0; i < n; i++) {
            if (i <= n / 2) {
                for (int j = mid - i; j <= mid + i; j++) {
                    res += arr[i][j];
                }
            } else {
                for (int j = mid - n + i + 1; j <= mid + n - i - 1; j++) {
                    res += arr[i][j];
                }
            }
        }

        cout << "#" << test_case << " " << res << "\n";
	}

	return 0;
}