/*boj1764 - 듣보잡

김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 
듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
*/

/*
C++의 리스트 : vector
자료형 하나만 가능 : vector<int>는 정수형만 담음
데이터 그 자체를 저장 : 리스트는 주소 저장
len = size()
.append(값) = push_back(값)
*/

#include <iostream>
#include <vector> // 배열을 불러오기위한 라이브러리
#include <string> // C++에서는 char가 문자 1개만 사용 가능해서 스트링을 따로 불러와야한다고 함
#include <algorithm> //sort, 이진 탐색 사용 가능 하다고 함, 이진 탐색은 직접 구현해볼 예정

using namespace std;

bool binarySearch(vector<string>& arr, string target) {
    // '&'은 붙여 써야 벡터를 복사하지 않고 원본을 참조해서 속도가 빠르다고 함
    int left = 0;
    int right = arr.size() - 1;

    while (left <= right) {
        int mid = (left + right) / 2; //중간 인덱스

        if (arr[mid] == target) {
            return true;
        }
        else if (arr[mid] < target) {
            //중간값보다 타겟이 크면? 오른쪽을 더 봐야함
            left = mid + 1;
        }
        else {
            // 중간값보다 타겟이 작으면? 왼쪽을 더 봐야함
            right = mid - 1;
        }
    }
    return false;
}




int main() {
    int N, M;
    cin >> N >> M;

    vector<string> unheard(N); // 듣도 못한 사람
    for(int i = 0; i < N; i++) {
        cin >> unheard[i];
    }

    // 기본 오름차순 정렬 
    sort(unheard.begin(), unheard.end());
    // 내림차순 정렬 하고 싶으면 세번째 인자로 greater<자료형>() 넣어주기
    // sort(unheard.begin(), unheard.end(), greater<string>()); 
    // 또는 rbegin(), rend() 사용하기 reverse
    // sort(unheard.rbegin(), unheard.rend());

    vector<string> result;
    string name;

    for(int i = 0; i < M; i++) {
        cin >> name;
        if (binarySearch(unheard, name)) {
            result.push_back(name);
        }
    }

    // 사전 순 출력해야 하므로 다시 sort
    sort(result.begin(), result.end());

    cout << result.size() << "\n";
    for(int i = 0; i < result.size(); i++) {
        cout << result[i] << "\n";
    }



    return 0;
}