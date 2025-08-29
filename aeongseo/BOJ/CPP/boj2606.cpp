/*** 2606. 바이러스 ***/

#include<iostream>
#include<vector>
#include<queue>
using namespace std;

int bfs(int s, int v, vector<vector<int>> adj_l);

int cnt;	// 컴퓨터 수 세기 위한 전역 변수

int main() {
	int V, E;
	cin >> V >> E;
	vector<vector<int>> arr(E, vector<int>(2));

	for (int i = 0; i < E; i++) {	// 연결된 컴퓨터 번호 입력받음
		cin >> arr[i][0] >> arr[i][1];
	}

	vector<vector<int>> adj_l(V + 1);
	for (int i = 0; i < E; i++) {	// 입력받은 컴퓨터 번호를 각 노드별 연결된 노드 리스트에 저장
		adj_l[arr[i][0]].push_back(arr[i][1]);
		adj_l[arr[i][1]].push_back(arr[i][0]);
	}

	int ans = bfs(1, V, adj_l);	// BFS
	cout << ans;

	return 0;
}

int bfs(int s, int v, vector<vector<int>> adj_l) {
	vector<int> visited(v + 1, 0);	// 방문 번호 배열
	queue<int> q;	// 큐 생성
	q.push(s);	// 시작 노드 push
	visited[s] = 1;	// 시작 노드 방문번호 1 저장
	
	while (!q.empty()) {	// 큐가 빌 때까지 반복
		int t = q.front();	// front값 저장후 pop
		q.pop();

		for (int j = 0; j < adj_l[t].size(); j++) {
			if (visited[adj_l[t][j]] == 0) {	// 방문한 적 없다면 큐에 push하고, 이전 방문 번호 + 1 저장
				q.push(adj_l[t][j]);
				visited[adj_l[t][j]] = visited[t] + 1;
				cnt++;	// 카운트 증가
			}
		}
	}

	return cnt;
}