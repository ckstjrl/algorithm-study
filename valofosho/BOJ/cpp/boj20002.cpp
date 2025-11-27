/*
BOJ20002 - 사과나무

문제 정의
N*N 정사각형 과수원에 K*K 크기의 정사각형만 수확 가능
K의 범위가 1<=K<=N일 때 최대 값을 구하라

로직 정의
1. 누적합 문제로 생각하고 풀이
2. K를 1일 때를 미리 복사해놓기
3. K가 커지면서 더해야하는 행과 열 리버스(ㄴ) 모양을 더해준다.
4. 각각의 지점에서 진행하고 최대값을 계속 갱신
*/

#include <iostream>
#include <vector>

using namespace std;

int main() {
	// N 입력
	int N;
	cin >> N;
	// vector 선언
	vector<vector<int>> maps (N, vector<int>(N));
	vector<vector<int>> apples (N, vector<int>(N));

	// max_val 초기화
	int max_val = -10000;

	// maps vector 채우기
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> maps[i][j];
			apples[i][j] = maps[i][j];
				if (max_val < apples[i][j]) {
					max_val = apples[i][j];
			}

		}
	}


	// K를 높여가며 순회 (1<=K<=N)
	for (int K = 2; K <= N; K++) {
		// 누적합 범위는 0~ N-K까지!
		for (int i = 0; i <= N - K; i++) {
			for (int j = 0; j <= N - K; j++) {
				// 구해서 더할 값들 범위
				int temp = apples[i][j];
				// 세로 축
				for (int r = 0; r <= K - 1; r++) {
					temp += maps[i + r][j + K - 1];
				}
				for (int c = 0; c <= K - 1; c++) {
					temp += maps[i + K - 1][j + c];
				}
				// 중복 대각선 빼주기
				temp -= maps[i + K -  1][j + K - 1];
				
				apples[i][j] = temp;
				if (max_val < temp) {
					max_val = temp;
				}
			}
		}
	}
	
	cout << max_val;

	return 0;
}
