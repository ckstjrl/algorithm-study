#include<iostream>
#include<string>
using namespace std;

int main() {
	string txt[3];
	int num = 0;
	cin >> txt[0] >> txt[1] >> txt[2];
	for (int i = 0; i < 3; i++) {
		if (txt[i] != "Fizz" && txt[i] != "Buzz" && txt[i] != "FizzBuzz") { // 입력받은 값이 숫자면
			num = stoi(txt[i]) + (3 - i);	// 출력해야 할 숫자로 저장
		}
	}

	if (num == 0) {	// 연속의 세 문자열이 모두 숫자가 아니었을 경우 아무거나 출력
		cout << "Fizz";
	}
	else {
		if (num % 3 == 0) {
			if (num % 5 == 0) {	// 3의 배수이고 5의 배수이면 FizzBuzz 출력
				cout << "FizzBuzz";
			}
			else {	// 3의 배수이지만 5의 배수가 아니면 Fizz 출력
				cout << "Fizz";
			}
		}
		else {
			if (num % 5 == 0) {	// 3의 배수가 아니지만 5의 배수이면 Buzz 출력
				cout << "Buzz";
			}
			else {	// 3의 배수도, 5의 배수도 아니면 숫자 출력
				cout << num;
			}
		}
	}

	return 0;
}