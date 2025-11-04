/*** 26069. 붙임성 좋은 총총이 ***/

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

vector<string> people;
vector<int> meet;

// 총총을 만난 첫 감염자 1 로 표시
// 이후 1로 표시된 사람 만난 사람은 1로 표시
// 마지막에 1의 개수 세기

int main() {
	int N;
	cin >> N;
	
	for (int i = 0; i < N; i++) {
		string pers1, pers2;
		cin >> pers1 >> pers2;
		// people 목록에 없으면 추가
		if (find(people.begin(), people.end(), pers1) == people.end()) {
			people.push_back(pers1);
			meet.push_back(0);
		}
		int pers1_idx = find(people.begin(), people.end(), pers1) - people.begin(); // 해당 인물의 인덱스 저장

		if(find(people.begin(), people.end(), pers2) == people.end()) {
			people.push_back(pers2);
			meet.push_back(0);
		}
		int pers2_idx = find(people.begin(), people.end(), pers2) - people.begin();

		// 둘 중 하나가 총총이거나 총총이를 만난 적이 있다면 만남 표시
		if ((pers1 == "ChongChong" || pers2 == "ChongChong") ||(meet[pers1_idx] == 1 || meet[pers2_idx] == 1)) {
			meet[pers1_idx] = 1;
			meet[pers2_idx] = 1;
		}
	}

	//만남 표시 카운트
	cout << count(meet.begin(), meet.end(), 1);

	return 0;
}