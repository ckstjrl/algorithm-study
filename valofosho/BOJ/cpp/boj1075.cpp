#include <iostream>

using namespace std;
using ll = long long int;

int main() {
	ll N, F;
	cin >> N >> F;
	N = (N / 100) * 100;
	for (int i = 0; i < 100; i++) {
		ll t = N + i;
		if (t % F == 0) {
			if (i < 10) {				
				cout << '0' << i << '\n';
				break;
			}
			else {
				cout << i << '\n';
				break;
			}
		}
	}
	return 0;
}