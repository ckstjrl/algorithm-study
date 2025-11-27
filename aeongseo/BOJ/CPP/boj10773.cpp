/*** 10773. 제로 (D3) ***/

#include<iostream>
using namespace std;

int main() {
	int K;
	cin >> K;
	int arr[100000] = { 0, };	// K의 최대값만큼 배열 인덱스로 설정, 0으로 초기화
	int top = -1;	// 스택의 맨위 값 위치
	int sum = 0;

	for (int i = 0; i < K; i++) {
		int num;
		cin >> num;
		if (num == 0) {	// 0 이면 맨위 값을 0으로 만들고 위치 -1 감소
			top--;
			arr[top + 1] = 0;
		}
		else {	// 0이 아니면 위치를 1 증가하고 스택에 값 추가
			top++;
			arr[top] = num;
		}
	}

	for (int j = 0; j < K; j++) {	// 스택에 있는 값 모두 합산
		sum += arr[j];
	}

	cout << sum << '\n';

	return 0;
}