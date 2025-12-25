#include <iostream>

using namespace std;

int N, K;

int main() {
	cin >> N >> K;
	int temp = N + K;
	for (int i = 1; i < temp / 2 + 1; i++) {
		// 나누어떨어지면 고려
		if (temp % i == 0) {
			int j = temp / i;
			if (i * 2 + (j - 2) * 2 == N) {
				cout << j << ' ' <<i << '\n';
				break;
			}

		}
	}
	return 0;
}