#include <iostream>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    stack<int> stk;
    int res = 0;

    int x, h;
    for (int i = 0; i < N; i++) {
        cin >> x >> h;

        while (!stk.empty() && stk.top() > h) {
            stk.pop();
            res++;
        }

        if (!stk.empty() && stk.top() == h) continue;
        if (h > 0) stk.push(h);
    }

    while (!stk.empty()) {
        if (stk.top() > 0) res++;
        stk.pop();
    }
    
    cout << res << '\n';

    return 0;
}