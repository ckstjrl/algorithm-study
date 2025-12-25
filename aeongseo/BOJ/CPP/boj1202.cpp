/*** 1202. 보석 도둑 ***/

#include<iostream>
#include<vector>
#include<queue>
#include<algorithm>
using namespace std;

// 보석을 무게 오름차순으로 정렬
// 가방을 용량 오름차순으로 정렬
// 가격 기준 maxheap에 가능한 무게의 보석 다 저장
// 그중 가장 비싼 보석 선택해 가격에 더함

vector<pair<int, long long>> gemstones;
vector<int> bag;
priority_queue<long long> price;
long long s = 0;
int N, K;

int main() {
	cin >> N >> K;
	
	for (int i = 0; i < N; i++) {
		int M;
		long long V;
		cin >> M >> V;
		gemstones.push_back({ M, V });
	}

	for (int i = 0; i < K; i++) {
		int C;
		cin >> C;
		bag.push_back(C);
	}

	// 보석(무게), 가방 오름차순 정렬
	sort(gemstones.begin(), gemstones.end());
	sort(bag.begin(), bag.end());

	int idx = 0;	// 보석 인덱스
	for (int i = 0; i < K; i++) {	// 가방 인덱스
		while (idx < N && gemstones[idx].first <= bag[i]) {	// idx가 범위 내이고, 보석의 무게가 가방 최대용량 이하면
			price.push(gemstones[idx].second);	// 보석의 가격을 우선순위큐에 저장
			idx++;	// 보석 인덱스 추가
			// 보석 인덱스는 가방이 바뀌어도 초기화 X
			// 우선순위큐에 보석 정보가 남아있으므로 이전에 훑었던 보석들을 다시 볼 필요 없음
		}
		
		if (!price.empty()) {	// 우선순위큐가 비어있지 않으면 총합에 합산
			s += price.top();
			price.pop();
		}
	}

	cout << s;

	return 0;
}


	/*
	for (int i = 0; i < K; i++) {
		for (int j = 0; j < N; j++) {
			if (gemstones[j].first <= bag[i]) price.push(gemstones[j].second);
		}

		s += price.top();

	}
	*/
// maxheap 초기화 금지
// 우선순위큐 계속 재사용함