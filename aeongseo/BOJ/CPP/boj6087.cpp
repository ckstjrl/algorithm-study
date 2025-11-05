/*** 6087. 레이저 통신 ***/

// c의 위치 저장
// c 한쪽에서 bfs 시작
// 시작점에서 모든 방향 q에 저장
// q에서 하나씩 꺼내며 이동, 다른 방향으로 가면 거울 1 추가, 같은 방향이면 거울 추가 X
// 다음 위치가 c면 거울 개수 저장 후 bfs 종료

#include<iostream>
#include<vector>
#include<deque>
#include<tuple>
#include<climits>
#include<algorithm>
using namespace std;

void bfs(int si, int sj);

vector<vector<char>> map;
vector<pair<int, int>> c;
vector<vector<vector<int>>> cnt;

int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };
int w, h, td;

int main() {
	cin >> w >> h;

	map.assign(h, vector<char>(w));
	cnt.assign(h, vector<vector<int>>(w, vector<int>(4, INT_MAX)));

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			char a;
			cin >> a;
			map[i][j] = a;
			if (a == 'C') c.push_back({ i, j });    // C의 위치 저장
		}
	}

	auto[si, sj] = c[0];
	//int si = c[0].first; int sj = c[0].second;
	bfs(si, sj);    // 첫번째 C의 위치에서 bfs

	auto[ti, tj] = c[1];
	// int ti = c[1].first; int tj = c[1].second;
	int ans = INT_MAX; 
	for (int d = 0; d < 4; d++) ans = min(ans, cnt[ti][tj][d]); // 네 방향 중 가장 작은 값 출력
	cout << ans;

	return 0;
}

void bfs(int si, int sj) {
	deque<tuple<int, int, int>> q;
	for (int d = 0; d < 4; d++) {
		cnt[si][sj][d] = 0;
		q.push_back({ si, sj, d }); // x좌표, y좌표, 방향
	}

	while (!q.empty()) {
		auto[i, j, dir] = q.front();
		// int i = get<0>(q.front());
		// int j = get<1>(q.front());
		// int dir = get<2>(q.front());
		q.pop_front();

		for (int nd = 0; nd < 4; nd++) { // 상하좌우 이동
			int ni = i + di[nd];
			int nj = j + dj[nd];

			if (ni < 0 || ni >= h || nj < 0 || nj >= w) continue; // 배열 벗어나면 continue
			if (map[ni][nj] == '*') continue; // 이동한 곳이 벽이면 continue

			int mirror = (dir != nd); // 방향이 같으면 0, 다르면 1

			if (cnt[ni][nj][nd] > cnt[i][j][dir] + mirror) { // 거울의 개수가 저장된 값보다 더 적으면 갱신
				cnt[ni][nj][nd] = cnt[i][j][dir] + mirror;
				if (mirror == 0) q.push_front({ ni, nj, nd }); // 방향이 같으면 큐 앞에 넣어서 계속 진행
				else q.push_back({ ni, nj, nd });   // 방향이 다르면 뒤에 넣어서 다른 방향 진행
			}

		}
	}
}