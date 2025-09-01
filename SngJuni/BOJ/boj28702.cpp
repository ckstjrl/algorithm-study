#include <iostream>
#include <string>

using namespace std;

int main() {
    int pos = 0, num = 0;

    string s;
    for (int i = 0; i < 3; i++) {
        cin >> s;  // 문자열로 입력받음

        if (s == "Fizz" || s == "Buzz" || s == "FizzBuzz") continue;
        else {     // 3개의 입력 중 하나는 반드시 숫자가 들어오기 때문에 이를 문자열에서 int 형으로 변환
            pos = i;
            num = stoi(s);
        }
    }

    num += (3 - pos);  // 다음 올 문자열에 해당하는 숫자
    if (!(num % 3) && !(num % 5)) cout << "FizzBuzz\n";
    else if (!(num % 3)) cout << "Fizz\n";
    else if (!(num % 5)) cout << "Buzz\n";
    else cout << num << '\n';

    return 0;
}