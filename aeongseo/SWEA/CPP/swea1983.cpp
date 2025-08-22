/*** 1983. 조교의 성적 매기기 (D2) ***/

#include<iostream>
#include<vector>
#include<algorithm>
#include<functional>
#include<string>
using namespace std;

int main() {
	int T;
	cin >> T;

	for (int tc = 1; tc < T + 1; ++tc) {
		int N, K, rank;
		double m, f, h;
		cin >> N >> K;

		vector<string> grade = { "A+","A0", "A-", "B +", "B0", "B-", "C+", "C0", "C-", "D0"}; // 학점

		vector<double> total_score(N, 0);
		vector<double> sorted_score(N, 0);

		for (int i = 0; i < N; i++) {
			cin >> m >> f >> h;
			total_score[i] = 0.35 * m + 0.45 * f + 0.2 * h;
			sorted_score[i] = 0.35 * m + 0.45 * f + 0.2 * h;
		}

		sort(sorted_score.begin(), sorted_score.end(), greater<>()); // 점수 내림차순 정렬

		for (int j = 0; j < N; j++) {
			if (total_score[K - 1] == sorted_score[j]) {
				rank = int(j / (N / 10));					// 각 학점별 받을 수 있는 학생 수로 나눔
				cout << '#' << tc << ' ' << grade[rank] << '\n';
			}
		}

	}

	return 0;
}