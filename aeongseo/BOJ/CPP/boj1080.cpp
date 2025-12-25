/*** 1080. 행렬 ***/

// 행렬을 순회하며 A와 B의 값이 다르면 뒤집는다.

#include<iostream>
#include<vector>
#include<string>
using namespace std;

vector<vector<int>> A, B;

int main() {
	int N, M, ans = 0; // ans : 뒤집은 횟수 저장
	cin >> N >> M;

	A.assign(N, vector<int>(M, 0));
	B.assign(N, vector<int>(M, 0));

	for (int k = 0; k < 2; k++) {
		for (int i = 0; i < N; i++) {
			string s;
			cin >> s;
			for (int j = 0; j < M; j++) {
				if (k == 0) A[i][j] = s[j];
				else B[i][j] = s[j];
			}
		}
	}

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (A[i][j] != B[i][j] && i < N - 2 && j < M - 2) { // A와 B의 값이 다르고 배열을 벗어나지 않으면
				for (int x = i; x < i + 3; x++) { // 뒤집기
					for (int y = j; y < j + 3; y++) {
						A[x][y] ^= 1;
					}
				}
				ans++;
			}
		}
	}

  // 일치하는지 확인
	bool flag = true;
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (A[i][j] != B[i][j]) flag = false; // 값이 다르면 false
		}
	}

	if (flag) cout << ans; // 일치하면 ans 출력
	else cout << -1; // 일치하지 않으면 -1 출력

	return 0;
}