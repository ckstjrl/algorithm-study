#include <iostream>
#include <vector>
#include <climits>

using namespace std;

int pos;          // 현재 탐색 위치 저장을 위한 변수
vector<int> arr;  // 전위 순회 결과를 위한 가변 배열

void postorder(int l, int h) {
    if (pos >= arr.size()) return;     // 모든 노드에 대해 처리했다면 종료

    int root = arr[pos];               // 현재 탐색하고 있는 노드를 root 로 설정

    if (root < l || root > h) return;  // 현재 root 가 현재 서브 트리 내에 있지 않으면 종료

    pos++;  // 다음 노드로 진행을 위해 1 증가

    // 후위 순회
    postorder(l, root - 1);  // 왼쪽 서브 트리일 경우
    postorder(root + 1, h);  // 오른쪽 서브 트리일 경우
    cout << root << '\n';    // root 출력
}

int main() {
    ios_base::sync_with_stdio(false);   // 입출력 속도 최적화
    cin.tie(NULL);

    int x;
    while (cin >> x) arr.push_back(x);  // 입력이 끝날 때까지 전위 순회 결과 vector 에 push

    postorder(INT_MIN, INT_MAX);  // INT 범위 내에서 탐색

    return 0;
}