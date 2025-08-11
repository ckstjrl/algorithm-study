/*** 파스칼의 삼각형 ***/

#include<iostream>
#include<vector>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int tc = 1; tc < T + 1; ++tc) {
		int N;
		cin >> N;
		
		vector<vector<int>> arr(N, vector<int>(N, 0));	// 값이 0인 N*N 가변 배열 생성

		cout << '#' << tc << '\n';
		for (int i = 0; i < N; i++) {	// N줄 생성
			for (int j = 0; j <= i; j++) {	// i열 생성
				if (j == 0 || j == i) {	// j가 첫번째거나 마지막이면 1 출력
					arr[i][j] = 1;
				}
				else {					// j가 중간이면 윗줄 왼쪽 값과 윗줄 오른쪽 값을 더한 값 출력
					arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j];
				}
				cout << arr[i][j] << ' ';
			}
			cout << '\n';
		}
	}
	return 0;
}