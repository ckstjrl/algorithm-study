 /*
 BOJ2504 - 괄호의 값

 문제 정의
 1. 한 쌍의 괄호로만 이루어진 '()', '[]'는 올바른 괄호열
 2. 만일 X가 올바른 괄호열이면 '(X)'나 '[X]'도 모두 올바른 괄호열
 3. X와 Y가 모두 올바른 괄호열이라면 이들을 결합한 XY도 올바른 괄호열

 '()' 인 괄호열의 값은 2이다.
'[]' 인 괄호열의 값은 3이다.
'(X)' 의 괄호값은 2×값(X) 으로 계산된다.
'[X]' 의 괄호값은 3×값(X) 으로 계산된다.
즉 괄호 내의 값은 곱하기 처리된다.
XY는 X+Y로 된다
올바르지 못한 괄호열이면 0 아니면 값을 출력

로직 정의
문자열을 앞에서부터 돌아가면서 열린 괄호가 나오면 temp를 2로 만들고 또 다른 열린 괄호가 연속이라면 temp에 곱해주는 형식
만약 닫힌 괄호라면 스택에 들어간 값과 비교해서 ans에 더해주고 해당 괄호값을 temp에서 나눠주기
스택이 남아있다면 0 출력 (() 같은 문제 해결용
그렇지 않다면 ans 출력
*/

#include <iostream>
#include <stack>
#include <string>

using namespace std;

int ans = 0;
int temp = 1;

string brackets;
stack<char> st;

int main() {
    cin >> brackets;
    for (int i = 0; i < brackets.size(); i++){
        if (brackets[i] == '('){
            temp *= 2;
            st.push(brackets[i]);
        }
        else if (brackets[i] == '['){
            temp *= 3;
            st.push(brackets[i]);
        }
        else if (brackets[i] == ')'){
            if (st.empty() || st.top() != '('){
                ans = 0;
                break;
            }
            if (brackets[i-1] == '(') {
                ans += temp;
            }
            st.pop();
            temp /= 2;
        }
        // else 쓰면 헷갈려서...
        else if (brackets[i] == ']'){
            if (st.empty() || st.top() != '['){
                ans = 0;
                break;
            }
            if (brackets[i-1] == '[') {
                ans += temp;
            }
            st.pop();
            temp /= 3;
        }
    }
    if (st.empty()){
        cout << ans;
    }
    else{
        cout << 0;
    }

    return 0;
}