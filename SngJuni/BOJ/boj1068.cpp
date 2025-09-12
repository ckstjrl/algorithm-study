#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int n, t, root, res;
vector<vector<int>> tree;  // 트리를 위한 2차원 가변배열
vector<bool> visited;      // 노드 방문정보를 위한 가변배열

void dfs(int r) {
    stack<int> stk;     // stack 을 사용해서 dfs 구현
    stk.push(r);        // root 를 stack 에 push
    visited[r] = true;  // 해당 노드 방문 체크

    while (!stk.empty()) { 
        int cur = stk.top();
        stk.pop();

        if (cur == t) continue;  // 해당 노드가 지워질 노드라면 해당 순회 종료

        int cnt = 0;  // 자식 노드의 갯수를 세기 위한 변수
        for (auto& next : tree[cur]) {  // 부모 노드가 가진 자식 노드 순회
            if (next == t) continue;    // 지워질 노드라면 해당 순회 종료

            cnt++;  // 자식 노드 갯수 1 증가
            if (!visited[next]) {  // 방문하지 않았다면 stack 에 push, 방문 체크
                stk.push(next);
                visited[next] = true;
            }
        }

        if (cnt == 0) res++;  // 자식 노드 갯수가 0 이라면 == 리프 노드라면, 갯수 1 증가
    }
}

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    cin >> n;

    tree.assign(n, {});         // {} 으로 초기화
    visited.assign(n, false);   // false 로 초기화

    int p;
    for (int i = 0; i < n; i++) {
        cin >> p;
        if (p == -1) {  // -1 이라면 루트 노드
            root = i;
        } else {        // 각 부모 노드가 가지는 자식 노드 저장
            tree[p].push_back(i);
        }
    }

    cin >> t;  // 지울 노드 번호 입력받음

    dfs(root);  // dfs 호출

    cout << res << '\n';  // 결과 출력

    return 0;
}