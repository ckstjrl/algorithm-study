/*
BOJ1389 : 케빈 베이컨의 6단계 법칙 (S1)

해결 방법 :
1. 친구들을 쌍방으로 인접리스트에 넣기
2. bfs로 각 친구들까지의 거리를 구하기
3. 각 bfs의 최소합을 구해 최소거리합을 구해, 친구 사이가 젤 적은 친구 찾기

메모 : 
- `friend`가 c++에 이미 클래스로 있다고 한다... 세상에
- bfs 및 최소합 구하는게 너무 어려웠다.
*/

#include <iostream>
#include <vector>
#include <queue>
#include <numeric>
#include <algorithm>
#include <climits>

using namespace std;

int bfs(int num, const vector<vector<int>>& friends, vector<int>& visited) {
    queue<int> q;
    q.push(num);
    visited[num] = 0;

    while (!q.empty()) {
        int t = q.front();
        q.pop();

        for (int nxt : friends[t]) {            
            if (visited[nxt] == 0 && nxt != num) {
                q.push(nxt);
                visited[nxt] = visited[t] + 1;
            }
        }
    }

    return accumulate(visited.begin(), visited.end(), 0);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<vector<int>> friends(n + 1);
    for (int i = 0; i < m; ++i) {
        int a, b;
        cin >> a >> b;
        friends[a].push_back(b);
        friends[b].push_back(a);
    }

    vector<int> temp;
    int x = INT_MAX;

    for (int i = 1; i <= n; ++i) {
        vector<int> visited(n + 1, 0);
        int y = bfs(i, friends, visited);

        if (y < x) {
            x = y;
            temp.clear();
            temp.push_back(i);
        } else if (y == x) {
            temp.push_back(i);
        }
    }

    cout << *min_element(temp.begin(), temp.end()) << '\n';
    return 0;
}