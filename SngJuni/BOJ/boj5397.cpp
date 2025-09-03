#include <iostream>
#include <string>
#include <list>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 속도 최적화
    cin.tie(NULL);

    int t;  // 테스트케이스 갯수
    cin >> t;
    while (t--) {
        string s;  // 입력된 문자열
        cin >> s;

        list<char> lst;        // 비밀번호 저장을 위한 연결리스트
        auto cur = lst.end();  // 커서의 현재 위치를 가리키는 iterator

        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '<') {         // 커서의 위치가 맨 앞이 아니라면 1 감소
                if (cur != lst.begin()) cur--;
            } else if (s[i] == '>') {  // 커서의 위치가 맨 뒤가 아니라면 1 증가
                if (cur != lst.end()) cur++;
            } else if (s[i] == '-') {  // 커서의 바로 앞에 글자가 존재한다면, 그 글자를 지움.
                if (cur != lst.begin()) {
                    cur--;
                    cur = lst.erase(cur);
                }
            } else {  // 입력된 문자열을 비밀번호에 저장
                lst.insert(cur, s[i]);
            }
        }

        for (auto cur = lst.begin(); cur != lst.end(); cur++) cout << *cur;  // 비밀번호 출력
        cout << '\n';
    }

    return 0;
}