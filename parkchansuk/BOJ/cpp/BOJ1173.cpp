// BOJ 1173. 운동 / D1
/*
문제
영식이가 운동을 하는 과정은 1분 단위로 나누어져 있다. 매 분마다 영식이는 운동과 휴식 중 하나를 선택해야 한다.

운동을 선택한 경우, 영식이의 맥박이 T만큼 증가한다. 즉, 영식이의 맥박이 X였다면, 1분 동안 운동을 한 후 맥박이 X+T가 되는 것이다. 영식이는 맥박이 M을 넘는 것을 원하지 않기 때문에, X+T가 M보다 작거나 같을 때만 운동을 할 수 있다. 휴식을 선택하는 경우 맥박이 R만큼 감소한다. 즉, 영식이의 맥박이 X였다면, 1분 동안 휴식을 한 후 맥박은 X-R이 된다. 맥박은 절대로 m보다 낮아지면 안된다. 따라서, X-R이 m보다 작으면 맥박은 m이 된다.

영식이의 초기 맥박은 m이다. 운동을 N분 하려고 한다. 이때 운동을 N분하는데 필요한 시간의 최솟값을 구해보자. 운동하는 시간은 연속되지 않아도 된다.

입력
첫째 줄에 다섯 정수 N, m, M, T, R이 주어진다.

출력
첫째 줄에 운동을 N분하는데 필요한 시간의 최솟값을 출력한다.. 만약 운동을 N분 할 수 없다면 -1을 출력한다.
*/
#include <iostream>
#include <vector>
using namespace std;

int main() {
	int N, m, M, T, R;
	cin >> N >> m >> M >> T >> R;
	vector<int> bpm;
	bpm.emplace_back(m);
	int cnt = 0;
	int min = 0;
	while (cnt < N) {
		if (m + T > M) { 
			min = -1;
			break;
		}
		else if (bpm[min] + T <= M) {
			bpm.emplace_back(bpm[min] + T);
			cnt++;
		}
		else {
			if (bpm[min] - R >= m) {
				bpm.emplace_back(bpm[min] - R);
			}
			else {
				bpm.emplace_back(m);
			}
		}
		min++;
	}
	cout << min;
}

/*
vector에 맥박수를 저장하면서 진행 -> min을 인덱스로 활용
cnt는 운동 횟수 저장하고 min은 총 시간을 의미함
cnt가 N과 같아질 때까지 while문 반복
while문 안에서 초반 맥박수 + 운동하면 올라가는 맥박 수가 최대값보다 크다면 min애 -1을 넣고 반복문 종료
아닌 경우 맥박수가 최댓값을 넘어가지 않도록 조절하고
맥박수가 최솟값보다 작게 계산된다면 최솟값으로 최신화
이 과정을 통해 운동하는데 총 걸린 시간은 min으로 출력 가능
*/