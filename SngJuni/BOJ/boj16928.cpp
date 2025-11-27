#include <iostream>
#include <queue>

using namespace std;

int n, m;
int board[101];
int dist[101];

void bfs(int i) {
    queue<int> q;
    q.push(i);
    dist[i] = 0;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        for (int j = 1; j <= 6; j++) {
            int next = cur + j;

            if (next > 100) continue;
            if (dist[board[next]] == -1) {
                q.push(board[next]);
                dist[board[next]] = dist[cur] + 1;
            }
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> n >> m;

    for (int i = 0; i < 101; i++) {
        board[i] = i;
        dist[i] = -1;
    }

    int x, y;
    for (int i = 0; i < n; i++) {
        cin >> x >> y;
        board[x] = y;
    }
    for (int i = 0; i < m; i++) {
        cin >> x >> y;
        board[x] = y;
    }
    
    bfs(1);

    cout << dist[100]<< '\n';

    return 0;
}