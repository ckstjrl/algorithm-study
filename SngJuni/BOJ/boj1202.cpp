#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int N, K;
    cin >> N >> K;

    vector<pair<long long, long long>> arr(N);  // (무게, 가격) 쌍으로 보석 정보
    vector<long long> bag(K);  // 가방에 담을 수 있는 무게 정보
    for (int i = 0; i < N; i++) {
        cin >> arr[i].first >> arr[i].second;
    }
    for (int i = 0; i < K; i++) {
        cin >> bag[i];
    }
    
    sort(arr.begin(), arr.end());  // 오름차순 정렬(pair의 특성에 의해 무게, 가격 순으로 정렬)
    sort(bag.begin(), bag.end());  // 오름차순 정렬

    priority_queue<long long> pq;
    long long res = 0;

    int j = 0;
    for (int i = 0; i < K; i++) {     // 가방 무게 정보 순회하면서
        long long capacity = bag[i];  // 현재 가방에 담을 수 있는 무게

        while (j < N && arr[j].first <= capacity) {  // 현재 가방에 보석이 담길 수 있으면
            pq.push(arr[j].second);
            j++;
        }
        if (!pq.empty()) {    // pq에 가방에 담길 수 있는 후보 보석이 있으면
            res += pq.top();  // 제일 큰 보석을 가방에 넣음
            pq.pop();
        }
    }

    cout << res << '\n';

    return 0;
}