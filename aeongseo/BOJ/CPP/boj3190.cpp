/*** 3190. 뱀 ***/

#include<iostream>
#include<deque>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int cnt = 0; // 현재 초
	int N, K, L;
	cin >> N >> K;
	deque<vector<int>> dq;	// 이렇게 하면 큐에 배열 삽입 가능
	vector<vector<int>> apple(N+1, vector<int>(N+1, 0));
	for (int k = 0; k < K; k++) {	// 사과의 위치 저장
		int a, b;
		cin >> a >> b;
		apple[a][b] = 1;
	}

	cin >> L;
	vector<vector<int>> dir(L, vector<int>(2));
	// 방향 전환을 위한 델타
	int di[4] = { 0, 1, 0, -1 };
	int dj[4] = { 1, 0, -1, 0 };
	int dr = 0;
 	for (int k = 0; k < L; k++) {	// 방향 전환 정보 저장
		char x;
		cin >> dir[k][0] >> x;
		if (x == 'L') {	// 왼쪽이면 2
			dir[k][1] = 2;
		}
		else {	// 오른쪽이면 3
			dir[k][1] = 3;
		}
	}

	// 뱀의 초기 위치
	dq.push_back({1, 1});	// (1, 1)
	int i = 1;
	int j = 1;
	int x = 0;	// 방향 정보 인덱스
	while (1) {
		cnt++;	// 초 증가
		// 이동할 위치
		i += di[dr];
		j += dj[dr];

		// 종료조건
		vector<int> target = { i, j };
		if (i < 1 || i > N || j < 1 || j > N || find(dq.begin(), dq.end(), target) != dq.end()) {
			break;
		}

		dq.push_back({ i, j });	// 한칸 이동
		if (apple[i][j] != 1) {	// 사과 없으면
			dq.pop_front();	// 뱀 길이 줄어듦
		}
		else {	// 사과 있으면 사과 먹음
			apple[i][j] = 0;
		}
		if (x < dir.size() && cnt == dir[x][0]) {	// 
			if (dir[x][1] == 2) {	// 방향이 왼쪽이면
				dr = (dr + 3) % 4;
			}
			else {	// 방향이 오른쪽이면
				dr = (dr + 1) % 4;
			}
			x++;	//  다음 방향 정보로 이동
		}
	}
	
	cout << cnt;

	return 0;
}