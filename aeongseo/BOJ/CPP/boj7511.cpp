/*** 7511. 소셜 네트워킹 어플리케이션 */

#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int find_set(int x);
void merge(int x, int y);

vector<int> parent;	// 부모노드
vector<int> ran;	// rank

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc < T + 1; tc++) {
		vector<int> ans;
		int n, k, m;
		cin >> n >> k;
		parent.assign(n, 0);
		ran.assign(n, 0);

		// make set
		for (int i = 0; i < n; i++) {
			parent[i] = i;
			ran[i] = 1;
		}
		
		for (int j = 0; j < k; j++) {
			int a, b;
			cin >> a >> b;
			merge(a, b);	// 두 노드 연결하기
		}

		cin >> m;
		for (int k = 0; k < m; k++) {
			int c, d;
			cin >> c >> d;
			if (find_set(c) == find_set(d)) ans.push_back(1); // 두 노드의 부모 노드가 같으면 1 저장
			else ans.push_back(0);	// 부모 노드가 다르면 0 저장
		}

		cout << "Scenario " << tc << ":" << '\n';
		for (int l = 0; l < ans.size(); l++) {
			cout << ans[l] << '\n';
		}
		cout << '\n';
	}

	return 0;
}

int find_set(int x) {
	if (x == parent[x]) return x;	// x의 부모 노드가 자기자신이라면 x 반환
	return parent[x] = find_set(parent[x]);
}

void merge(int x, int y) {
	x = find_set(x);	// x의 부모 노드 찾기
	y = find_set(y);	// y의 부모 노드 찾기

	if (x == y) return;	// x와 y의 부모 노드가 같다면 병합 성공
	if (ran[x] > ran[y]) swap(x, y);	// x의 깊이가 y의 깊이보다 높으면 swap
	parent[x] = y;	// x의 부모노드를 y로 저장
	if (ran[x] == ran[y]) ran[y]++;	// x와 y의 깊이가 같으면 y의 깊이 1 증가
}