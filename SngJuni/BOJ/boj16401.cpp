#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int M, N;
    cin >> M >> N;

    vector<long long> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];
    sort(arr.begin(), arr.end());

    long long start = 1;
    long long end = arr[N - 1];
    long long max_cut = 0;

    while (start <= end) {
        long long cut = (start + end) / 2;
        long long cnt = 0;

        for (int i = 0; i < N; i++) {
            cnt += (arr[i] / cut);
        }

        if (cnt >= M) {
            max_cut = cut;
            start = cut + 1;
        } else {
            end = cut - 1;
        }
    }

    cout << max_cut << '\n';

    return 0;
}