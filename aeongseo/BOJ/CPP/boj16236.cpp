/*** 16236. 아기 상어 ***/

/*
	NxN 크기 물고기 M마리, 상어 1마리
	한칸에 물고기 최대 1마리
	초기 아기상어 크기 2, 상하좌우 이동
	상어 크기 >= 물고기 크기 : 지나갈 수 있음
	상어 크기 > 물고기 크기 : 먹을 수 있음, 먹으면 빈칸 됨
	거리가 가장 가까운 물고기 먹으러 가기
	크기와 같은 수 먹어야 크기 증가
*/

#include<iostream>
#include<queue>
#include<tuple>

using namespace std;

int cnt = 0, eat = 0, shark = 2, si, sj, N; // cnt, eat, shark, si, sj, N 선언
bool nofeed = false; // 먹을 것 없는지 플래그 false
int sea[21][21] = { 0, };
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };

void find_fish(int si, int sj);

int main() {
	cin >> N;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> sea[i][j];
			if (sea[i][j] == 9) { // 상어 위치 저장
				si = i;
				sj = j;
			}
		}
	}

	sea[si][sj] = 0; // 처음 상어 위치 초기화
	while (!nofeed) {// nofeed가 false일 동안
		find_fish(si, sj); // 먹이 찾기
	}

	cout << cnt;

	return 0;
}

void find_fish(int i, int j) { // 먹을 수 있는 물고기 찾기
	// bfs 실행
	bool ate = false; // 먹었는지 플래그 false
	queue<pair<int, int>> q; // 큐 선언
	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq; // 우선순위 큐 (거리, 좌표) 선언
	int visited[21][21] = { 0, }; // 방문 배열
	q.push({ i, j }); // 큐에 상어 위치 저장
	visited[i][j] = 1; // 방문 표시 = cnt

	while (!q.empty()) {// 큐가 빌때까지
		auto [ti, tj] = q.front(); // 큐 top 꺼내서 저장
		q.pop();
		
		if (sea[ti][tj] && sea[ti][tj] < shark) pq.push({visited[ti][tj], ti, tj}); // shark보다 작으면 우선순위큐에 저장
		
		for (int d = 0; d < 4; d++) {// 델타 위한 for문
			int ni = ti + di[d]; // 이동한 좌표 설정
			int nj = tj + dj[d];
			if (ni < 0 || ni >= N || nj < 0 || nj >= N || visited[ni][nj]) continue; // 좌표가 배열을 벗어나면 continue
			if (sea[ni][nj] > shark) continue; // shark보다 크면 continue
			q.push({ ni, nj }); // 큐에 좌표 저장
			visited[ni][nj] = visited[ti][tj] + 1; // 방문 표시
		}
	}
	if(pq.empty()) nofeed = true; // 우선순위큐가 비었으면 nofeed = true
	else{// 안비었으면
		auto[dist, ti, tj] = pq.top(); // 우선순위큐 top의 좌표에서 물고기 먹음
		eat++; // eat++
		si = ti; // si = ti, sj = tj
		sj = tj;
		sea[ti][tj] = 0; // 좌표 값 0
		cnt += visited[ti][tj] - 1; // cnt = 방문 값
		if (eat == shark) {// eat == shark면 shark++
			shark++;
			eat = 0; // eat  = 0
		}
	}
}