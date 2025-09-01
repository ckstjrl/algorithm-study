#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
        int n, m, k;                             // n 명, m 초, k 개
        cin >> n >> m >> k;

        vector<int> arr(n, 0);                   // 손님의 도착 시간을 위한 동적 배열
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }

        sort(arr.begin(), arr.end());            // 손님의 도착 시간 오름차순으로 정렬

        string res = "Possible";
        for (int i = 0; i < n; i++) {
            int total_bread = (arr[i] / m) * k;  // 해당 도착 시간 기준, 생산된 붕어빵 갯수 -> 누적 붕어빵 생산량
            int customer = i + 1;                // 해당 도착 시간 기준, 손님의 수        -> 누적 손님 수
            
            if (total_bread < customer) {        // 손님 수가 붕어빵 생산량보다 많으면 Impossible!
                res = "Impossible";
                break;
            }
        }

        cout << "#" << test_case << " " << res << "\n";
	}

	return 0;
}