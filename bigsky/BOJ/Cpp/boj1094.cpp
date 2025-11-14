#include <iostream>
using namespace std;

int main() {
	int X;
	cin >> X;

	// X를 2진수로 표현했을 때 1의 개수가 필요한 막대 개수
	int count = 0;
	while (X > 0) {
		if (X % 2 == 1) {
			count++;
		}
		X /= 2;
	}

	cout << count << endl;

	return 0;
}