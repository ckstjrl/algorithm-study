#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	int N, k;
	cin >> N >> k;

	int score[1000]; // 점수를 저장할 배열(최대 1000명)

	for (int i = 0; i < N; i++) {
		cin >> score[i];
	}

	sort(score, score + N, greater<int>());

	cout << score[k - 1] << endl;

	return 0;
}