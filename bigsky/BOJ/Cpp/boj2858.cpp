#include <iostream>

using namespace std;

int main() {
	int r, b;
	cin >> r >> b;
	int x, y;
	
	int extent = r + b; // 총넓이 = 빨강 + 갈색

	for (int i = 1; ; i++) {
		if (extent % i == 0) { // 총넓이의 약수일때만
			x = i;
			y = extent / i;
			if (((2 * x + 2 * y - 4) == r) && ((x - 2) * (y - 2) == b))
				break;
		}
	}
	if (x > y) cout << x << ' ' << y << '\n';
	else cout << x << ' ' << y << '\n';
	return 0;
}