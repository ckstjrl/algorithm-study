/*** 4963. 섬의 개수 ***/


#include<iostream>
#include<vector>
#include<queue>

using namespace std;

vector<vector<int>> map; // 지도 배열
vector<vector<bool>> visited; // 방문 배열
int island = 0; // 섬의 개수
int di[8] = { 0, 0, 1, 1, 1, -1, -1, -1 }; // 8방 델타
int dj[8] = { 1, -1, 0, 1, -1, 0, 1, -1 };
int h, w;

void find_island(int si, int sj);

int main() {

	while (1) {
		cin >> w>> h; // h, w 입력
		if (h == 0 && w == 0) break; // h, w이 0, 0 이면 break (입력종료)

		map.assign(h, vector<int>(w, 0)); // 지도 재선언
		visited.assign(h, vector<bool>(w, false)); // 방문 재선언
		
		for (int i = 0; i < h; i++) {// 지도 입력
			for (int j = 0; j < w; j++) {
				cin >> map[i][j];
			}
		}

		for (int i = 0; i < h; i++) {// 지도 순회
			for (int j = 0; j < w; j++) {
				if (map[i][j] && !visited[i][j]) {// 땅이고, 방문한 적 없으면
					island++; // 섬의 개수 증가
					find_island(i, j); // bfs 실행
				}
			}
		}

		cout << island << '\n'; //섬의 개수 출력
		island = 0; // 섬의 개수 초기화

	}

	return 0;
}

void find_island(int si, int sj) {
	queue<pair<int, int>> q; // 큐 선언
	visited[si][sj] = true; // 현재 위치의 방문 표시
	q.push({ si, sj }); // 큐에 삽입

	while (!q.empty()) {// 큐가 빌 때까지
		auto [ti, tj] = q.front();
		q.pop();

		for (int d = 0; d < 8; d++) {// 델타 순회
			int ni = ti + di[d];
			int nj = tj + dj[d];
			
			if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue; // 지도를 벗어나면 continue
			if (visited[ni][nj]) continue; // 방문한 적 있으면 continue
			if (!map[ni][nj]) continue; // 바다면 continue
			q.push({ ni, nj }); // 큐에 삽입
			visited[ni][nj] = true; // 방문 표시
		}
	}
}