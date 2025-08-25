#include <iostream>
#include <stack>

using namespace std;

int main() {
    int k, temp, res = 0;
    cin >> k;
    
    stack<int> stk;            // stack 자료구조 사용
    
    while (k--) {
        cin >> temp;
        if (temp != 0) {       // 0이 아니면 해당 수 stack에 push
            stk.push(temp);
        }
        else if (temp == 0) {  // 0이면 stack에서 pop
            stk.pop();
        }
    }
    while (!stk.empty()) {     // stack에 남아있는 수들의 합 계산
        res += stk.top();
        stk.pop();
    }
    
    cout << res;
    return 0;
}