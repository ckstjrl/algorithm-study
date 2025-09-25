#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int N, C;
    cin >> N >> C;
    
    vector<int> arr(N);  // 집의 좌표를 위한 가변배열
    for (int i = 0; i < N; i++) cin >> arr[i];

    sort(arr.begin(), arr.end());  // 집들의 좌표를 오름차순으로 정렬
    
    // 이분탐색을 위한 초기화
    int low = 1;                     // 두 공유기 사이의 최소 거리
    int high = arr[N - 1] - arr[0];  // 두 공유기 사이의 최대 거리
    int res = 0;

    while (low <= high) {
        int mid = (low + high) / 2;  // 최소 거리 후보

        int cnt = 1;  // 첫번째 집에 공유기 설치
        int prev = arr[0];  // 마지막으로 공유기를 설치한 집의 좌표
        for (int i = 1; i < N; i++) {    // 집의 좌표를 순회하며
            if (arr[i] - prev >= mid) {  // 최소 거리 후보보다 크면 
                cnt++;                   // 공유기 설치
                prev = arr[i];           // 마지막 집 좌표 갱신

                if (cnt == C) break;     // 만약 공유기 대수만큼 설치됐으면 순회 종료 (가지치기)
            }
        }

        if (cnt >= C) {     // 현재 후보(mid) 간격으로 C개 이상 설치 가능
            low = mid + 1;  // 간격 넓힘
            res = mid;
        } else {             // 공유기 C개 설치 불가
            high = mid - 1;  // 간격 줄임
        }
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}