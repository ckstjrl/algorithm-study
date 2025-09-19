/*** 1261. 알고스팟 ***/

#include<iostream>
#include<vector>
#include<queue>
#include<string>
#include<climits>	// 무한대 값 INT_MAX 사용을 위한 라이브러리
using namespace std;

int dijkstra(int si, int sj);

vector<vector<int>> maze;
vector<vector<int>> dists;	// 벽을 부순 횟수의 최소값 찾기 위한 배열
int M, N;
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };

int main() {
	cin >> M >> N;
	maze.assign(N, vector<int>(M));
	dists.assign(N, vector<int>(M, INT_MAX));

	for (int i = 0; i < N; i++) {
		string line;
		cin >> line;
		for (int j = 0; j < M; j++) {
			maze[i][j] = line[j] - '0';
		}
	}

	int result = dijkstra(0, 0);	// 시작 지점에서 다익스트라 시작
	cout << result;

	return 0;
}

int dijkstra(int si, int sj) {
	priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
	pq.push({ 0, { si, sj } }); // {가중치, {x좌표, y좌표}}
	dists[si][sj] = 0;


	while(!pq.empty()) {
		int dist = pq.top().first;
		int ti = pq.top().second.first;
		int tj = pq.top().second.second;
		pq.pop();

		if (dists[ti][tj] < dist) continue;

		for (int i = 0; i < 4; i++) {
			int ni = ti + di[i];
			int nj = tj + dj[i];

			if (ni < 0 || ni >= N || nj < 0 || nj >= M) continue;

			int new_dist = dist;	// 기본값으로 빈방이라고 생각하고 경로값 유지
			if (maze[ni][nj]) new_dist++;	// 해당 위치가 벽이면 가중치 1 을 더함
			if (dists[ni][nj] <= new_dist) continue;

			dists[ni][nj] = new_dist;
			pq.push({ new_dist, {ni, nj} });
		}
	}

	return dists[N - 1][M - 1];	// 종료 지점의 최단 거리 반환
}


/* (21줄)
 limits라이브러리의 INFINITY는 float형이다. climits 라이브러리의 INT_MAX가 int형이다.
*/

/* (23~29줄)
 공백없는 입력을 cin >> maze[i][j]로 받았더니 각각의 요소로 입력이 들어가지 않고, 통째로 들어갔다.
 string으로 한줄을 한번에 입력받고 각 배열에 요소를 int형으로 변환하여 저장했다. 그러나 아스키코드가 숫자로만 바뀌어 0이 48로 저장되었다.
 0과 1을 저장하기 위해 아스키코드 '0'을 빼서 정수로 저장하였다.
*/

/* (38줄)
 가중치와 좌표를 넣어야 하므로 우선순위 큐에 3개의 요소를 넣기 위해 tuple로 선언하였다.
 그러나 tuple은 가중치와 좌표가 다 정렬의 키로 사용된다.
 가중치만 키로 사용해야 하기 때문에 요소 좌표를 포함하여 요소 3개를 받아야 한다면 pair를 중첩하여 사용하도록 하자!
*/

/* (47줄)
 pq.pop()을 넣지 않아 무한 루프에 빠졌다.
 코드를 암기하려고 하지 말고 알고리즘을 떠올리면서 작성하자...
*/