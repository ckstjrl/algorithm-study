#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s1, s2;
    cin >> s1 >> s2;

    int m = s2.size();

    vector<char> st;  // 스택처럼 사용할 vector 배열

    for (char c : s1) {   // 첫번째 문자열 순회하면서
        st.push_back(c);  // 현재 문자를 스택에 push

        if (st.size() >= m && st.back() == s2.back()) {  // 스택의 끝이 폭탄 문자열의 끝과 같을 때만 폭탄인지 판단
            bool flag = true;
            for (int i = 0; i < m; i++) {  // 스택의 끝 부분과 폭탄 문자열이 같은지 확인
                if (st[st.size() - m + i] != s2[i]) {
                    flag = false;
                    break;
                }
            }
            if (flag) {  // 같으면 뒤에서부터 m개의 문자 pop
                for (int i = 0; i < m; i++) st.pop_back();
            }
        }
    }

    string res = "";
    if (st.empty()) res += "FRULA";  // 남아있는 문자가 없는 경우
    else {
        for (int i = 0; i < st.size(); i++) {  // 남은 문자 res 배열에 담음
            res += st[i];
        }
    }

    cout << res << '\n';  // 결과 출력

    return 0;
}