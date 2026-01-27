// BOJ 2668. 숫자고르기 / G5
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int num[101] = { 0 };
int visited[101] = { 0 };
int finish[101] = { 0 };
vector<int> ans;

void dfs(int x) {
	visited[x] = 1;
	int nxt = num[x];

	if (visited[nxt] == 0) {
		dfs(nxt);
	}
	else if(visited[nxt] == 1 && finish[nxt] == 0) {
		int cur = nxt;
		while (cur != x) {
			ans.push_back(cur);
			cur = num[cur];
		}
		ans.push_back(x);
	}
	finish[x] = 1;
}

int main() {
	int N;
	cin >> N;
	
	for (int i = 1; i < N + 1; i++) {
		cin >> num[i];
	}

	for (int i = 1; i < N + 1; i++) {
		if (visited[i] == 0) {
			dfs(i);
		}
	}

	sort(ans.begin(), ans.end());

	cout << ans.size() << "\n";
	for (int a : ans) {
		cout << a << "\n";
	}
}

/*
DFS 활용
visited로 방문 확인, finish로 DFS가 끝났는지 확인
순환이 될 수 있는 조건은 visited[nxt] == 1 && finish[nxt] == 0 인경우
이미 방문을 했지만 다시 돌아왔다.
*/