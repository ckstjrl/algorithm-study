/*** 1463. 1로 만들기 ***/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int N;
	cin >> N;
	
	vector<int> f(N + 1, 0); // f(i) : N에서 i가 되기 위해 사용하는 연산 횟수의 최소값
	
	for (int i = N-1; i > 0; i--) {	// 거꾸로 반복
		if (i * 3 <= N) {	// 3을 곱한 값이 N보다 작으면 
			int temp = min(f[i + 1], f[i * 2]);	// f(i) = min(f(i+1), f(i*2), f(i*3)) + 1
			f[i] = min(temp, f[i * 3]) + 1;
		}
		else if (i * 2 <= N && i * 3 > N) {	// 3을 곱한 값이 N보다 크고, 2를 곱한 값이 N보다 작으면
			f[i] = min(f[i + 1], f[i * 2]) + 1;	// f(i) = min(f(i+1), f(i*2)) + 1
		}
		else {	// 2를 곱한 값이 N보다 작으면
			f[i] = f[i + 1] + 1;	// f(i) = f(i+1)
		}
	}

	cout << f[1];	// 1이 되었을 떄의 연산 횟수 최소값

	return 0;
}