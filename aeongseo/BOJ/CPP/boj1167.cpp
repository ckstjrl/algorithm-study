/*** 1167. 트리의 지름 ***/

#include<iostream>
#include<vector>
#include<cstring>	// memset 사용 위해
using namespace std;

void dfs(int current, int s);

vector<pair<int, int>> graph[100001];	// {인접 노드, 거리} 저장
bool visited[100001];
int max_s = 0;
int far = 0;

int main() {
	ios_base::sync_with_stdio(false);	// scanf, printf와의 동기화를 끊음
	cin.tie(NULL);						// 쓰고 안쓰고의 속도 차이가 엄청남

	int V;
	cin >> V;

	for (int i = 0; i < V; i++) {
		int n1, n2, d;
		cin >> n1;	// 시작 노드
		while (1) {
			cin >> n2;
			if (n2 == -1) break;	// 연결된 노드가 아니라 종료 입력이면 break
			cin >> d;
			graph[n1].push_back({ n2, d });	// 인접리스트에 저장
			// graph[n2].push_back({ n1, d });
		}
	}

	/*더 간단한 입력 방법
	for (int i = 0; i < V; i++) {
		int n1, n2, d;
		cin >> n1;
		while (cin >> n2 && n2 != -1) {
			cin >> d;
			graph[n1].push_back({ n2, d });
		}
	}
	*/

	dfs(1, 0);	// 임의의 시작 지점에서 가장 먼 노드 찾기

	memset(visited, false, sizeof(visited));	// visited 배열 false로 초기화
	max_s = 0;	// 거리 최대값 0으로 초기화

	dfs(far, 0);	// 가장 먼 노드에서 트리의 지름 찾기

	cout << max_s;

	return 0;
}

void dfs(int current, int s) {
	visited[current] = true; 

	if (max_s < s) {
		max_s = s;
		far = current;
	}

	for (const auto& nodes: graph[current]) {
		int next = nodes.first;
		int dist = nodes.second;

		if (!visited[next]) {
			dfs(next, s + dist);
		}
	}
}