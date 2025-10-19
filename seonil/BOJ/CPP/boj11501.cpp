/*
BOJ11501. 주식

[문제]
홍준이는 요즘 주식에 빠져있다. 그는 미래를 내다보는 눈이 뛰어나, 날 별로 주가를 예상하고 언제나 그게 맞아떨어진다.
매일 그는 아래 세 가지 중 한 행동을 한다.

1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.

홍준이는 미래를 예상하는 뛰어난 안목을 가졌지만, 어떻게 해야 자신이 최대 이익을 얻을 수 있는지 모른다. 따라서 당신에게 날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산을 해달라고 부탁했다.
예를 들어 날 수가 3일이고 날 별로 주가가 10, 7, 6일 때, 주가가 계속 감소하므로 최대 이익은 0이 된다.
그러나 만약 날 별로 주가가 3, 5, 9일 때는 처음 두 날에 주식을 하나씩 사고, 마지막날 다 팔아 버리면 이익이 10이 된다.

[입력]
입력의 첫 줄에는 테스트케이스 수를 나타내는 자연수 T가 주어진다.
각 테스트케이스 별로 첫 줄에는 날의 수를 나타내는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
둘째 줄에는 날 별 주가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다. 날 별 주가는 10,000이하다.

[출력]
각 테스트케이스 별로 최대 이익을 나타내는 정수 하나를 출력한다. 답은 부호있는 64bit 정수형으로 표현 가능하다.
*/

#include <iostream>
#include <vector>
using namespace std;

long long calculateMaxProfit(const vector<int>& prices, int n) {
    long long profit = 0;
    int maxPrice = 0;

    for (int i = n - 1; i >= 0; i--) {    // 뒤에서부터 앞으로 탐색(미래의 최고 주가 기준으로 이익 계산)
        if (prices[i] > maxPrice) {   // 현재 주가가 지금까지 본 최고가보다 크면,
            maxPrice = prices[i];   // 새로운 최고가 갱신
        } else {    // 현재 주가가 최고가보다 낮으면,
            profit += (maxPrice - prices[i]);   // 오늘 사서 나중에 최고가에 판다고 가정하고 이익 계산
        }
    }
    return profit;    // 모든 날 확인 후 계산된 총 이익 반환
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;   // 테스트 케이스 수 T 입력 받기

    for (int tc = 1; tc < T + 1; tc++) {
        int N;
        cin >> N;   // 날의 수 N 입력 받기

        vector<int> stockPrices(N);
        for (int i = 0; i < N; ++i) {
            cin >> stockPrices[i];    // 각 날의 주가 입력 받기
        }

        long long answer = calculateMaxProfit(stockPrices, N);    // 최대 이익 계산
        cout << answer << '\n';   // 최대 이익 출력
    }

    return 0;
}
