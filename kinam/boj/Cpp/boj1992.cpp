/*boj1992 - 쿼드트리
흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다. 
흰 점을 나타내는 0과 검은 점을 나타내는 1로만 이루어진 영상(2차원 배열)에서 같은 숫자의 점들이 한 곳에 많이 몰려있으면, 쿼드 트리에서는 이를 압축하여 간단히 표현할 수 있다.

주어진 영상이 모두 0으로만 되어 있으면 압축 결과는 "0"이 되고, 모두 1로만 되어 있으면 압축 결과는 "1"이 된다. 
만약 0과 1이 섞여 있으면 전체를 한 번에 나타내지를 못하고, 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래, 이렇게 4개의 영상으로 나누어 압축하게 되며, 이 4개의 영역을 압축한 결과를 차례대로 괄호 안에 묶어서 표현한다



위 그림에서 왼쪽의 영상은 오른쪽의 배열과 같이 숫자로 주어지며, 이 영상을 쿼드 트리 구조를 이용하여 압축하면 "(0(0011)(0(0111)01)1)"로 표현된다. N ×N 크기의 영상이 주어질 때, 이 영상을 압축한 결과를 출력하는 프로그램을 작성하시오.
*/

// 분할정복?
// 좌상 우상 좌하 우하로 계속 파고들어야함
// 예제입력 1을 보면 8 * 8 
// 좌상의 4 * 4로 파고들고
// 거기서 2*2의 좌상은 1111 이니까 1
// 2*2의 우상은 1111이니까 1
// 2*2의 좌하는 0000 이니까 0 
// 2*2의 우하는 0101이니까 0101
// 따라서 110(0101)이다 이걸 반복하면 될듯?

#include <iostream>
#include <string>

using namespace std;


// 이렇게 선언하면?
string arr[64];


void solve(int y, int x, int size) {
    /* 처음 N * N 크기의 배열을 검사해서 같은 색인지 아닌지 검사부터 하고
    0 1로 간단하게 못나타내면 이걸 분해해서 0101 이런식으로 나타내게 하기
    */
    char current = arr[y][x];
    bool is_same = true;

    for (int i = y; i < y + size; i++) {
        for (int j = x; j < x + size; j++) {
            if (arr[i][j] != current) {
                is_same = false;
                break;
            }
        }
        if (!is_same) break;
    }

    if (is_same) {
        //모든 색이 같으면 출력하고 끝내면 됨
        cout << current;
        return;
    }

    // 아니면 4등분하고 파고들기
    cout << "(";

    int half = size /2;

    solve(y, x, half); // 좌상
    solve(y, x + half, half); // 우상
    solve(y + half, x, half); // 좌하
    solve(y + half, x + half, half); // 우하

    cout << ")";
    
}




int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    // cout << arr; 
    // 0x7ff75152a08011110000 >> 메모리 주소
    // for (int i = 0; i < N; i++) {
    //     cout << arr[i] << endl;
    // } 아무것도 안나옴
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
    }

    solve(0, 0, N);

    return 0;
}