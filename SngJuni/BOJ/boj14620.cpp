#include <iostream>
#include <vector>
#include <queue>
#include <climits>

using namespace std;

int N, res = INT_MAX;
vector<vector<int>> arr;
vector<vector<int>> used;
vector<pair<int, int>> cand;

int dx[4] = {0, 0, -1, 1};
int dy[4] = {-1, 1, 0, 0};

int calc_cost(int i, int j) {
    int cost = arr[i][j];

    for (int k = 0; k < 4; k++) {
        int ny = i + dy[k];
        int nx = j + dx[k];

        if (nx < 0 || nx >= N || ny < 0 || ny >= N) return -1;
        if (used[ny][nx]) return -1;

        cost += arr[ny][nx];
    }

    return cost;
}

void use(int i, int j, int c) {
    used[i][j] = c;
    for (int k = 0; k < 4; k++) {
        int ny = i + dy[k];
        int nx = j + dx[k];
        used[ny][nx] = c; 
    }
}

void dfs(int idx, int depth, int total) {
    if (depth == 3) {
        res = min(res, total);
        return;
    }

    if (total >= res) return;

    if (idx == cand.size()) return;
    if (depth + (cand.size() - idx) < 3) return;

    for (int i = idx; i < cand.size(); i++) {
        int y = cand[i].first;
        int x = cand[i].second;
        
        int c = calc_cost(y, x);
        if (c == -1) continue;

        use(y, x, 1);
        dfs(i + 1, depth + 1, total + c);
        use(y, x, 0);
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    cin >> N;
    arr.assign(N, vector<int>(N, 0));
    used.assign(N, vector<int>(N, 0));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> arr[i][j];
        }
    }

    for (int i = 0; i < N - 1; i++) {
        for (int j = 0; j < N - 1; j++) {
            cand.push_back({i, j});
        }
    }

    dfs(0, 0, 0);

    cout << res << '\n';

    return 0;
}