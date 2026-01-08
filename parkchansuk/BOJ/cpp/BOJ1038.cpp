// BOJ 1038. 감소하는 수 / G5
/*
문제
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.

입력
첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

출력
첫째 줄에 N번째 감소하는 수를 출력한다.
*/
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<long long> num;
vector<int> arr;
void combination(int deep, int nxt, int r) {
	if (deep == r) {
		long long x = 0;
		for (int i = r - 1; i >= 0; i--) {
			x = x * 10 + arr[i];
		}
		num.push_back(x);
		return;
	}

	for (int i = nxt; i <= 9; i++) {
		arr.push_back(i);
		combination(deep + 1, i + 1, r);
		arr.pop_back();
	}
}
int main() {
	for (int i = 1; i <= 10; i++) {
		combination(0, 0, i);
	}
	

	int N;
	cin >> N;

	sort(num.begin(), num.end());

	if (N >= num.size()) cout << -1 << "\n";

	else {
			cout << num[N] << "\n";
	}
}

/*
조합 함수 작성하여 감소하는 수 x를 제작
이후 10 C 1 ~ 10 C 10까지 연산하여 벡터 num에 집어 넣고
sort 진행
이후 input으로 받은 N이 num의 size보다 크면 -1 출력
아니면 num의 N번째 인덱스 출력
*/