/*** 1974. 스도쿠 검증 (D2) ***/
/*
스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1부터 9까지의 숫자를 채워넣는 퍼즐이다.
같은 줄에 1에서 9까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1에서 9까지의 숫자가 겹치지 않아야 한다.
입력으로 9 x 9 크기의 스도쿠 퍼즐의 숫자들이 주어졌을 때, 위와 같이 겹치는 숫자가 없을 경우, 1을 정답으로 출력하고 그렇지 않을 경우 0을 출력한다.
*/

#include<iostream>
using namespace std;

int sudoku_col(int arr[9][9]);
int sudoku_row(int arr[9][9]);
int sudoku_box(int arr[9][9]);


int main(){
    int T;
    cin >> T;

    for(int tc=1; tc<T+1; ++tc){
        int arr[9][9];

        for(int i=0; i<9; i++){
            for(int j=0; j<9; j++){
                cin >> arr[i][j];
            }
        }
        
        int col = sudoku_col(arr);
        int row = sudoku_row(arr);
        int box = sudoku_box(arr);

        if(col==1 && row==1 && box==1){
            cout << '#' << tc << ' ' << 1 << '\n';
        }
        else cout << '#' << tc << ' ' << 0 << '\n';
    }
    

    return 0;
}

int sudoku_col(int arr[9][9]){
    // 행 우선순회
    for(int i=0; i<9; i++){
        int cnt[9] = {0,};
        for(int j=0; j<9; j++){
            cnt[arr[i][j]-1]++;
        }
        if(cnt[0]==cnt[1]==cnt[2]==cnt[3]==cnt[4]==cnt[5]==cnt[6]==cnt[7]==cnt[8]){
            continue;
        }
        else return 0;
    }
    return 1;
}

int sudoku_row(int arr[9][9]){
    // 열 우선순회
    for(int j=0; j<9; j++){
        int cnt[9] = {0,};
        for(int i=0; i<9; i++){
            cnt[arr[i][j]-1]++;
        }
        if(cnt[0]==cnt[1]==cnt[2]==cnt[3]==cnt[4]==cnt[5]==cnt[6]==cnt[7]==cnt[8]){
            continue;
        }
        else return 0;
    }
    return 1;
}

int sudoku_box(int arr[9][9]){
    // 3x3 순회
    for(int i=0; i<9; i+=3){
        for(int j=0; j<9; j+=3){
            int cnt[9] = {0,};
            for(int di=i; di<i+3; di++){
                for(int dj=j; dj<j+3; dj++){
                    cnt[arr[di][dj]-1]++;
                }
            }
            if(cnt[0]==cnt[1]==cnt[2]==cnt[3]==cnt[4]==cnt[5]==cnt[6]==cnt[7]==cnt[8]){
                continue;
            }
            else return 0;
        }
    }
    return 1;
}