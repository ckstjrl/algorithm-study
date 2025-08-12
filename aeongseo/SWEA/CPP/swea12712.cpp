/*** 12712. 파리퇴치3 ***/

#include<iostream>
using namespace std;

int main(){
    int T;
    cin >> T;

    for(int tc=1; tc<T+1; ++tc){
        int N, M;
        cin >> N >> M;
        
        int arr[N][N];
        for(int i=0; i<N; i++){     // 입력된 배열
            for(int j=0; j<N; j++){
                cin >> arr[i][j];
            }
        }
        

        int max_fly = 0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                int ni, nj;
                // +자
                int result_cross = arr[i][j];
                int dr_cross[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};   // 십자로 이동할 때 각 방향
                for(int k=0; k<4; k++){                             // dr_cross 제어 위한 for문
                    for(int d=1; d<M; d++){
                        ni = i + dr_cross[k][0] * d;
                        nj = j + dr_cross[k][1] * d;

                        if(ni >= 0 && ni < N && nj >= 0 && nj < N){
                            result_cross += arr[ni][nj];
                        }
                    }
                }
                
                if(max_fly < result_cross){
                    max_fly = result_cross;
                }
                
                // x자
                int result_diagonal = arr[i][j];
                int dr_diagonal[4][2] = {{1, 1}, {1, -1}, {-1, -1}, {-1, 1}};   // 대각선으로 이동할 때 각 방향
                for(int k=0; k<4; k++){
                    for(int d=1; d<M; d++){
                        ni = i + dr_diagonal[k][0] * d;
                        nj = j + dr_diagonal[k][1] * d;
                        
                        if(ni >= 0 && ni < N && nj >= 0 && nj < N){
                            result_diagonal += arr[ni][nj];
                        }
                        
                    }
                }

                if(max_fly < result_diagonal){
                    max_fly = result_diagonal;
                }

            }
        }

        cout << '#' << tc << ' ' << max_fly << '\n';

    }

    return 0;
}