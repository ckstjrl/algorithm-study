/*** 16928. 뱀과 사다리 게임 ***/

#include<iostream>
#include<vector>
#include<deque>
using namespace std;

int bfs(int s);

vector<vector<int>> map(101, vector<int>()); // 칸에 도착했을 때 이동해야 할 칸 저장할 배열

int main() {
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < n + m; i++) {
		int a, b;
		cin >> a >> b;
		map[a].push_back(b);	// 사다리의 출발(a) 배열에 도착칸(b) 저장
	}

	for (int j = 0; j < 101; j++) {
		if (map[j].size() == 0) {	// 출발 배열에 아무것도 없다면 제자리 저장
			map[j].push_back(j);
		}
	}

	cout << bfs(1);

	return 0;
}

int bfs(int s) {
	int visited[101] = { 0, };	// 방문 번호 저장을 위한 배열
	deque<int> q;
	q.push_back(s);	// 시작점 저장 후 방문 표시
	visited[s] = 1;

	while (!q.empty()) {
		int t = q.front();	// 현재 위치
		q.pop_front();
		if (t == 100) {	// 현재 위치가 100번 칸이면 방문번호 -1 반환
			return visited[t] - 1;
		}
		for (int i = 1; i < 7; i++) {	// 주사위 굴림
			int ni = t + i;	// 이동할 칸
			if (ni > 100) {	// 이동할 칸이 100번 칸을 넘으면 이동 안함
				continue;
			}
			int w = map[ni][0];	// 이동하여 도착한 칸
			if (visited[w] == 0 || visited[w] > visited[t] + 1) {	// 도착한 칸이 첫 방문이거나 방문했던 번호보다 작으면 갱신
				visited[w] = visited[t] + 1;
				q.push_back(w);	// 이동한 위치 저장
			}
		}
	}
	return 0;
}