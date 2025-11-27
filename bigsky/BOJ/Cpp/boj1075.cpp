#include <iostream>

using namespace std;

int main() {
	int n, f;
	cin >> n >> f;
	n = n - n % 100; // n의 가장 뒤 두 자리 00만들기
	for (int i = n; ; i++) {
		if (i % f == 0)	{ // 나눠 떨어지는데,
			if (i % 100 < 10) // 한자리면
				cout << "0"; // 앞에 0 추가
			cout << i % 100 << '\n'; // 뒷 2자리 출력
			break;
		}
	}
}