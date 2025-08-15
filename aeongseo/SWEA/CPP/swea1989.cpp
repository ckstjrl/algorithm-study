/*** 1989. 초심자의 회문 검사 ***/

#include<iostream>
#include<string>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc < T + 1; ++tc) {
		string word;
		cin >> word;
		int l = word.length();
		for (int i = 0; i < l / 2; i++) {    // 단어 길이의 절반만큼 문자 하나씩  순회
			if (word[i] != word[l - 1 - i]) {    // 해당 문자와 반대편 문자가 일치하지 않으면
				cout << '#' << tc << ' ' << 0 << '\n';    // 0 출력
				break;
			}
			else if (i == l / 2 - 1 && word[i] == word[l - 1 - i]) { // 인덱스가 마지막이고 문자가 일치하면
				cout << '#' << tc << ' ' << 1 << '\n';    // 1 출력
			}
		}
	}
	return 0;
}