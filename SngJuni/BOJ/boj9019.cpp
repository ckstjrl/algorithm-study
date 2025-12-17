#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

int A, B;
string res;

int opD(int x) {
    return (x * 2) % 10000;
}

int opS(int x) {
    return (x == 0 ? 9999 : x - 1);
}

int opL(int x) {
    return (x % 1000) * 10 + (x / 1000);
}

int opR(int x) {
    return (x % 10) * 1000 + (x / 10);
}

void bfs() {
    vector<int> prev(10000, -1);
    vector<char> how(10000);
    vector<bool> visited(10000, false);

    queue<int> q;
    q.push(A);
    visited[A] = true;

    while (!q.empty()) {
        int cur = q.front();
        q.pop();

        if (cur == B) break;

        int next[4] = { opD(cur), opS(cur), opL(cur), opR(cur) };
        char cmd[4] = { 'D', 'S', 'L', 'R' };

        for (int i = 0; i < 4; i++) {
            int nx = next[i];

            if (visited[nx]) continue;

            q.push(nx);
            visited[nx] = true;
            prev[nx] = cur;
            how[nx] = cmd[i];
        }
    }

    res.clear();

    for (int x = B; x != A; x = prev[x]) {
        res.push_back(how[x]);
    }
    reverse(res.begin(), res.end());
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;

    while (T--) {
        cin >> A >> B;
        bfs();
        
        cout << res << '\n';
    }

    return 0;
}
