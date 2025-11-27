#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    cin >> T;

    while (T--) {
        long long res = 0;
        long long max_price = 0;

        int N;
        cin >> N;

        vector<long long> arr(N);
        for (int i = 0; i < N; i++) cin >> arr[i];

        for (int i = N - 1; i >= 0; i--) {
            if (arr[i] > max_price) {
                max_price = arr[i];
            } else {
                res += max_price - arr[i];
            }
        }

        cout << res << '\n';
    }

    return 0;
}