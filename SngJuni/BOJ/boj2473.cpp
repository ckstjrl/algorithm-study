#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<long long> arr(N);  // 제약사항이 10e9지만 합산 시 오버플로우 방지를 위해 long long 으로 형 변환 해야하기 때문에 long long으로 받음
    for (int i = 0; i < N; i++) cin >> arr[i];
    
    sort(arr.begin(), arr.end());  // 오름차순으로 정렬

    long long best = LLONG_MAX;  // min 값을 구하기 위해 LONG LONG MAX 로 초기화
    long long a = 0, b = 0, c = 0;  // 각 용액의 특성값 초기화

    bool flag = false;  // 0이 된 경우를 판단
    for (int i = 0; i < N - 2; i++) {
        // i번째를 첫번째 용액으로 고정하고
        int l = i + 1;  // i + 1번째와
        int r = N - 1;  // N - 1번째의 용액부터 탐색

        while (l < r) {  // l, r을 통해 이분탐색
            long long temp = arr[i] + arr[l] + arr[r];  // 세 용액의 합산

            if (llabs(temp) < best) {  // 최솟값 갱신
                best = llabs(temp);
                a = arr[i];
                b = arr[l];
                c = arr[r];
            }

            if (temp > 0) r--;  // 0보다 크면 오른쪽 값을 줄여야 함.
            else if (temp < 0) l++;  // 0보다 작으면 왼쪽 값을 늘려야 함.
            else {  // 0이 되면 while문 탈출
                flag = true;
                break;
            }
        }
        if (flag) break;  // 0이 됐을 경우 for문 탈출
    }

    cout << a << ' ' << b << ' ' << c << '\n';  // 결과 출력

    return 0;
}