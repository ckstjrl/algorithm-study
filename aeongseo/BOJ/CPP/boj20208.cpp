/*** 20208. 진우의 민트초코우유 ***/

#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

int maxcnt = 0, hi, hj, K=0;
int N, M, H;
vector<vector<int>> map;
vector<pair<int, int>> milks;
vector<bool> drink;

void backtrack(int si, int sj, int cnt, int hp);
int dist(int x1, int y1, int x2, int y2);

int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N >> M >> H;
	map.assign(N, vector<int>(N, 0));
	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			cin >> map[i][j];
			// 집 위치 저장
			if (map[i][j] == 1) {
				hi = i; hj = j;
			}

			// 우유 개수 세기
			if (map[i][j] == 2) {
				milks.push_back({ i, j });
				K++;
			}
		}
	}
	drink.assign(K, 0);

	backtrack(hi, hj, 0, M);

	cout << maxcnt;

	return 0;
}

void backtrack(int si, int sj, int cnt, int hp) {
	// 현재 위치에서 귀환 가능하면 우유 개수 저장
	int home_dist = dist(si, sj, hi, hj);
	if (home_dist <= hp) maxcnt = max(maxcnt, cnt);

	bool flag = false; // 갈 수 있는 우유 체크를 위한 플래그


	// 다음 우유까지 체력이 되면 위치 이동 (backtrack)
	for (int i = 0; i < K; i++) {

		// 방문한 적 있으면 continue
		if (drink[i]) continue;


		auto[ni, nj] = milks[i];
		int milk_dist = dist(si, sj, ni, nj);
		if (milk_dist > hp) continue;

		flag = true;
		drink[i] = true;
		backtrack(ni, nj, cnt + 1, hp - milk_dist + H);
		drink[i] = false;
	}

	// 가지치기 : 집도 못가고 다음 우유도 못가면 종료
	if (!flag) return;
	
}

int dist(int x1, int y1, int x2, int y2) {
	return abs(x1 - x2) + abs(y1 - y2);
}