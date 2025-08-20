/*** 2869. 달팽이는 올라가고 싶다 ***/

#include<iostream>
#include<cmath>
using namespace std;

int main() {
	int A, B, V, cnt;
	cin >> A >> B >> V;
	if ((V - A) % (A - B) != 0) {	// 높이를 초과해서 도착하는 경우
		cnt = ceil((double)(V - A) / (double)(A - B)) + 1; // 왜 float은 안되고 double은 가능?????
	}
	else {	// 딱맞게 도착하는 경우
		cnt = (V - A) / (A - B) + 1; // (다음날 올라가야할 높이) / (하루에 올라가는 높이) + 하루
	}
	cout << cnt;

	return 0;
}