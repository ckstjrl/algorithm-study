/*** 2001. 파리 퇴치 ***/

#include<iostream>
using namespace std;

int main(){
    int T, M, N;

    cin >> T;

    for(int tc=1; tc<T+1; ++tc){
        cin >> N >> M;

        int arr[N][N];
        int sum = 0;
        int max = 0;

        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cin >> arr[i][j];
            }
        }

        for(int i=0; i<N-M+1; i++){                 // 파리채가 움직일 수 있는 범위
            for(int j=0; j<N-M+1; j++){
                for(int col=i; col<i+M; col++){     // 파리채의 크기 범위. 처음에 범위를 M+1, -> M 했다가 sum을 매번 출력했더니 2에서 끝나는 것을 보고 i+M으로 바꿈
                    for(int row=j; row<j+M; row++){
                        sum += arr[col][row];
                    }
                }
                
                if(max < sum){
                    max = sum;
                }
                sum = 0;    // 처음에 sum 초기화 안했었음. 그래서 max가 엄청 큰 수 나옴.
            }
        }

        cout << '#' << tc << ' ' << max << '\n';

    }

    return 0;
}
