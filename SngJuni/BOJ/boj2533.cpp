#include <iostream>
#include <vector>
#include <stack>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int N;
    cin >> N;

    vector<vector<int>> graph(N + 1);  // 간선 정보를 위한 인접리스트

    int u, v;
    for (int i = 0; i < N - 1; i++) {  // 간선 정보 입력 받음.
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u);
    }

    vector<int> parent(N + 1, 0), order;  // 각 정점의 부모와 탐색 순서 저장을 위한 배열
    order.reserve(N);

    stack<int> st;  // stack을 사용해서 dfs로 전위순회 순서 저장
    st.push(1);
    parent[1] = -1;
    
    while (!st.empty()) {
        int u = st.top();
        st.pop();
        order.push_back(u);

        for (const auto& v : graph[u]) {
            if (v != parent[u]) {
                parent[v] = u;
                st.push(v);
            }
        }
    }

    vector<int> dp0(N + 1, 0), dp1(N + 1, 0);  // dp0 -> 얼리 X, dp1 -> 얼리

    for (int i = order.size() - 1; i >= 0; i--) {  // 전위순회를 역순으로 순회 -> 후위 순회
        int u = order[i];
        int nEarly = 0, early = 1;

        for (const auto& v : graph[u]) {  // 각 자식들을 순회하면서
            if (v != parent[u]) {
                nEarly += dp1[v];              // 현재의 u 정점이 비얼리인 경우, 모두 얼리여야 함
                early += min(dp0[v], dp1[v]);  // 현재의 정점이 얼리인 경우, 자식 중 얼리 수 최소 선택
            }
        }

        dp0[u] = nEarly;  // u가 비얼리인 경우 갱신
        dp1[u] = early;   // u가 얼리인 경우 갱신
    }

    cout << min(dp0[1], dp1[1]) << '\n';

    return 0;
}