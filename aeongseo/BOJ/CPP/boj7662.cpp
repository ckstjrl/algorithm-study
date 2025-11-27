/*** 7662. 이중 우선순위 큐 ***/

#include<iostream>
#include<set>
using namespace std;

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc < T + 1; tc++) {
		multiset<int> ms;	// 중복 가능한 set
		int k;
		cin >> k;
		for (int i = 0; i < k; i++) {
			char order;
			int n;
			cin >> order >> n;
			if (order == 'I') {	// I면 삽입
				ms.insert(n);
			}
			else {	// D면
				if (ms.empty()) continue;	// set이 비었으면 실행 X
				if (n == 1) ms.erase(prev(ms.end()));	// 1이면 최대값 제거
				else ms.erase(ms.begin());	// -1이면 최소값 제거
			}
		}

		if (ms.empty()) cout << "EMPTY" << '\n';	// set이 비었으면 EMPTY 출력
		else cout << *prev(ms.end()) << ' ' << *ms.begin() << '\n';	// 아니면 최대값과 최소값 출력
	}

	return 0;
}