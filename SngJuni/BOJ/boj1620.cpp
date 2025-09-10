#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);  // 입출력 최적화 코드
    cin.tie(NULL);

    int n, m;
    cin >> n >> m;

    vector<string> arr;             // 포켓몬 이름을 문자열로 저장하기 위한 가변배열
    unordered_map<string, int> um;  // 포켓몬 이름을 키로 갖고 번호를 값으로 갖는 unorderd_map

    string s;
    for (int i = 0; i < n; i++) {  // 포켓몬 이름 입력 받으며 vector와 unordered_map에 저장
        cin >> s;
        arr.push_back(s);
        um[s] = i + 1;
    }
    for (int i = 0; i < m; i++) {   
        cin >> s;
        if (isdigit(s[0])) {                   // 입력으로 숫자가 들어오면 가변배열에서 포켓몬의 이름을 출력
            cout << arr[stoi(s) - 1] << '\n';
        } else {                               // 입력으로 문자가 들어오면 unordered_map에서 포켓몬의 번호를 출력
            cout << um[s] << '\n';
        }
    }

    return 0;
}