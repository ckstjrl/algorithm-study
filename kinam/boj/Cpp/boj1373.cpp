/* boj1373 - 2진수 8진수
2진수가 주어졌을 때, 8진수로 변환하는 프로그램을 작성하시오.
*/

// 8진수 : 0~7 은 2진수로 000 ~ 111 까지임
// 3자리씩 끊어서 8진수로 바꾸면? 될듯
// 8자리 받았다고 치면 맨앞은 2자리 먼저 처리하고 나머지 3자리씩 처리
// 8 // 3 하면 2 


#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    // C++에서 사용하는 입출력 속도 향상 코드라고 함
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    // 2진수를 문자열로 일단 받기
    string str;
    cin >> str;

    int len = str.length();

    if (len % 3 == 1) {
        // 맨 앞 1자리부터 처리해야함
        // '1' - '0' 은 아스키코드로 49 - 48이라 1이 나올 수 있음
        // 맨 앞자리는 미리 출력 
        cout << (str[0] - '0');

    }
    else if (len % 3 == 2) {
        // 맨 앞 2자리부터 처리
        // 앞 2자리가 11이면 1 * 2 + 1 * 1 해야함
        cout << ((str[0] - '0') * 2 + (str[1] - '0'));

    }
    // 선언부는 위에서 len % 3 으로 앞자리 1인경우 2인경우 미리 예외처리했으므로 len % 3 그대로
    // 조건부는 i가 2진수 기준 3자리씩 처리하므로 i가 3씩 올라 len 미만일때 만족하게 하면 됨
    for (int i = len % 3; i < len; i += 3) {
        int num = (str[i] - '0') * 4 + (str[i+1] - '0') * 2 + (str[i+2] - '0');
        cout << num;
    }
    
    return 0;
}