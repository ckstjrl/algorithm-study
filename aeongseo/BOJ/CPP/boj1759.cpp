/*** 1759. 암호 만들기 ***/
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

void backtrack(int idx, int cnt, int vowel, int consonant);	// idx: 현재 인덱스, cnt: 암호로 선택한 문자 개수, vowel: 암호의 모음 개수, consonant: 암호의 자음 개수

vector<char> characters;
vector<char> pw;
char vowel_arr[5] = { 'a', 'e', 'i', 'o', 'u' };	// 모음 배열
int L, C;

int main() {
	cin >> L >> C;

	characters.resize(C);
	for (int i = 0; i < C; i++) {
		cin >> characters[i];
	}
	sort(characters.begin(), characters.end());	// 문자 오름차순으로 정렬
	
	backtrack(0, 0, 0, 0);

	return 0;
}

void backtrack(int idx, int cnt, int vowel, int consonant) {
	if (cnt == L) {	// L개를 조합했을 때
		if (vowel >= 1 && consonant >= 2) {	// 모음 1개 이상, 자음 2개 이상이면 출력
			for (int i = 0; i < L; i++) {
				cout << pw[i];
			}
			cout << '\n';
		}
		return;
	}

	if (idx == C) return;	// C번 문자까지 다 돌면 반환
	
	pw.push_back(characters[idx]);	// pw에 문자 저장
	bool flag = false;	// 모음 판단을 위한 플래그
	for (int j = 0; j < 5; j++) {
		if (characters[idx] == vowel_arr[j]) {	// 현재 문자가 모음 리스트에 있으면 플래그 true
			flag = true;
		}
	}
	if (flag) backtrack(idx + 1, cnt + 1, vowel + 1, consonant); // 플래그가 true면 모음개수 증가하고 재귀 진행
	else backtrack(idx + 1, cnt + 1, vowel, consonant + 1);	// false면 자음개수 증가하고 재귀 진행
	pw.pop_back();	// pw에 문자 제거
	backtrack(idx + 1, cnt, vowel, consonant);	// 현재 문자를 선택하지 않고 재귀 진행
}