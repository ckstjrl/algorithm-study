/*** 2533. 사회망 서비스(SNS) ***/

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

// 인접 리스트, dp, visited 생성
// dp는 2차원 배열로 [node][state] 형식으로 사용
// dp 배열 요소의 값 = 얼리어답터의 수
// 1을 루트노드라 가정, dfs 진행
// 일단 dp[node][0]=0, dp[node][1]=1 저장
// 인접 노드로 이동 후 dfs 실행
// 인접 노드에서의 dp 결과를 현재 노드의 dp에 합산

void dfs(int node);

vector<vector<int>> graph;
vector<int> visited;
int dp[1000001][2];
int N;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> N;
	graph.assign(N + 1, {});
	visited.assign(N + 1, 0);

	// 인접 리스트 생성
	for (int i = 0; i < N - 1; i++) {
		int u, v;
		cin >> u >> v;
		graph[u].push_back(v);
		graph[v].push_back(u);
	}

	dfs(1); // 루트 노드를 1이라 가정하고 dfs

	cout << min(dp[1][0], dp[1][1]); // 루트 노드 dp의 최소값 출력
	
	return 0;
}

void dfs(int node) {
	visited[node] = 1;
	dp[node][0] = 0;
	dp[node][1] = 1;

	for (int child : graph[node]) {
		if (visited[child]) continue;	// 양방향으로 저장했기 때문에 방문했던 노드면 pass
		dfs(child);	// 재귀

		// 재귀 종료 후 node dp에 자식 노드의 dp 더함.
		dp[node][0] += dp[child][1];	// 현재 노드가 얼리가 아니면 자식은 무조건 얼리
		dp[node][1] += min(dp[child][0], dp[child][1]);	// 현재 노드가 얼리면 자식 dp 중 최소값 합산
	}
}