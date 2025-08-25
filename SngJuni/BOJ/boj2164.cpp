#include <iostream>
#include <deque>

using namespace std;

int main() {
    int n;
    cin >> n;

    deque<int> dq;
    for (int i = 1; i <= n; i++) {
        dq.push_back(i);
    }

    while (1) {
        if (dq.size() > 1) {     // dq가 비지 않았으면 pop
            dq.pop_front();
        } else break;
        if (dq.size() > 1) {     // dq가 비지 않았으면 맨 앞의 카드를 맨 뒤로
            dq.push_back(dq[0]);
            dq.pop_front();
        } else break;
    }
    cout << dq[0];

    return 0;
}