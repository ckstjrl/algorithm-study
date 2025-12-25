/*** 1756. 피자 굽기 ***/

/*
	깊이별 오븐의 지름을 최소 지름으로 저장한다. -> 지름 내림차순
	깊은 곳에서부터 오븐 입구쪽으로 순회
	반죽 지름이 오븐 지름보다 크면 continue
	반죽 지름이 오븐 지름과 같거나 작으면 그 위의 위치를 저장
	위치가 오븐을 벗어나면(pos=0) 더이상 반죽이 들어가지 못하므로 break
	들어간 반죽의 개수가 N개와 같다면 위치를 출력, 아니라면 0 출력
	마지막으로 저장된 위치는 마지막 반죽의 바로 위이므로, 출력할 때는 +1
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int N, D, cnt = 0;
	cin >> D >> N;

	vector<int> oven(D + 1, 0);
	vector<int> minOven(D + 1, 0);
	vector<int> dough(N + 1, 0);
	vector<bool> isPizza(D + 1, false);
	int pos = D;

	for (int i = 1; i <= D; i++) {
		cin >> oven[i];
	}
	for (int i = 1; i <= N; i++) {
		cin >> dough[i];
	}

	minOven[1] = oven[1];
	for (int i = 2; i <= D; i++) {
		minOven[i] = min(minOven[i - 1], oven[i]);
	}

	for (int i = 1; i <= N; i++) {
		if (pos == 0) break;
		for (int j = pos; j > 0; j--) {
			if (dough[i] > minOven[j]) continue;
			pos = j - 1;
			cnt++;
			break;
		}
	}

	if (cnt != N) cout << 0;
	else cout << pos + 1;

	return 0;
}