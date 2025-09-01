#include <iostream>
#include <string>
#include <stack>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화
    cin.tie(NULL);

    vector<string> res;  // 결과를 위한 문자열 가변배열
    string line;  // 입력받을 문자열
    while (true) {
        getline(cin, line);  // 공백을 포함해서 한 줄씩 읽어옴.
        if (!line.empty() && line[0] == '.') break;  // 빈 값이 들어오거나 . 이 들어오면 반복문 탈출

        stack<char> stk;  // stack 사용
        bool flag = true; // 문자열 판단을 위한 flag
        for (int i = 0; i < line.size(); i++) {
            if (line[i] == '[' || line[i] == '(') {  // 여는 괄호 만나면 stack에 push
                stk.push(line[i]);
            } else if (line[i] == ']') {
                if (stk.empty() || stk.top() != '[') {  // stack이 비어있거나 top이 [ 가 아니면 균형 X
                    flag = false;
                    break;
                } else {
                    stk.pop();
                }
            } else if (line[i] == ')') {
                if (stk.empty() || stk.top() != '(') {  // stack이 비어있거나 top이 ( 가 아니면 균형 X
                    flag = false;
                    break;
                } else {
                    stk.pop();
                }
            }
        }
        if (!stk.empty()) flag = false;  // stack에 여는 괄호가 남아있어도 균형 X

        res.push_back(flag ? "yes" : "no");  // 해당 문자열에 대한 결과 저장
    }

    for (int i = 0; i < res.size(); i++) {  // 결과 출력
        cout << res[i] << '\n';
    }
    
    return 0;
}