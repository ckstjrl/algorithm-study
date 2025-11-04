#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int N;
    cin >> N;

    vector<pair<int, int>> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i].second >> arr[i].first;
    }

    sort(arr.begin(), arr.end());

    int res = 0, et = 0;
    for (int i = 0; i < N; i++) {
        if (arr[i].second >= et) {
            res++;
            et = arr[i].first;
        }
    }

    cout << res << '\n';

    return 0;
}