#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<long long> dist(N - 1);
    vector<long long> gas(N);

    for (int i = 0; i < N - 1; i++) cin >> dist[i];
    for (int i = 0; i < N; i++) cin >> gas[i];

    long long cur_min = gas[0];
    long long res = gas[0] * dist[0];
    for (int i = 1; i < N - 1; i++) {
        if (cur_min > gas[i]) cur_min = gas[i];
        res += (cur_min * dist[i]);
    }

    cout << res << '\n';

    return 0;
}