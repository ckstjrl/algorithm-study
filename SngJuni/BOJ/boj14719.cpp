#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int H, W;
    cin >> H >> W;
    
    vector<int> arr(W);  // 각 열의 블록 높이 저장
    for (int i = 0; i < W; i++) {
        cin >> arr[i];
    }
    
    int res = 0;  // 총 빗물의 양

    // 첫번째 칸과 마지막 칸은 물이 고일 수 없음 -> 1 ~ W - 2 까지만 검사
    for (int i = 1; i < W - 1; i++) {
        int l = 0, r = 0;  // 현재 칸 기준 왼쪽, 오른쪽에서 가장 높은 블록의 높이

        // 왼쪽에서 가장 높은 블록
        for (int j = 0; j < i; j++) {
            if (arr[i] < arr[j]) l = max(l, arr[j]);
        }
        // 오른쪽에서 가장 높은 블록
        for (int j = i; j < W; j++) {
            if (arr[i] < arr[j]) r = max(r, arr[j]);
        }
        // 양쪽에 벽이 모두 있을 경우 -> 물이 고임
        if (l && r) res += min(l, r) - arr[i];  // 낮은 벽 기준으로 고이는 빗물의 양 계산
    }

    cout << res;  // 결과 출력
    
    return 0;
}