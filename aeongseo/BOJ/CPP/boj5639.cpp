/*** 5639. 이진 검색 트리 ***/

#include<iostream>
using namespace std;

void enque(int x);
void postorder(int t);

int L[1000001];	// 부모의 왼쪽 노드
int R[1000001];	// 부모의 오른쪽 노드

int main() {
	freopen("input.txt", "r",stdin);	// 파일로 입력 받기
	cin >> L[0];	// 루트 노드 저장
	int x;
	while (cin >> x) {	// 입력받을 때마다 노드 저장
		enque(x);
	}

	postorder(L[0]);	// 후위 순회
	return 0;
}

void enque(int x) {
	int root = L[0];	// 루트 노드
	while (1) {
		if (x < root) {	// 입력값이 루트노드 키보다 작을 때
			if (L[root] == 0) {	// 왼쪽 노드가 비었다면 키 삽입
			L[root] = x;
			break;
			}
			else {	// 왼쪽 노드에 키가 있다면 그 키를 루트노드로 삼음
				root = L[root];
			}
		}
		else {	// 입력값이 루트노드 키보다 클 때
			if (R[root] == 0) {	// 오른쪽 노드가 비었다면 키 삽입
				R[root] = x;
				break;
			}
			else {	// 오른쪽 노드에 키가 있다면 그 키를 루트 노드로 삼음
				root = R[root];
			}
		}
	}
}

void postorder(int t) {
	if (t != 0) {	// 키가 0이 아니라면 후위 순회
		postorder(L[t]);
		postorder(R[t]);
		cout << t << '\n';	// 키 출력
	}
}