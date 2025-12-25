#include <iostream>
#include <vector>
#include <stack>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int N;
    cin >> N;

    vector<int> arr(N);
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    vector<int> res(N, -1);
    stack<int> stk;

    for (int i = 0; i < N; i++) {
        while (!stk.empty() && arr[stk.top()] < arr[i]) {
            res[stk.top()] = arr[i];
            stk.pop();
        }
        stk.push(i);
    }

    for (int i = 0; i < N; i++) {
        cout << res[i] << ((i == N - 1) ? '\n' : ' ');
    }

    return 0;
}