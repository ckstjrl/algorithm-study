#include <iostream>
#include <stack>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;
    
    int res = 0, temp = 1;
    stack<char> stk;  // 여는 괄호들 저장을 위한 스택

    for (int i = 0; i < s.size(); i++) {
        // 여는 소괄호
        if (s[i] == '(') {
            stk.push('(');
            temp *= 2;
        }
        // 여는 대괄호
        else if (s[i] == '[') {
            stk.push('[');
            temp *= 3;
        }
        // 닫는 소괄호
        else if (s[i] == ')') {
            // 스택이 비었거나 매칭되지 않으면 잘못된 문자열
            if (stk.empty() || stk.top() != '(') {
                res = 0;
                break;
            }

            // 바로 이전 문자가 여는 소괄호 -> temp 더함
            if (s[i - 1] == '(') {
                res += temp;
                temp /= 2;
                stk.pop();
            }
            // 바로 이전이 소괄호가 아니면 깊이 감소
            else {
                temp /= 2;
                stk.pop();
            }
        }
        // 닫는 대괄호
        else if (s[i] == ']') {
            // 스택이 비었거나 매칭되지 않으면 잘못된 문자열
            if (stk.empty() || stk.top() != '[') {
                res = 0;
                break;
            }

            // 바로 이전 문자가 여는 대괄호  -> temp 더함
            if (s[i - 1] == '[') {
                res += temp;
                temp /= 3;
                stk.pop();
            }
            // 닫기
            else {
                temp /= 3;
                stk.pop();
            }
        }
    }

    // 모든 괄호가 정상적으로 닫히지 않았다면
    if (!stk.empty()) res = 0;

    cout << res << '\n';  // 결과 출력
    
    return 0;
}