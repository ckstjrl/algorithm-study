/* boj2563 - 색종이

가로, 세로의 크기가 각각 100인 정사각형 모양의 흰색 도화지가 있다. 
이 도화지 위에 가로, 세로의 크기가 각각 10인 정사각형 모양의 검은색 색종이를 색종이의 변과 도화지의 변이 평행하도록 붙인다. 
이러한 방식으로 색종이를 한 장 또는 여러 장 붙인 후 색종이가 붙은 검은 영역의 넓이를 구하는 프로그램을 작성하시오.*/

// 중복된 넓이를 어떻게 처리하는가?
// 아니면 그냥 100x100 배열을 만들고 값을 0으로 초기화 한 다음에 
// for문 돌면서 값을 1로 만들고 1인 값의 개수를 세면 될듯 

#include <iostream>
#include <vector>

using namespace std;

// 글로벌에서 선언 시 자동으로 0으로 초기화
int arr[100][100];

int main() {

    int N;
    cin >> N;
    
    int start_i, start_j;

    for (int i = 0; i < N; i++) {
        cin >>start_i >> start_j;

        for (int a = 0; a < 10; a++) {
            for (int b = 0; b < 10; b++) {
                arr[start_i + a][start_j + b] = 1;
            }
        }
    }
    int cnt = 0;

    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++) {
            if (arr[i][j] == 1) {
                cnt += 1;
            }
        }
    }

    cout << cnt;

    return 0;
}