/*** 5052. 전화번호 목록 ***/

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc < T + 1; ++tc) {

		int n;
		string ans = "YES";	// 초기값 yes
		cin >> n;
		vector<string> phonenumber(n);
		for (int i = 0; i < n; i++) {
			cin >> phonenumber[i];	// 전화번호를 문자열로 입력받고 배열에 저장
		}

		sort(phonenumber.begin(), phonenumber.end());	// 오름차순 정렬


		for (int i = 0; i < n-1; i++) {
			int l = min(phonenumber[i].size(), phonenumber[i + 1].size());	// 인접한 전화번호 중 짧은 길이 저장
			int cnt = 0;
			for (int j = 0; j < l; j++) {
				if (phonenumber[i][j] == phonenumber[i + 1][j]) {	// 문자열의 앞에 겹치는 숫자가 있으면 카운트 증가
					cnt++;
					if (cnt == l) ans = "NO"; // 카운트가 짧은 전화번호 길이와 같으면 인접한 번호의 접두어에 위치하므로 no로 변경
				}
			}
		}

		cout << ans << '\n';
	}

	return 0;
}