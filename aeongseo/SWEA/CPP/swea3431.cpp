/*** 3431. 준환이의 운동관리 (D3) ***/

#include<iostream>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int tc = 1; tc < T + 1; ++tc) {
		int L, U, X, t;
		cin >> L >> U >> X;

		if (X < L) {	// 운동시간이 최소시간보다 작다면 부족한 시간 저장
			t = L - X;
		}
		else if (X > U) {	// 운동시간이 최대시간을 초과했다면 -1 저장
			t = -1;
		}
		else {	// 운동시간이 최소와 최대시간 사이에 있다면 0 저장
			t = 0;
		}

		cout << '#' << tc << ' ' << t << '\n';

	}

	return 0;
}