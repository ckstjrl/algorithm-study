/*** 2573. 빙산 ***/

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

// bfs 실행
// cnt 이용해서 덩어리 2개 이상이면 stop
// 2개 미만이면 빙하 삭제
// 상하좌우로 0의 개수 카운트 후 값 변화 
// -> for문 돌면서 원본을 바꾸면 값 이상해짐. 복사본 만들고 나중에 원본에 붙이기
// 연수 카운트 1 증가

void bfs(int si, int sj);
void delete_ice();

int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };

vector<vector<int>> ice;
vector<vector<int>> ice_copy;
vector<vector<int>> visited;
int N, M;

int main() {
	cin >> N >> M;

	ice.assign(N, vector<int>(M, 0));
	ice_copy.assign(N, vector<int>(M, 0));
	visited.assign(N, vector<int>(M, 0));

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			cin >> ice[i][j];
		}
	}

	int year = 0;
	while (1) {
		int ice_cnt = 0;
		visited.assign(N, vector<int>(M, 0));

		// 모든 빙하가 녹았는데 2개로 쪼개진 적이 없으면 year 0으로 초기화
		int cnt = 0;
		for (auto& row : ice) {
			cnt += count(row.begin(), row.end(), 0);
		}
		if (cnt == N * M) {
			year = 0;
			break;
		}

		// BFS 실행
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				if (ice[i][j] != 0 && visited[i][j] == 0) {
					bfs(i, j);
					ice_cnt++;
				}
			}
		}
		if (ice_cnt >= 2) break; // 빙산 덩어리가 2개 이상이면 종료

		// 빙하 삭제 후 원본에 덮어쓰기
		delete_ice();
		copy(ice_copy.begin(), ice_copy.end(), ice.begin());

		//연수 증가
		year++;
	}

	cout << year;
	
	return 0;
}

void bfs(int si, int sj) {
	queue<pair<int, int>> q;

	visited[si][sj] = 1;
	q.push({ si, sj });

	while (!q.empty()) {
		int ti = q.front().first;
		int tj = q.front().second;
		q.pop();

		for (int i = 0; i < 4; i++) {
			int ni = ti + di[i];
			int nj = tj + dj[i];
			if (ni < 0 || ni >= N || nj < 0 || nj >= M || visited[ni][nj] || ice[ni][nj] == 0) continue;
			visited[ni][nj] = 1;
			q.push({ ni, nj });
		}
	}
}

void delete_ice() {
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < M; j++) {
			if (ice[i][j] == 0) continue;
			
			int cnt = 0;
			for (int k = 0; k < 4; k++) {
				int ni = i + di[k];
				int nj = j + dj[k];
				if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;
				if (ice[ni][nj] == 0) cnt++;
			}
			ice_copy[i][j] = ice[i][j] - cnt;
			if (ice_copy[i][j] <= 0) ice_copy[i][j] = 0; // 빙산의 높이가 0 이하면 0으로 저장
		}
	}
}