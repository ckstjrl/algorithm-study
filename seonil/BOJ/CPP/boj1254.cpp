/*
BOJ1254. 팰린드롬 만들기

[문제]
동호와 규완이는 212호에서 문자열에 대해 공부하고 있다. 규완이는 팰린드롬을 엄청나게 좋아한다. 팰린드롬이란 앞에서부터 읽으나 뒤에서부터 읽으나 같게 읽히는 문자열을 말한다.
동호는 규완이를 위한 깜짝 선물을 준비했다. 동호는 규완이가 적어놓고 간 문자열 S에 0개 이상의 문자를 문자열 뒤에 추가해서 팰린드롬을 만들려고 한다. 동호는 가능하면 가장 짧은 문자열을 만들려고 한다.
동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력하는 프로그램을 작성하시오.

[입력]
첫째 줄에 문자열 S가 주어진다. S는 알파벳 소문자로만 이루어져 있고, 길이는 최대 50이다.

[출력]
첫째 줄에 동호가 만들 수 있는 가장 짧은 팰린드롬의 길이를 출력한다.
*/

#include <iostream>
#include <algorithm>
using namespace std;

// 팰린드롬이면 True, 아니라면 False를 반환하는 함수
bool is_palindrome(const string& s) {
    // rev에 s를 저장하고 뒤집기
    string rev = s;
    reverse(rev.begin(), rev.end());
    return s == rev; // 뒤집은 문자열 rev가 s와 똑같으면 True, 다르다면 False 반환
}

int make_shortest_palindrome(string s) {
    int n = s.size(); // n: 문자열의 길이
    for (int i = 0; i < n; i++) {
        string prefix = s.substr(0, i); // prifix: 앞에서부터 i개의 문자
        // add에 prifix를 뒤집은 문자열을 뒤에 붙여서 후보 문자열 candidate를 만든다.
        string add = prefix;
        reverse(add.begin(), add.end());
        string candidate = s + add;

        if (is_palindrome(candidate)) // 후보 문자열 candidate가 팰린드롬이면,
        {
          return candidate.size();  // 후보 문자열의 길이를 반환하고 종료
        }
    }
    return 2 * n - 1; // 모든 candidate들이 팰린드롬이 아닌 경우 최악의 경우인 2 * n - 1을 반환하고 종료
}

int main() {
    // 입력 문자열 s 받기
    string s;
    cin >> s;
    // 팰린드롬이 되기 위한 최소 길이를 출력
    cout << make_shortest_palindrome(s) << endl;
}