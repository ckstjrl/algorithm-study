/* boj1924 - 2007년

오늘은 2007년 1월 1일 월요일이다. 
그렇다면 2007년 x월 y일은 무슨 요일일까? 
이를 알아내는 프로그램을 작성하시오.

첫째 줄에 빈 칸을 사이에 두고 x(1 ≤ x ≤ 12)와 y(1 ≤ y ≤ 31)이 주어진다. 
참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.
*/
// 7로 나눠서 1이면 월요일 2면 화... 0이면 일요일
// x월 -> 31일로 치환

#include <iostream>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int x, y;
    cin >> x >> y;

    int month[13] = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
    string day[7] = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};

    int days = 0;

    for (int i = 1; i < x; i++) {
        days += month[i];
    }

    days += y;

    string ans;
    ans = day[days % 7];
    cout << ans;

    return 0;
}