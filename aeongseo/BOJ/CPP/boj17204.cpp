/*** 17204. 죽음의 게임 ***/

// 배열의 인덱스에 외친 번호를 저장한다
// 0부터 번호를 외쳐 보성이 지목당하면 체크하고 탐색을 종료한다
// 보성이 지목당한 적이 있으면 카운트 된 수를, 지목당한 적이 없으면 -1을 출력한다

#include<iostream>
#include<vector>
using namespace std;

int main() {
	int N, K;
	bool flag = false;	// 보성이 지목됐는지 체크하기 위한 플래그
	cin >> N >> K;

	vector<int> people(N, 0);

	for (int i = 0; i < N; i++) {
		int a;
		cin >> a;
		people[i] = a;	// 지목한 사람 번호 저장
	}

	int num = 1, idx = 0;
	while (num <= N) {	
		if (people[idx] == K) {	// 지목당한 사람이 보성이면 체크하고 break
			flag = true;
			break;
		}
		idx = people[idx];	// 지목한 사람이 보성이 아니면 다음 사람으로 넘어감
		num++;	// 외친 번호 증가
	}

	if (!flag) cout << -1;	// 보성을 지목한 적 없으면 -1 출력
	else cout << num; // 보성을 지목한 적이 있으면 외친 번호 출력
	
	return 0;
}