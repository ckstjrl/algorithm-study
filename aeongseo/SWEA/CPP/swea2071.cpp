/*** 2071. 평균값 구하기 ***/


#include<iostream>
using namespace std;

int main() {
	int test_case;
	int T;

	cin >> T;

	for (test_case = 1; test_case <= T; ++test_case) {
		int arr[10];
		int sum = 0, avg = 0;
		for (int i = 0; i < 10; i++) {
			cin >> arr[i];
		}

		for (int j = 0; j < 10; j++) {
			sum += arr[j];
		}

		if (sum % 10 >= 5) {                            // 평균의 소수점이 0.5 이상일 때 올림
			avg = sum / 10 + 1;
		}
		else {                                          // 0.5 미만이면 버림
			avg = sum / 10;
		}

		cout << '#' << test_case << ' ' << avg << '\n';
	}

	return 0;
}