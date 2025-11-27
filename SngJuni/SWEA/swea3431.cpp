#include <iostream>

using namespace std;

int main(int argc, char** argv) {
	int test_case;
	int T;
	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
        int l, u, x;
        cin >> l >> u >> x;

        int res = 0;
        if (x >= u) {        // 필요한 양보다 더 많은 운동을 하고 있는 경우
            res = -1;
        } else if (x < l) {  // 추가로 운동을 해야하는 경우
            res = l - x;
        }
        cout << "#" << test_case << " " << res << "\n";
	}

	return 0;
}