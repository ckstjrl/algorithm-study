#include <iostream>
using namespace std;

int main(){
    int test_case;
    int T;

    cin>>T;

    for(test_case=1;test_case<=T; ++test_case){
        int arr[10];
        int sum = 0;
    
        for(int i =0; i<10; i++){
            cin>>arr[i];
        }
    
        for(int j=0; j<10; j++){
            if(arr[j] % 2 != 0){                        // 값이 홀수면
                sum += arr[j];                          // sum에 더하기
            }
        }
    
        cout<<"#" << test_case << " " << sum << "\n";

    }
    return 0;

}