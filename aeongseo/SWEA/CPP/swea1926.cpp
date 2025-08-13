/*** 1926. 간단한 369게임 ***/

#include<iostream>
using namespace std;

int main(){
    int N;
    cin >> N;

    for(int i=1; i<N+1; i++){
        int cnt = 0;
        int first = i % 10;             // 일의 자릿수 저장
        int second = (i/10) % 10;       // 십의 자릿수 저장
        int third = ((i/10)/10) %10;    // 백의 자릿수 저장. 10<=N<=1000이므로 백의 자리 까지.

        if(first == 3 || first == 6 || first == 9){     // 일의 자릿수가 3, 6, 9일 때
            cnt++;                                      // cnt 증가
        }
        if(second == 3 || second == 6 || second == 9){  // 십의 자릿수가 3, 6, 9일 때
            cnt++;                                      // cnt 증가
        }
        if(third == 3 || third == 6 || third == 9){     // 백의 자릿수가 3, 6, 9일 때
            cnt++;                                      // cnt 증가
        }
        
        if(cnt == 0){                                   // 자릿수에 3, 6, 9가 없다면
            cout << i;                                  // 숫자 출력
        }
        else{ 
            for(int j=0; j<cnt; j++){                   // 자릿수에 3, 6, 9 있다면 cnt 만큼 - 출력
                cout << '-';
            }
        }
        cout << ' ';

    }

    return 0;
}