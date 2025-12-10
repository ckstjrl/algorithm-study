/*** 1992. 쿼드트리 ***/

#include<iostream>
#include<string>
using namespace std;

int video[65][65] = { 0, };
string ans;

void zip(int si, int sj, int n);

int main() {
	int N;
	cin >> N;
	for (int i = 0; i < N; i++) {
		string line;
		cin >> line;
		for (int j = 0; j < N; j++) {
			video[i][j] = line[j] - '0';
		}
	}

	zip(0, 0, N);

	cout << ans;

	return 0;
}

void zip(int si, int sj, int n) { // 왼쪽 최상단 좌표, 영상 크기
	int white = 0, black = 0;

	for (int i = si; i < si + n; i++) {
		for (int j = sj; j < sj + n; j++) {
			if (video[i][j]) black++;	// 1 개수 카운트
			else white++;	// 0 개수 카운트
		}
	}

	if (!white) ans.push_back('1');	// 모두 1이면 1 출력
	else if (!black) ans.push_back('0');	// 모두 0이면 0 출력
	else {	// 0과 1이 섞여있으면
		ans.push_back('(');	// ( 출력
		n /= 2;	// 크기 반으로 나누기
		zip(si, sj, n);	// 4등분 나눠 압축 재시도
		zip(si, sj + n, n);
		zip(si + n, sj, n);
		zip(si + n, sj + n, n);
		ans.push_back(')');	// ) 출력
	}
}