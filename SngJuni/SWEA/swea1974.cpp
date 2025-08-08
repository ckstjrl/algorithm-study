#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int check_box(int x, int y, int arr[9][9]) {   // 3 x 3 크기의 격자 안에서 1 ~ 9 까지의 모든 숫자가 있는지 검사
    unordered_set<int> us;
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            us.insert(arr[x + i][y + j]);
        }
    }
    if (us.size() != 9) return 0;
    return 1;
}
int check_row(int s, int arr[9][9]) {          // 같은 행에 1 ~ 9 까지의 모든 숫자가 있는지 검사
    unordered_set<int> us;
    for (int i = 0; i < 9; i++) {
        us.insert(arr[i][s]);
    }
    if (us.size() != 9) return 0;
    return 1;
}
int check_col(int s, int arr[9][9]) {          // 같은 열에 1 ~ 9 까지의 모든 숫자가 있는지 검사
    unordered_set<int> us;
    for (int i = 0; i < 9; i++) {
        us.insert(arr[s][i]);
    }
    if (us.size() != 9) return 0;
    return 1;
}

int main(int argc, char** argv) {
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
        int arr[9][9] = {0,};
        int res = 1; // 최초에는 스도쿠가 정답인 것으로 초기화
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                cin >> arr[i][j];
            }
        }
        for (int i = 0; i < 7; i += 3) {
            for (int j = 0; j < 7; j += 3) {    // 0부터 6까지 3씩 증가하면서 3 X 3 크기의 격자 시작 좌표 설정
                int flag = check_box(i, j, arr);
                if (flag == 0) res = 0;         // 검사 함수의 반환값이 0이면 즉, 정답이 아니면 res를 1로 변경
            }
        }
        for (int i = 0; i < 9; i++) {
            int flag_r = check_row(i, arr);
            int flag_c = check_col(i, arr);
            if (!flag_r || !flag_c) res = 0;    // 검사 함수의 반환값이 0이면 즉, 정답이 아니면 res를 1로 변경
        }

        cout << "#" << test_case << " " << res << "\n";
	}
	return 0;
}