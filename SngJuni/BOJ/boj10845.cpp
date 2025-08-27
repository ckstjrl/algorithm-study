#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int n;
    cin >> n;

    queue<int> q;  // queue 자료구조 사용
    string op;

    for (int i = 0; i < n; i++) {  // 각
        cin >> op;
        if (op == "push") {
            int x;
            cin >> x;
            q.push(x);
        } else if (op == "pop") {
            if (!q.empty()) {
                cout << q.front() << '\n';
                q.pop();
            }
            else cout << "-1\n";
        } else if (op == "size") {
            cout << q.size() << '\n';
        } else if (op == "empty") {
            if (!q.empty()) cout << "0\n";
            else cout << "1\n";
        } else if (op == "front") {
            if (!q.empty()) cout << q.front() << '\n';
            else cout << "-1\n";
        } else if (op == "back") {
            if (!q.empty()) cout << q.back() << '\n';
            else cout << "-1\n";
        }
    }

    return 0;
}