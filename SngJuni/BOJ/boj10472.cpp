#include <iostream>
#include <queue>
#include <unordered_map>
#include <string>

using namespace std;

void toggle(string& b, int pos) {
    int y = pos / 3;
    int x = pos % 3;

    const int dx[5] = {0, 0, 0, -1, 1};
    const int dy[5] = {0, -1, 1, 0, 0};

    for (int k = 0; k < 5; k++) {
        int nx = x + dx[k];
        int ny = y + dy[k];

        if (nx < 0 || nx >= 3 || ny < 0 || ny >= 3) continue;

        int idx = ny * 3 + nx;
        b[idx] = (b[idx] == '.' ? '*' : '.');
    }
}

int bfs(const string& tar) {
    const string start = ".........";

    if (start == tar) return 0;

    queue<string> q;
    unordered_map<string, int> dist;

    q.push(start);
    dist[start] = 0;

    while (!q.empty()) {
        string cur = q.front();
        q.pop();

        int curDist = dist[cur];

        for (int i = 0; i < 9; i++) {
            string nxt = cur;
            toggle(nxt, i);

            if (dist.find(nxt) == dist.end()) {
                dist[nxt] = curDist + 1;

                if (nxt == tar) return dist[nxt];

                q.push(nxt);
            }
        }
    }
    
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int P;
    cin >> P;


    while (P--) {
        string target(9, '.');

        for (int i = 0; i < 3; i++) {
            string s;
            cin >> s;
            for (int j = 0; j < 3; j++) {
                target[i * 3 + j] = s[j];
            }
        }

        cout << bfs(target) << '\n';
    }

    return 0;
}