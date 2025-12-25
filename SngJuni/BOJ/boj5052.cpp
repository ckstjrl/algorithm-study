#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);
    
    int t, n;
    cin >> t;
    while (t--) {
        cin >> n;

        vector<string> arr(n);  // 전화번호들을 문자열로 입력받아서 저장
        for (int i = 0; i < n; i++) cin >> arr[i];

        string res = "YES";
        unordered_map<string, int> um;  // 각 전화번호를 중복없이 저장
        for (int i = 0; i < n; i++) um[arr[i]]++;

        bool flag = true;
        for (int i = 0; i < n; i++) {  // 각 문자열 순회하면서
            if (!flag) break;
            for (int j = 1; j < arr[i].size(); j++) {
                if (um[arr[i].substr(0, j)]) {  // 부분 문자열(접두어)이 um에 존재하면 일관성 X
                    res = "NO";
                    flag = false;
                    break;
                }
            }
        }
        cout << res << '\n';
    }

    return 0;
}

/* ============================================================
   Trie 를 구현해서 해결하는 방식 (공부용)

#include <iostream>
#include <vector>
#include <string>
#include <array>

using namespace std;

struct Trie {
    struct Node {
        array<int, 128> nxt{};
        bool end = false;
        int child_cnt = 0;
        Node() { nxt.fill(-1); }
    };
    vector<Node> tr;
    Trie() { tr.push_back(Node()); }

    bool insert(const string& s) {
        int u = 0;
        for (int i = 0; i < (int)s.size(); ++i) {
            unsigned char c = s[i];
            if (tr[u].end) return true;
            if (tr[u].nxt[c] == -1) {
                tr[u].nxt[c] = (int)tr.size();
                tr[u].child_cnt++;
                tr.push_back(Node());
            }
            u = tr[u].nxt[c];
        }
        if (tr[u].end) return true;
        if (tr[u].child_cnt > 0) return true;
        tr[u].end = true;
        return false;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        vector<string> a(n);
        for (int i = 0; i < n; ++i) cin >> a[i];

        Trie trie;
        bool bad = false;
        for (auto& s : a) {
            if (!bad && trie.insert(s)) bad = true;
        }
        cout << (bad ? "NO" : "YES") << '\n';
    }
    return 0;
}

============================================================ */
