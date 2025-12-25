#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<pair<int, int>> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i].first >> arr[i].second;
    }

    sort(arr.begin(), arr.end());

    priority_queue<int, vector<int>, greater<int>> pq;

    for (int i = 0; i < N; i++) {
        int deadline = arr[i].first;
        int ramen = arr[i].second;

        pq.push(ramen);
        if (pq.size() > deadline) {
            pq.pop();
        }
    }

    long long res = 0;
    while (!pq.empty()) {
        res += pq.top();
        pq.pop();
    }

    cout << res << '\n';

    return 0;
}