/*** 2070. 큰 놈, 작은 놈, 같은 놈 ***/

#include<iostream>
using namespace std;

int main(){
    int T, a, b;
    char oper;

    cin >> T;
    
    for(int tc=1; tc < T+1; ++tc){
        cin >> a >> b;
    
        if(a > b){
            oper = '>';             // a가 b보다 크면 oper에 > 저장.
        }
        else if(a == b){            // a와 b가 같으면 oper에 = 저장.
            oper = '=';
        }
        else{                       // a가 b보다 작으면 oper에 < 저장.
            oper = '<';
        }

        cout << '#' << tc << ' ' << oper << '\n';
    }

    return 0;
}