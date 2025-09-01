#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        string p, s;        // 수행할 함수 p를 문자열로 받음.
        int n;
        cin >> p >> n >> s;
        
        vector<int> arr;
        string temp = "";   // 문자열 s에서 숫자를 파싱해서 arr 가변배열에 넣어줌.
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '[') {
                continue;
            } else if (s[i] == ',' || s[i] == ']') {
                if (!temp.empty()) {
                    arr.push_back(stoi(temp));
                    temp = "";
                }
            } else {
                temp += s[i];
            }
        }

        bool error_flag = false, reverse_flag = false;  // error 와 reverse 체크를 위한 flag
        for (int i = 0; i < p.size(); i++) {
            if (p[i] == 'R') {
                reverse_flag = !reverse_flag;           // 토글처럼 true/false
            } else if (p[i] == 'D') {
                if (arr.empty()) {
                    error_flag = true;
                    break;
                }
                if (reverse_flag) arr.pop_back();       // reverse면 뒤에서 값을 제거
                else arr.erase(arr.begin());            // !reverse면 앞에서 값을 제거 
            }
        }
        if (error_flag) {
            cout << "error\n";
        } else {
            cout << "[";
            if (!reverse_flag) {    // !reverse면 앞에서부터 출력
                for (int i = 0; i < arr.size(); i++) {
                    cout << arr[i];
                    if (i != arr.size() - 1) cout << ",";
                }
            } else {                // reverse면 뒤에서부터 출력
                for (int i = arr.size() - 1; i >= 0; i--) {
                    cout << arr[i];
                    if (i != 0) cout << ",";
                }
            }
            cout << "]\n";
        }
    }

    return 0;
}