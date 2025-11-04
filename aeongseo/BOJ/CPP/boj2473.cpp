/*** 2473. 세 용액 ***/

#include<iostream>
#include<vector>
#include<algorithm>
#include<climits>
using namespace std;

// 용액 오름차순 정렬
// 세 포인터 i, j, k 설정
// i는 고정, j는 i+1, k는 마지막에서 출발
// i는 for문, j k는 while문
// 합이 0이면 종료
// 0이 아니면 합의 절대값과 최소값 비교 갱신 후 j 또는 k 이동
// 0보다 크면 k 이동, 0보다 작으면 j 이동
// j==k 일 때까지 반복

vector<int> solutions;
int ans[3];

int main() {
	int N;
	cin >> N;
	solutions.assign(N, 0);
	for (int i = 0; i < N; i++) cin >> solutions[i];

	sort(solutions.begin(), solutions.end()); // 오름차순 정렬

	long long min_s = LLONG_MAX;	// 합이 int 범위 넘어갈 수 있으므로 long long으로 타입 설정
	for (int i = 0; i < N - 2; i++) {
		if (min_s == 0) break;	// 최소값이 0이면 바로 종료
		int j = i + 1;	// i 다음 인덱스에서 출발
		int k = N - 1; // 마지막 인덱스에서 역으로 출발
		while (j < k) {
			long long s = (long long)solutions[i] + solutions[j] + solutions[k];
			if (abs(s) < min_s) {	// s의 절대값이 최소값보다 작으면 갱신 후 특성값 저장
				min_s = abs(s);
				ans[0] = solutions[i];
				ans[1] = solutions[j];
				ans[2] = solutions[k];
			}
			if (s == 0) break;	// 합이 0이면 탐색 종료

			if (s > 0) k--;	// 합이 0보다 크면 k 1 감소
			else j++;	// 합이 0보다 작으면 j 1 증가
		}
	}

	cout << ans[0] << ' ' << ans[1] << ' ' << ans[2];

	return 0;
}