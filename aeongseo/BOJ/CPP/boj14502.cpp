/*** 14502.연구소 ***/

/*
	1. 벽을 세운다 -> 브루트포스
	2. 바이러스가 퍼진다 -> bfs
	3. 안전영역의 크기를 센다 -> for문

	바이러스 퍼뜨린 후 이 방법 아니면 원상복구 해야 함
	초기 바이러스 위치는 계속 저장되어 있어야 함
*/

#include<iostream>
#include<vector>
#include<queue>

using namespace std;

vector<vector<int>> lab; // 연구소 지도
vector<vector<int>> test; // 바이러스 퍼뜨린 후 원복을 위해 복사해서 사용
queue<pair<int, int>> virus; // 바이러스 큐
int N, M, ans = 0;

void makeWall(int cnt); // 벽세우기
void spreadVirus(); // 바이러스 퍼뜨리기
int safezone(); // 안전영역 카운트

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M;

	lab.assign(N, vector<int>(M, 0));
	test.assign(N, vector<int>(M, 0));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> lab[i][j];
			if (lab[i][j] == 2) {
				virus.push({ i, j }); // 2이면 바이러스 배열에 추가
			}
		}
	}
		
	makeWall(0); // 벽세우기

	cout << ans;

	return 0;
}

void makeWall(int cnt) {
	if (cnt == 3) {// cnt == 3이면 테스트
		spreadVirus(); // 바이러스 퍼짐
		int safe = safezone(); // 안전영역 세기
		if (safe > ans) ans = safe; // 만약 최대값보다 크면 갱신
		return;
	}
	for (int i = 0; i < N; i++) {// 연구소 순회 이중 for문
		for (int j = 0; j < M; j++) {
			if (lab[i][j]) continue; // 0아니면 continue
			lab[i][j] = 1; // 벽세우기
			makeWall(cnt + 1); // 재귀
			lab[i][j] = 0; // 벽 치우기
		}
	}
}

void spreadVirus() {
	copy(lab.begin(), lab.end(), test.begin()); // 연구소 배열 복사
	queue<pair<int, int>> testVirus = virus; // 바이러스 큐 복사

	int di[4] = { 0, 1, 0, -1 };
	int dj[4] = { 1, 0, -1, 0 };

	while (!testVirus.empty()) {// 바이러스 큐 순회
		auto [ti, tj] = testVirus.front();
		testVirus.pop();

		for (int d = 0; d < 4; d++) {// 상하좌우 델타 순회
			int ni = ti + di[d];
			int nj = tj + dj[d];
			if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue; // 범위 벗어나면 continue
			if (test[ni][nj]) continue; // 0이 아니면 continue
			test[ni][nj] = 2; // 2로 바꿈
			testVirus.push({ ni, nj }); // 큐에 넣기
		}
	}
}

int safezone() {
	int cnt = 0; // cnt = 0 선언
	for (int i = 0; i < N; i++) {// 이중 for문
		for(int j=0;j<M;j++){
			if (!test[i][j]) cnt++;// 0이면 개수 증가
		}
	}
	return cnt; // cnt 반환
}