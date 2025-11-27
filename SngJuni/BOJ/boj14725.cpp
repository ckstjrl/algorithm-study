#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

// 트라이(Trie) 구조를 위한 map 배열
// nxt[i] = i번째 노드에서 이어지는 자식 노드들
// map<string, int> = (문자열 -> 자식 노드 인덱스)
vector<map<string, int>> nxt(1);

// 현재 노드 u 기준으로 depth에 맞춰서 출력
void dfs(int u, int depth) {
    for (auto& p : nxt[u]) {
        for (int i = 0; i < depth; i++) {
            cout << "--";  // 현재 깊이에 따라 -- 출력
        }
        cout << p.first << '\n';   // 현재 층 문자열 출력
        dfs(p.second, depth + 1);  // 자식 노드 재귀 탐색
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    int K;
    for (int i = 0; i < N; i++) {  // N개의 먹이 정보 순회
        cin >> K;

        int cur = 0;  // 루트 노드에서 시작
        string s;
        for (int j = 0; j < K; j++) {
            cin >> s;
            
            if (!nxt[cur].count(s)) {      // 현재 노드에 해당 문자열 자식이 없으면
                nxt[cur][s] = nxt.size();  // 새 노드 번호 할당
                nxt.push_back({});         // 새 노드 생성
            }
            cur = nxt[cur][s];  // 다음 노드로 이동
        }
    }

    dfs(0, 0);  // 루트부터 dfs로 출력

    return 0;
}