#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
        string s;
        cin >> s;

        vector<int> arr(s.size(), 0);                    // 원래 상태를 위한 배열
        vector<int> mem(s.size(), 0);                    // 초기화 상태를 위한 배열

        for (int i = 0; i < s.size(); i++) {             // 한 줄씩 문자열로 읽어와서 int형으로 변환해서 저장
            arr[i] = s[i] - '0';
        }

        int cnt = 0;
        for (int i = 0; i < s.size(); i++) {
            if (mem[i] != arr[i]) {                      // 0번째 인덱스부터 초기화 상태의 값과 원래 상태의 값이 다를 때,
                for (int j = 0; j < s.size(); j++) {     // 해당 인덱스 이후의 모든 배열을 원래 상태의 값으로 덮어쓰기 -> 최소값 보장
                    mem[j] = arr[i];
                }
                cnt++;
            }
        }
        cout << "#" << test_case << " " << cnt << "\n";
	}
	return 0;
}