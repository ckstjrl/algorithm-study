/*** 9251. LCS ***/

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	string str1, str2;
	cin >> str1 >> str2;
	int l1 = str1.size();
	int l2 = str2.size();
	vector<vector<int>> dp(l1 + 1, vector<int>(l2 + 1, 0));	// LCS 길이 저장할 배열

	for (int i = 1; i < l1 + 1; i++) {
		for (int j = 1; j < l2 + 1; j++) {
			if (str1[i - 1] == str2[j - 1]) {	// str1의 문자와 str2의 문자가 같으면
				dp[i][j] = dp[i - 1][j - 1] + 1;	// 이전 LCS 길이에서 1 더함
			}
			else {	// 문자가 같지 않으면
				dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]);	// 이전 LCS 길이 중에서 최장 길이 저장
			}
		}
	}

	cout << dp[l1][l2];	// 모든 문자열에서의 LCS 출력

	return 0;
}