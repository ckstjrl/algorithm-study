/*** 15686. 치킨 배달 ***/

#include<iostream>
#include<vector>
#include<cmath>
#include<algorithm>
using namespace std;

vector<pair<int, int>> house;
vector<pair<int, int>> chicken;
vector<bool> visited;
int N, M, min_dist = 1400;

void backtrack(int idx, int m);
int cal_dist(int x1, int y1, int x2, int y2);

int main() {
	cin >> N >> M;

	for (int i = 0; i < N; i++) {
		for (int j = 0; j < N; j++) {
			int temp;
			cin >> temp;
			if (temp == 1) house.emplace_back(i, j);
			else if (temp == 2) chicken.emplace_back(i, j);
		}
	}

	visited.assign(chicken.size(), false);

	backtrack(0, 0);

	cout << min_dist;

	return 0;
}

void backtrack(int idx, int m) {
	if (m == M) { // 집 M개 골랐으면 거리 계산
		int dist = 0;
		for (int h = 0; h < house.size(); h++) {
			int min_house_dist = 105;
			auto [hi, hj] = house[h];
			for (int c = 0; c < chicken.size(); c++) {
				if (visited[c] == false) continue; // 치킨집 선택 안했으면 패스
				auto [ci, cj] = chicken[c];
				int temp_dist = cal_dist(hi, hj, ci, cj); // 거리 계산
				min_house_dist = min(min_house_dist, temp_dist); // 해당 집과 치킨집의 최소 거리 갱신
			}
			dist += min_house_dist; // 해당 집과 치킨집 최소 거리를 총거리에 저장
		}
		min_dist = min(min_dist, dist); // 최소 치킨 거리 갱신
		return;
	}

	for (int i = idx; i < chicken.size(); i++) { // 치킨집 선택
		visited[i] = true;
		backtrack(i+1, m + 1);
		visited[i] = false;
	}
}

int cal_dist(int x1, int y1, int x2, int y2) {
	return abs(x1 - x2) + abs(y1 - y2);
}