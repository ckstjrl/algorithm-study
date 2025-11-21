#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M;
    cin >> N >> M;

    vector<int> arr(N + 1, 0);  // 수열
    for (int i = 1; i <= N; i++) {
        cin >> arr[i];
    }

    for (int i = 2; i <= N; i++) {  // 누적합 구하기
        arr[i] += arr[i - 1];
    }

    int s, e;
    for (int i = 0; i < M; i++) {
        cin >> s >> e;
        cout << arr[e] - arr[s - 1] << '\n'; // i부터 j까지의 구간합 == 누적합 arr[j] - arr[i - 1] 
    }

    return 0;
}