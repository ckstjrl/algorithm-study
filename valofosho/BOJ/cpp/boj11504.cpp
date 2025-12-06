/*
BOJ11504 - 가장 긴 바이토닉 부분 수열

문제 정의
수열 S가 주어질 때, S1 < S2 < ... <Sk > Sk+1 > ... 이 성립해야 함
즉 기준 값이 되는 최대값 Sk 를 기준으로 좌측은 증가, 우측은 감소하는 형태
해당 수열에서 가장 긴 바이토닉 부분 수열의 최대 길이를 구하라

로직 정의
이런 문제는 보통 스택을 여러개 활용하는 경우가 많았던 점 고려,
수열의 길이가 N일 때 k는 S[k] 가정 시 1 <= k <= N-2가 가능(좌우에 하나씩 값이 존재해야 하니까)

첫 로직 생각
1. 그냥 브루트포스로 때려 박기
2. 임의의 K값을 기준으로 가장 긴 증가하는 부분 수열 + 가장 긴 감소하는 부분수열 을 구하고 중복 K 빼주기
    - 두 개의 배열을 선언하고, 각 DP 배열을 채워주기
    - 이전 값보다 다음 값이 크고, DP 배열에서도 +1  한 값보다 크다면 DP + 1 로 갱신
*/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int answer = 1;

vector<int> arr;
vector<int> dp_asc;
vector<int> dp_desc;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    arr.assign(n, 0);
    dp_asc.assign(n, 1);
    dp_desc.assign(n, 1);

    for (int i = 0; i < n; i++){
        cin >> arr[i];
    }
    // 가장 긴 증가하는 부분 수열
    for (int i = 0; i < n; i ++){
        for (int j = i+1; j < n; j++){
            if (arr[i] < arr[j]){
                if(dp_asc[j] < dp_asc[i] + 1){
                    dp_asc[j] = dp_asc[i] + 1;
                }
            }
        }
    }
    // 가장 긴 감소하는 부분 수열
    for (int i = n-1; i >= 0; i--){
        for (int j = i-1; j >= 0; j --){
            if (arr[i] < arr[j]){
                if (dp_desc[j] < dp_desc[i] + 1){
                    dp_desc[j] = dp_desc[i] + 1;
                }
            }
        }
    }
    for (int i = 0; i < n; i++){
        answer = max(answer, dp_asc[i] + dp_desc[i] - 1);
    }
    
    cout << answer;
    return 0;
}

/* 첫 풀이
- 운 좋게 UB를 피해간 케이스
- 1001로 배열을 선언하고 초기값을 주어서 desc 배열 과정에서 UB를 피해갈 수 있었다

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
int answer = 1;

int dp_asc[1001];
int dp_desc[1001];

vector<int> arr;

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    arr.assign(n, 0);

    for (int i = 0; i < n; i++){
        cin >> arr[i];
        dp_asc[i] = 1;
        dp_desc[i] = 1;
    }
    // 가장 긴 증가하는 부분 수열
    for (int i = 0; i < n; i ++){
        for (int j = i+1; j < n; j++){
            if (arr[i] < arr[j]){
                if(dp_asc[j] < dp_asc[i] + 1){
                    dp_asc[j] = dp_asc[i] + 1;
                }
            }
        }
    }
    // 가장 긴 감소하는 부분 수열
    for (int i = n; i >= 0; i--){
        for (int j = i-1; j >= 0; j --){
            if (arr[i] < arr[j]){
                if (dp_desc[j] < dp_desc[i] + 1){
                    dp_desc[j] = dp_desc[i] + 1;
                }
            }
        }
    }
    for (int i = 0; i < n; i++){
        answer = max(answer, dp_asc[i] + dp_desc[i] - 1);
    }
    
    cout << answer;
    return 0;
}
*/