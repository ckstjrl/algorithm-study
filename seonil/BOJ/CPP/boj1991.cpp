/*
BOJ1991. 트리 순회

[문제]
이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.

예를 들어 위와 같은 이진 트리가 입력되면,

* 전위 순회한 결과 : ABDCEFG // (루트)→(왼쪽 자식)→(오른쪽 자식)
* 중위 순회한 결과 : DBAECFG // (왼쪽 자식)→(루트)→(오른쪽 자식)
* 후위 순회한 결과 : DBEGFCA // (왼쪽 자식)→(오른쪽 자식)→(루트)
가 된다.

[입력]
첫째 줄에는 이진 트리의 노드의 개수 N(1 ≤ N ≤ 26)이 주어진다.
둘째 줄부터 N개의 줄에 걸쳐 각 노드와 그의 왼쪽 자식 노드, 오른쪽 자식 노드가 주어진다. 노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드가 된다. 자식 노드가 없는 경우에는 .으로 표현한다.

[출력]
첫째 줄에 전위 순회, 둘째 줄에 중위 순회, 셋째 줄에 후위 순회한 결과를 출력한다. 각 줄에 N개의 알파벳을 공백 없이 출력하면 된다.
*/

#include <iostream>
#include <vector>
using namespace std;

vector<vector<char>> tree(26, vector<char>(2, '.'));  // [노드번호][왼쪽,오른쪽] 자식 저장

// 전위 순회 (루트 → 왼쪽 → 오른쪽)
void preorder(char node) {
    if (node == '.') return;  // 현재 노드가 없다면 종료
    cout << node;  // 현재 노드 출력
    preorder(tree[node - 'A'][0]);  // 왼쪽 서브트리에 대하여 전위 순회
    preorder(tree[node - 'A'][1]);  // 오른쪽 서브트리에 대하여 전위 순회
}

// 중위 순회 (왼쪽 → 루트 → 오른쪽)
void inorder(char node) {
    if (node == '.') return;  // 현재 노드가 없다면 종료
    inorder(tree[node - 'A'][0]);  // 왼쪽 서브트리에 대하여 중위 순회
    cout << node;  // 현재 노드 출력
    inorder(tree[node - 'A'][1]);  // 오른쪽 서브트리에 대하여 중위 순회
}

// 후위 순회 (왼쪽 → 오른쪽 → 루트)
void postorder(char node) {
    if (node == '.') return;  // 현재 노드가 없다면 종료
    postorder(tree[node - 'A'][0]);  // 왼쪽 서브트리에 대하여 후위 순회
    postorder(tree[node - 'A'][1]);  // 오른쪽 서브트리에 대하여 후위 순회
    cout << node;  // 현재 노드 출력
}

int main() {
    int N;
    cin >> N;  // 이진 트리 노드의 개수 N 입력 받기

    // 이진 트리 입력 받기
    for (int i = 0; i < N; i++) {
        char node, left, right;
        cin >> node >> left >> right;
        tree[node - 'A'][0] = left;  // 입력 노드의 왼쪽 자식을 저장
        tree[node - 'A'][1] = right;  // 입력 노드의 오른쪽 자식을 저장 
    }

    // 루트 A부터 전위 순회, 중위 순회, 후위 순회 시작
    preorder('A');
    cout << '\n';
    inorder('A');
    cout << '\n';
    postorder('A');
    cout << '\n';

    return 0;
}
