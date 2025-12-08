/*
BOJ1107 - 리모컨

문제 정의
1. 0-9 까지 숫자, + 와 - 존재
2. +를 누르면 현재 채널 +1, -는 -1
3. 채널 0에서 -는 없고 채널은 양의 무한대
4. 시작 채널은 100번
5. 만약 고장난 버튼이 있다면, M개의 줄에 걸쳐 주어진다..

로직 생각
1. 주어진 N번 채널에 가장 가깝게 수를 만들고 거기서 값을 구하는 방식
2. 키를 여러번 누를 수 있다는 점을 생각, 100번이 시작이므로 100, 만들 수 있는 값 이 후보군
3. 문자열을 이어붙이면서 만들 수 있는 모든 경우의 수를 만들어 int 형으로 변환
4. 변환 후에 N과 차이를 절대값으로 얼마나 차이 나는지 확인, 차이가 가장 적은 애를 저장
5. 100이랑 차이가 얼마나 나는지를 확인
6. 두 경우 중 가장 적은 횟수를 반환

두 번째 로직 생각
1. 주어진 N번 채널에 가장 가깝게 수를 만들고 거기서 값을 구하는 방식
2. 키를 여러번 누를 수 있다는 점을 생각, 100번이 시작이므로 100, 만들 수 있는 값 이 후보군
3. 모든 경우의 채널을 돌면서 가능하면 cont 아니면 break
*/

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int n, m, min_ans;
bool nums[10];
bool cands[1000001];

int up_num = 1000001;
int down_num = 1000001;
int close_num = 1000001;


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m;
    for (int i = 0; i < m; i++){
        int temp;
        cin >> temp;
        nums[temp] = true;
    }
    
    
    // 100에서 움직이는 수로 최소값 초기화
    min_ans = abs(100-n);
    for (int i = n; i < 1000001; i++){
        string s = to_string(i);
        bool flag = false;
        for (int j = 0; j < s.size(); j++){
            if (nums[s[j] - '0']){
                flag = true;
                break;
            }
        }
        if (!flag){
            up_num = i;
            break;
        }
    }

    for (int i = n; i > -1; i--){
        string s = to_string(i);
        bool flag = false;
        for (int j = 0; j < s.size(); j++){
            if (nums[s[j] - '0']){
                flag = true;
                break;
            }
        }
        if (!flag){
            down_num = i;
            break;
        }
    }

    if (abs(up_num - n) + to_string(up_num).length() >= abs(down_num - n)+ to_string(down_num).length()){
        close_num = down_num;
    }
    else{
        close_num = up_num;
    }
    int temp_ans = abs(close_num-n)+ to_string(close_num).length();
    min_ans = min(temp_ans, min_ans);

    cout << min_ans;
    return 0;
}