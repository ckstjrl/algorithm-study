/*** 20055. 컨베이어 벨트 위의 로봇 ***/

#include<iostream>
#include<vector>
using namespace std;

int main() {
	int N, K, stage = 0, dur = 0;
	cin >> N >> K;

	vector<int> belt(2 * N + 1, 0);
	vector<bool> robot(N + 1, false);

	for (int i = 1; i < 2 * N + 1; i++) {
		cin >> belt[i];
	}

	while (1) {
		stage++;
		dur = 0;
		// 1. 컨베이어 벨트 이동

		// 벨트 이동
		int temp = belt[2 * N];
		for (int i = 2 * N - 1; i > 0; i--) {
			belt[i + 1] = belt[i];
		}
		belt[1] = temp;

		// 로봇 이동
		for (int i = N - 1; i > 0; i--) {
			robot[i + 1] = robot[i];
		}
		robot[N] = false;
		robot[1] = false;

		// 2. 로봇 이동
		for (int i = N - 1; i > 0; i--) {
			if (robot[i] == true && belt[i + 1] > 0 && robot[i + 1] == false) {
				robot[i + 1] = robot[i];
				robot[i] = false;
				belt[i + 1]--;
			}
		}
		robot[N] = false;

		// 3. 로봇 올리기
		if (belt[1] > 0 && robot[1] == false) {
			robot[1] = true;
			belt[1]--;
		}

		// 4. 내구도 0 개수가 K개 이상이면 종료
		for (int i = 1; i < 2 * N + 1; i++) {
			if (!belt[i]) dur++;
		}
		if (dur >= K) break;
	}

	cout << stage;

	return 0;
}