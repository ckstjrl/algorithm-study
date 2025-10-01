#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n, x;
    cin >> n;

    vector<int> arr(n);
    for (int i = 0; i < n; i++) cin >> arr[i];

    cin >> x;

    sort(arr.begin(), arr.end());

    int res = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] + arr[j] > x) break;
            if (arr[i] + arr[j] == x) {
                res++;
                break;
            }
        }
    }
    
    cout << res << '\n';

    return 0;
}