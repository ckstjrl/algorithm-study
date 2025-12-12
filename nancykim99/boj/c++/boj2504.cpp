/*
BOJ2504 : 괄호의 값 (G5)

해결 방법 :
1. 문자열을 스택에 하나씩 넣으면서 확인하기
2. 여는 괄호 -> 스택에 넣기
3. 닫는 괄호 -> 여는 괄호면, 괄호 값을 스택에 넣기
    3-2. 숫자들이면, 다 더해서 계산해서 스택에 넣기
4. 스택에 숫자만 있으면, 합하기 -> 정답
*/

#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    string s;
    if (!(cin >> s)) return 0;

    vector<int> st;  
    bool flag = true;
    int ans = 0;

    for (char b : s) {
        if (!flag) break;

        if (b == '(') {
            st.push_back(-1);
            continue;
        } else if (b == '[') {
            st.push_back(-2);
            continue;
        }

        if (b == ')' || b == ']') {
            vector<int> n;
            bool inner = true;

            while (inner) {
                if (st.empty()) {
                    ans = 0;
                    flag = false;
                    break;
                }

                int p = st.back();
                st.pop_back();

                if (p > 0) {  
                    n.push_back(p);
                } else if (p != -1 && p != -2) {  
                    ans = 0;
                    flag = false;
                    inner = false;
                } else {  
                    if (b == ')' && p == -1) {  
                        int a;
                        if (!n.empty()) {
                            int sum = 0;
                            for (int v : n) sum += v;
                            a = sum * 2;
                        } else {
                            a = 2;
                        }
                        st.push_back(a);
                        inner = false;
                    } else if (b == ']' && p == -2) {  
                        int a;
                        if (!n.empty()) {
                            int sum = 0;
                            for (int v : n) sum += v;
                            a = sum * 3;
                        } else {
                            a = 3;
                        }
                        st.push_back(a);
                        inner = false;
                    } else {  
                        ans = 0;
                        flag = false;
                        inner = false;
                    }
                }
            }
        }
    }

    if (!flag) {
        cout << 0 << '\n';
    } else {
        for (int x : st) {
            if (x <= 0) {  
                cout << 0 << '\n';
                return 0;
            }
            ans += x;
        }
        cout << ans << '\n';
    }

    return 0;
}
