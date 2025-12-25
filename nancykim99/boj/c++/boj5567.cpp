/*
BOJ5567 : 결혼식 (S2)

해결 방법 : 일단 인접리스트 구해서, 그래프 형태로 만들고, bfs를 상근이를 기준으로 실행.
상근이가 1이기에, 3까지는 초대할 친구이기에 친구들 중에 3까지의 친구들의 수를 구하기.
*/

#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> lst(n + 1);
    for (int i = 0; i < m; i++) {
        int a, b;
        cin >> a >> b;
        lst[a].push_back(b);
        lst[b].push_back(a);
    }

    vector<int> visited(n + 1, 0);
    queue<int> q;

    q.push(1);
    visited[1] = 1;  

    while (!q.empty()) {
        int t = q.front();
        q.pop();
        for (int friendNode : lst[t]) {
            if (!visited[friendNode]) {
                visited[friendNode] = visited[t] + 1;  
                q.push(friendNode);
            }
        }
    }

    int cnt = 0;
    for (int i = 2; i <= n; i++) {
        if (visited[i] > 1 && visited[i] <= 3) {
            cnt++;
        }
    }

    cout << cnt << '\n';
    return 0;
}
