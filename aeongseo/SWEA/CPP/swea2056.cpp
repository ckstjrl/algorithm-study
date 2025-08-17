/*** 2056. 연월일 달력 (D1) ***/
/*
연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
해달 날짜의 유호ㅛ성을 판단한 후, 날짜가 유효하다면 "YYYY/MM/DD"형식으로 출력하고, 날짜가 유효하지 않을 경우, -1을 출력하는 프로그램을 작성하라.
*/

#include<iostream>
#include<string>
using namespace std;

int main(){
    int T;
    cin >> T;

    for (int tc=1; tc<T+1; ++tc){
        string date;
        cin >> date;

        // substr() 함수 : 문자열의 특정 부분 잘라냄. s.substr(시작위치, 길이)
        string s_year = date.substr(0, 4);
        string s_month = date.substr(4, 2);
        string s_day = date.substr(6);

        int result;
        // stoi() 함수 : sring 입력받고, 출력으로 integer 반환
        int month = stoi(s_month);
        int day = stoi(s_day);

        // 31일까지인 달 : 1, 3, 5, 7, 8, 10, 12
        if ((month==1 || month==3 || month==5 || month==7 || month==8 || month==10 || month==12) && (day>=1 && day<=31)){
            cout << '#' << tc << ' ' << s_year << '/' << s_month << '/' << s_day << '\n';
        }
        // 30일까지인 달 : 4, 6, 9, 11
        else if ((month==4 || month==6 || month==9 || month==11) && (day>=1 && day<=30)) {
            cout << '#' << tc << ' ' << s_year << '/' << s_month << '/' << s_day << '\n';
        }

        // 28일까지인 달 : 2
        else if ((month == 2) && (day>=1 && day<=28)) {
            cout << '#' << tc << ' ' << s_year << '/' << s_month << '/' << s_day << '\n';
        }
        
        else {
            cout << '#' << tc << ' ' << -1 << '\n';
        }
        
    }

    return 0;
}