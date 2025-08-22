/*** 1970. 쉬운 거스름돈 (D2) ***/

#include<iostream>
using namespace std;

int main() {
	int T;
	cin >> T;
	
	for (int tc = 1; tc < T + 1; ++tc) {
		int N, change;
		cin >> N;
		N = (int)(N / 10);	// 십의 자리부터 계산하도록 마지막 0을 날림
		int money[8] = { 0, };	// 각 종류의 돈의 개수

		for (int i = 0; i < 8; i += 2) {
			if (i < 6) {
			change = N % 10;	// 만의 자리 전까지는 자리 수 뽑기
			}
			else {
				change = N; // 만의 자리에서는 값 그대로 저장. (5만원권까지만 있으므로)
			}
			if (change >= 5) {	// 자리수가 5 이상이면 
				money[i + 1] = change / 5;	// 5로 나눈 몫을 오십, 오백, 오천, 오만원권으로 저장
				money[i] = change % 5;	// 나머지를 십, 백, 천, 만원권으로 저장
			}
			else {	// 자리수가 5 미만이면 자리수 그대로 십, 백, 천, 만원권으로 저장
				money[i] = change;
			}
			N = (int)(N / 10);	// 다음 자리수로 이동
		}

		cout << '#' << tc << '\n';
		for (int j = 7; j >= 0; j--) {
			cout << money[j] << ' ';	// 오만원권부터 거꾸로 출력
		}
		cout << '\n';

	}
	return 0;
}