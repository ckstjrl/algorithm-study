/*
BOJ16401. 과자 나눠주기

[문제]
명절이 되면, 홍익이 집에는 조카들이 놀러 온다. 떼를 쓰는 조카들을 달래기 위해 홍익이는 막대 과자를 하나씩 나눠준다.
조카들이 과자를 먹는 동안은 떼를 쓰지 않기 때문에, 홍익이는 조카들에게 최대한 긴 과자를 나눠주려고 한다.
그런데 나눠준 과자의 길이가 하나라도 다르면 조카끼리 싸움이 일어난다. 따라서 반드시 모든 조카에게 같은 길이의 막대 과자를 나눠주어야 한다.
M명의 조카가 있고 N개의 과자가 있을 때, 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 구하라.
단, 막대 과자는 길이와 상관없이 여러 조각으로 나눠질 수 있지만, 과자를 하나로 합칠 수는 없다. 단, 막대 과자의 길이는 양의 정수여야 한다.

[입력]
첫째 줄에 조카의 수 M (1 ≤ M ≤ 1,000,000), 과자의 수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
둘째 줄에 과자 N개의 길이 L1, L2, ..., LN이 공백으로 구분되어 주어진다. 과자의 길이는 (1 ≤ L1, L2, ..., LN ≤ 1,000,000,000) 를 만족한다.

[출력]
첫째 줄에 조카 1명에게 줄 수 있는 막대 과자의 최대 길이를 출력한다.
단, 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없다면, 0을 출력한다.
*/

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// length 길이로 과자를 잘랐을 때 조카 몇 명에게 줄 수 있는지 계산하는 함수
long long countChildren(const vector<long long>& snacks, long long length) {
    long long count = 0;
    for (long long s : snacks) {  // 각각의 과자 길이에 대하여,
        count += s / length;  // 과자를 length로 나눈 몫을 구하여 count에 더함
    }
    return count; // length 길이의 과자 조각들이 총 몇 개 나오는지 반환
}

// 이분 탐색으로 가능한 최대 과자 길이 계산
long long findMaxSnackLength(const vector<long long>& snacks, int M) {
    long long left = 1;  // left = 1
    long long right = *max_element(snacks.begin(), snacks.end());  // right = snacks의 최댓값
    long long answer = 0;

    while (left <= right) {
        long long mid = (left + right) / 2;

        if (countChildren(snacks, mid) >= M) { // M개 이상의 같은 길이 과자 조각이 있으면
            answer = mid;       // 일단 저장
            left = mid + 1;     // 절반의 오른쪽 부분 확인하여 더 긴 길이를 시도
        }
        else  // M개 이상의 같은 길이 과자 조각이 없으면
        {
            right = mid - 1;    // 절반의 왼쪽 부분 확인하여 더 짧은 길이를 시도
        }
    }
    return answer; // 이분 탐색으로 구한 최대 과자 길이 반환
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int M, N;
    cin >> M >> N;  // M: 조카 수, N: 과자 수 입력 받기

    vector<long long> snacks(N);
    for (int i = 0; i < N; i++) cin >> snacks[i];  // 과자 N개의 길이 입력 받기

    long long result = findMaxSnackLength(snacks, M);  // 막대 과자의 최대 길이를 찾아 result에 저장
    cout << result << '\n'; // 결과 출력

    return 0;
}
