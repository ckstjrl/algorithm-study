// BOJ 1041. 주사위 / G5
#include <iostream>

using namespace std;

int main() {
	long long N;
	cin >> N;

	long long ans = 0;
	
	long long ju[6];
	long long min_one = 1000001;
	long long max_one = 0;
	long long sum = 0;
	for (int i = 0; i < 6; i++) {
		cin >> ju[i];
		sum += ju[i];
		if (ju[i] < min_one) min_one = ju[i];
		if (ju[i] > max_one) max_one = ju[i];
	}

	if (N == 1) {
		ans = sum - max_one;
	}

	else {
		long long two[12] = { ju[0] + ju[1], ju[0] + ju[2], ju[0] + ju[3], ju[0] + ju[4],
								ju[1] + ju[2], ju[1] + ju[3], ju[1] + ju[5],
								ju[2] + ju[4], ju[2] + ju[5],
								ju[3] + ju[4], ju[3] + ju[5],
								ju[4] + ju[5] };

		long long three[8] = { ju[0] + ju[1] + ju[2], ju[0] + ju[1] + ju[3], ju[0] + ju[2] + ju[4], ju[0] + ju[3] + ju[4],
								ju[1] + ju[2] + ju[5], ju[1] + ju[3] + ju[5],
								ju[2] + ju[4] + ju[5],
								ju[3] + ju[4] + ju[5] };

		long long min_two = 2000002;
		long long min_three = 3000003;
		for (int i = 0; i < 12; i++) {
			if (two[i] < min_two) min_two = two[i];
		}

		for (int i = 0; i < 8; i++) {
			if (three[i] < min_three) min_three = three[i];
		}

		ans = min_one * (5 * N * N - 16 * N + 12)
			+ min_two * (8 * N - 12)
			+ min_three * 4;
	}
	cout << ans << "\n";
}

/*
그냥 완전 구현
*/