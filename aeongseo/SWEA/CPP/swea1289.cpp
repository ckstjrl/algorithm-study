/*** 1289. 원재의 메모리 복구하기 ***/

#include<iostream>
#include<vector>
#include<string>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int tc=1; tc<T+1; ++tc){
        string n;      // 숫자로 받으려고 해서 계속 오버플로우가 났다.
        cin >> n;
        int len = n.length();           //입력 받은 메모리 값 길이
        int cnt = 0;                    // 수정 횟수
        vector<int> origin (len, 0);    // 원래 메모리 배열
        for(int i=0; i<len; i++){
            origin[i] = n[i] - '0';
        }
        
        vector<int> memory (len, 0);    // 초기화된 메모리 배열
        
        for(int j=0; j<len; j++){
            if(memory[j] != origin[j]){     //특정 자리의 원래 값과 초기화된 값이 다르면 원래값으로 끝까지 덮어씀.
                for(int k=j; k<len; k++){
                    memory[k] = origin[j];
                }
                cnt++;                      // 수정횟수 증가
            }
        }

        cout << '#' << tc << ' ' << cnt << '\n';
    }

    return 0;
}