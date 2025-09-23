#include <iostream>
#include <vector>   // vector
#include <numeric>  // iota 함수

using namespace std;

int t, n, k, m;
vector<int> parent;  // 각 정점의 부모를 저장하는 Union-Find 를 위한 가변배열

int find_parent(int x) {  // x가 속한 집합의 대표를 찾는 함수
    if (parent[x] == x) return x;  // 자신이 대표라면

    parent[x] = find_parent(parent[x]);  // 재귀적으로 부모 찾고, 경로 압축
    return parent[x];  // 대표 반환
}

void union_parent(int a, int b) {  // a와 b가 속한 집합을 합침
    int ra = find_parent(a);  // 각 대표 찾고
    int rb = find_parent(b);

    if (ra != rb) parent[rb] = ra;  // 대표가 다르면 합침
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> n >> k;

        parent.assign(n + 1, 0);
        iota(parent.begin() + 1, parent.end(), 1);  // 각자 자기 자신을 부모로 가리키도록 초기화

        int a, b, u, v;
        for (int i = 0; i < k; i++) {
            cin >> a >> b;       // 서로 아는 사람
            union_parent(a, b);  // 두 사람을 같은 집합으로
        }

        cin >> m;
        cout << "Scenario " << tc << ":\n";
        for (int i = 0; i < m; i++) {
            cin >> u >> v;

            if (find_parent(u) == find_parent(v)) cout << "1\n";  // u, v가 같은 집합이면 1 출력
            else cout << "0\n";  // 아니면 0 출력
        }
        cout << '\n';
    }

    return 0;
}