/*** 1107. 리모컨 ***/

#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int N, minClick, channel;
bool broken[10];

void remote(string cur);

int main() {
	cin >> channel >> N;
	for (int i = 0; i < N; i++) {
		int x;
		cin >> x;
		broken[x] = true;
	}

	minClick = abs(channel - 100); // +, - 버튼만 눌렀을 때 횟수

	for (int i = 0; i < 10; i++) {
		if (!broken[i]) remote(to_string(i)); // 고장나지 않은 버튼으로 시작
	}

	cout << minClick;

	return 0;
}

void remote(string cur) {

	if (!cur.empty()) {
		int intCur = stoi(cur);

		int count = cur.size() + abs(intCur - channel); // 숫자 버튼 누른 횟수 + +,- 버튼 누른 횟수
		
		if (count < minClick) minClick = count;
	}

	if (cur.size() >= 6) return; // 가지치기

	for (int i = 0; i < 10; i++) {
		if (broken[i]) continue;
		remote(cur + to_string(i));
	}
}