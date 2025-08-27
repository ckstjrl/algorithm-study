#include <iostream>
#include <string>

using namespace std;

int main() {
    string s;
    cin >> s;  // 식을 문자열로 받음.

    bool flag = false;  // 첫번째 - 의 위치를 찾기 위한 플래그
    string num = "";    // +, -, \0 이 아닌 각 숫자의 값을 구하기 위한 임시 문자열
    int sum = 0;        // 식의 결과가 담길 변수
    for (int i = 0; i <= s.size(); i++) {
        if (s[i] == '+' || s[i] == '-' || s[i] == '\0') {  // 연산기호나 문자열의 끝이면 현재까지 저장한 num 문자열을 숫자로 바꿔서 식 계산
            if (flag) {  // 첫번째 - 가 나온 이후라면 해당 숫자를 합계에서 빼기 연산
                sum -= stoi(num);
                num = "";
            } else {     // 첫번째 - 가 나오지 않았다면 해당 숫자를 합계에 더하기 연산
                sum += stoi(num);
                num = "";
            }
        } else {  // 연산기호나 문자열의 끝이 아니라면 해당 숫자(문자)를 문자열에 더함.
            num += s[i];
        }

        if (s[i] == '-') flag = true;  // 첫번째 - 를 만나면 flag를 true로 전환해서 식의 값을 최소로 만들 수 있게 함.
    }
    cout << sum << '\n';

    return 0;
}