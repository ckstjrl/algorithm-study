/*** 2665. 미로만들기 ***/

#include<iostream>
#include<queue>
#include<tuple>
#include<string>
using namespace std;

const int INF = 1e9;
int rooms[51][51], black[51][51]; // rooms : 입력받은 방의 정보, black : 최소한으로 바꾼 방의 개수
int n;
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };

void find_goal();

int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		string line;
		cin >> line;
		for (int j = 0; j < n; j++) {
			rooms[i][j] = line[j] - '0';
			black[i][j] = INF;
		}
	}

	find_goal();

	cout << black[n - 1][n - 1];

	return 0;
}

void find_goal() {
	priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;

	pq.push({ 0, 0, 0 });
	black[0][0] = 0;

	while (!pq.empty()) {
		auto[cd, ci, cj] = pq.top();
		pq.pop();

		if (black[ci][cj] < cd) continue;

		for (int d = 0; d < 4; d++) {
			int ni = ci + di[d];
			int nj = cj + dj[d];
			if (ni < 0 || ni >= n || nj < 0 || nj >= n) continue;

			int nd = cd;
			if (!rooms[ni][nj]) nd += 1; // 검은 방이면 바꾼 방 개수 추가

			if (black[ni][nj] <= nd) continue;
			black[ni][nj] = nd;
			pq.push({ nd, ni, nj });
		}
	}
}