/*** 1158. 요세푸스 문제 ***/

#include<iostream>
#include<vector>
using namespace std;

int main() {
	int n, k;
	cin >> n >> k;
	vector<int> arr;
	for (int i = 0; i < n; i++) {	// 배열에 1부터 N까지 삽입
		arr.push_back(i + 1);
	}
	cout << "<";
	int j = k - 1;	// 처음 제거될 숫자 위치
	while (arr.size() > 1) {	// 배열에 숫자가 1개 남을 때까지 반복
		cout << arr[j] << ", ";
		arr.erase(arr.begin() + j);	// 출력한 숫자 제거

		j += k - 1;	// 제거된 숫자 인덱스에서 k-1칸 이동
		if (j >= arr.size()) {	// 인덱스가 배열의 범위 넘으면 다시 처음부터 시작
			j = j % arr.size();
		}
	}

	cout << arr[j] << ">";	// 마지막 숫자 출력

	return 0;
}