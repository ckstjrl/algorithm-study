#include <iostream>
#include <string>
#include <list>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 속도 최적화
    cin.tie(NULL);

    int m;
    string s;  // 초기에 입력되어 있는 문자열
    cin >> s;

    list<char> lst(s.begin(), s.end());  // list 자료구조 사용

    auto cur = lst.end();  // iterator 사용해서 cursor 선언

    cin >> m;
    char cmd, c;
    while (m--) {
        cin >> cmd;

        if (cmd == 'L') {
            if (cur != lst.begin()) cur--;  // cursor가 문장의 맨 앞이 아니라면 cursor 1 감소
        } else if (cmd == 'D') {
            if (cur != lst.end()) cur++;    // cursor가 문장의 맨 뒤가 아니라면 cursor 1 증가
        } else if (cmd == 'B') {
            if (cur != lst.begin()) {       // cursor가 문장의 맨 앞이 아니라면 왼쪽에 있는 문자 삭제
                cur--;
                cur = lst.erase(cur);
            } 
        } else if (cmd == 'P') {            // 커서 왼쪽에 입력받은 문자 c 추가
            cin >> c;
            lst.insert(cur, c);
        }
    }

    for (auto cur = lst.begin(); cur != lst.end(); cur++) cout << *cur;  // 결과 출력
    cout << '\n';

    return 0;
}