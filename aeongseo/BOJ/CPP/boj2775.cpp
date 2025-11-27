/*** 2775. 부녀회장이 될테야 (D2) ***/

#include<iostream>
#include<vector>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int tc = 1; tc < T + 1; ++tc) {
		int k, n;
		cin >> k >> n;
		
		vector<vector<int>> arr(k+1, vector<int>(n+1, 0));	// 아파트

		for (int j = 1; j < n + 1; j++) {
			arr[0][j] = j;	// 0층 각 호수에 사는 사람 수
		}

		for (int i = 1; i < k + 1; i++) {	// k층
			for (int j = 1; j < n + 1; j++) {	// n호
				for (int l = 1; l < j + 1; l++) {	// 아래층 1호부터 j호까지 더함
					arr[i][j] += arr[i - 1][l];
				}
			}
		}
		cout << arr[k][n] << '\n';
	}

	return 0;
}