/*
BOJ16398 : 행성 연결 (G4)

해결 방법 : 모든 노드를 다 연결하면서 최소 비용을 구하는 문제 -> MST
노드가 많지 않기에, 크루스칼로 해결

메모 : 
모든 간선을 넣었다가, 테케는 다 나오는데 틀려서 다시 보니, 간선을 반만 넣었어야 했음

- 구조체(struct) : 하나 이상의 변수를 그룹 지어서 새로운 자료형을 정의하는 것
```
struct Edge {
    int cost;
    int a;
    int b;
};
```
- sort 하는 법 : `sort(컨테이너.begin(), 컨테이너.end(), 정렬기준);`
```
sort(edges.begin(), edges.end(),
    [](const Edge& x, const Edge& y) {
        return x.cost < y.cost;
    }
);
```
- 속도를 빠르게 하는 방법 : 
```
ios::sync_with_stdio(false);
cin.tie(NULL);
```
- c++에는 union이라는 예약어가 있음 -> 다른걸로 함수 이름 설정
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int find_func(vector<int>& parent, int x) {
    if (parent[x] != x) {
        parent[x] = find_func(parent, parent[x]);
    }
    return parent[x];
}

void union_func(vector<int>& parent, int a, int b) {
    a = find_func(parent, a);
    b = find_func(parent, b);
    if (a < b) parent[b] = a;
    else parent[a] = b;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<vector<int>> fee_arr(n, vector<int>(n));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> fee_arr[i][j];
        }
    }

    vector<tuple<int,int,int>> edges;
    int edges_num = (n * (n - 1)) / 2;
    long long total_cost = 0;

    // edges 정보 만들기
    for (int i = 0; i < n; i++) {
        for (int j = (i+1); j < n; j++) {
            if (i != j) {
                int a = i;
                int b = j;
                int cost = fee_arr[i][j];
                edges.push_back({cost, a, b});
            }
        }
    }

    sort(edges.begin(), edges.end());

    vector<int> parent(n + 1);
    for (int i = 1; i <= n; i++) {
        parent[i] = i;
    }

    for (int i = 0; i < edges_num; i++) {
        int cost, a, b;
        tie(cost, a, b) = edges[i];

        if (find_func(parent, a) != find_func(parent, b)) {
            union_func(parent, a, b);
            total_cost += cost;
        }
    }

    cout << total_cost << "\n";
    return 0;
}