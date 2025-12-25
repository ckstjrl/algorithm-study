#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) cin >> arr[i];  // 센서의 좌표 정보
    sort(arr.begin(), arr.end());  // 오름차순으로 정렬
    
    vector<int> diff(N - 1);
    for (int i = 1; i < N; i++) diff[i - 1] = arr[i] - arr[i - 1];  // 각 센서 사이의 거리 구함.
    sort(diff.begin(), diff.end());  // 오름차순으로 정렬

    // 거리의 합이 최소가 되려면 결국 각 센서의 거리를 오름차순으로 정렬 후, N - K 개의 거리를 더하면 됨.
    int res = 0;
    for (int i = 0; i < N - K; i++) res += diff[i];

    cout << res << '\n';

    return 0;
}