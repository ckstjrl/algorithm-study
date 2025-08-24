#include <iostream>
#include <stack>
#include <vector>

using namespace std;

int main() {
    int n, temp, num = 1, error_flag = false;

    stack<int> stk;
    vector<char> res;
    
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> temp;
        
        while (num <= temp) {      // temp 보다 현재 num 이 작은 동안 stack 에 push 하고 결과 배열 res 에 + 넣어줌.
            stk.push(num++);
            res.push_back('+');
        }

        if (stk.top() == temp) {   // temp 와 stack 의 top 이 같으면 pop 하고 결과 배열 res 에 - 넣어줌.
            stk.pop();
            res.push_back('-');
        } else {                   // top 이 temp 보다 클 때 -> 수열 불가능
            error_flag = true;
        }
    }

    if (error_flag) {
        cout << "NO\n";
    } else {
        for (int i = 0; i < res.size(); i++) {
            cout << res[i] << "\n";
        }
    }

    return 0;
}