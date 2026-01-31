// BOJ 7490. 0 만들기 / G3
#include <iostream>
#include <vector>
#include <queue>

using namespace std;
int N;
char ops[10];

int cal() {
	int result = 0;
	int cur = 1;
	int sign = 1;

	for (int i = 2; i <= N; i++) {
		char op = ops[i - 1];

		if (op == ' ') {
			cur = cur * 10 + i;
		}
		else {
			result += sign * cur;
			cur = i;
			if (op == '+') sign = 1;
			else sign = -1;
		}
	}
	result += sign * cur;
	return result;
}

void allcase(int i) {
	if (i > N - 1) {
		if (cal() == 0) {
			cout << 1;
			for (int j = 2; j <= N; j++) {
				cout << ops[j - 1] << j;
			}
			cout << "\n";
		}
		return;
	}

	ops[i] = ' ';
	allcase(i + 1);
	ops[i] = '+';
	allcase(i + 1);
	ops[i] = '-';
	allcase(i + 1);
}

int main() {
	int T;
	cin >> T;

	while (T--) {
		cin >> N;
		allcase(1);
		cout << "\n";
	}
}

/*
cal -> allcase에서 정해준 부호에 맞춰서 계산하는 함수
allcase -> 모든 ' ', '+', '-' 세 가지 부호를 조합하여 식을 만들고 그 식의 결과가 0이라면 출력하는 재귀함수
*/