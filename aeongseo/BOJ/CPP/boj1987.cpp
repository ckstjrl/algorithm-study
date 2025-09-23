/*** 1987. 알파벳 ***/

#include<iostream>
#include<vector>
#include<string>
#include<set>
#include<algorithm>
using namespace std;

void backtrack(int si, int sj, int cnt);

vector<vector<char>> arr;
bool alphabet[26] = { false };
int di[4] = { 0, 1, 0, -1 };
int dj[4] = { 1, 0, -1, 0 };
int R, C;
int max_cnt = 0;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	cin >> R >> C;

	arr.assign(R, vector<char>(C));

	for (int i = 0; i < R; i++) {
		string line;
		cin >> line;
		for (int j = 0; j < C; j++) {
			arr[i][j] = line[j];
		}
	}
	// 공백이 없으므로 한줄 입력 받고 각 배열 요소에 집어넣는다.

	alphabet[arr[0][0] - 'A'] = true;
	backtrack(0, 0, 1); // 시작지점부터 카운트하기 때문에 1부터 시작

	cout << max_cnt;
	return 0;
}

void backtrack(int si, int sj, int cnt) {
	max_cnt = max(max_cnt, cnt);

	for (int i = 0; i < 4; i++) {
		int ni = si + di[i];
		int nj = sj + dj[i];

		if (ni < 0 || ni >= R || nj < 0 || nj >= C) {
			continue;
		}
		if (alphabet[arr[ni][nj]-'A']) {
			continue;
		}

		alphabet[arr[ni][nj]-'A'] = true;
		backtrack(ni, nj, cnt + 1);
		alphabet[arr[ni][nj] - 'A'] = false;
	}

}