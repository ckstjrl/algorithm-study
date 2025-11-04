/*** 1068. 트리 ***/

#include<iostream>
#include<vector>
#include<stack>
using namespace std;

void dfs(int start);

int N, del, root;
vector<int> graph[50];  // 인접 리스트
int cnt = 0;
bool deleted[50] = { false };   // 삭제할 노드 표시

int main() {
	// 입력
	cin >> N;
	for (int i = 0; i < N; i++) {
		int parent;
		cin >> parent;
		if (parent == -1) {
			root = i;
			continue;
		}
		graph[parent].push_back(i);
	}
	cin >> del;

	// 노드 삭제
	dfs(del);
	
	// 리프 노드 카운트
	for (int j = 0; j < N; j++) {
		if (!deleted[j]) {  // 삭제한 노드가 아니면 true
			bool isleaf = true;
			for (int child : graph[j]) {
				if (!deleted[child]) {  // 자식 노드가 있으면 false
					isleaf = false;
					break;
				}
			}

			if (isleaf) cnt++;  // 리프 노드가 맞으면 카운트 증가
		}
	}

	cout << cnt;

	return 0;
}

void dfs(int start) {
	stack<int> s;
	s.push(start);

	deleted[start] = true;  

	while (!s.empty()) {
		int current = s.top();
		s.pop();

		deleted[current] = true;


		for (int i = 0; i < graph[current].size(); i++) {
			int next = graph[current][i];

			if (!deleted[next]) {
				deleted[next] = true;
				s.push(next);
			}
		}
	}
}