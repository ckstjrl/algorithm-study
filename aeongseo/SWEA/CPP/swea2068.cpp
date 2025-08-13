/*** 2068. 최대수 구하기 ***/

#include<iostream>
using namespace std;

int main(){
    int T;
    cin >> T;
    
    for(int tc=1; tc<T+1; ++tc){
        int max = 0;    // 각 테스트 케이스마다 max 초기화
        int n[11];      // 입력된 10개의 수 배열
        for(int i=0; i<10; i++){
            cin >> n[i];
            if(max < n[i]){ // 입력받은 수가 max보다 크면 max에 저장
                max = n[i];
            }
        }

        cout << '#' << tc << ' ' << max << '\n';
    }

    return 0;
}