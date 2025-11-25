/* boj10814 - 나이순 정렬
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다. 
이때, 회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.
*/

// 파이썬에서 정렬에 람다 사용하는 방법을 C++에서는 어떻게 하는지 찾아보기
// 파이썬의 sort는 기본적으로 stable sort임. 나이가 같으면 원래 있던 순서 유지됨
// C++은 퀵 정렬 기반의 unstable sort라서 나이가 같다고 치면 누가 먼저 올지 모름
// 따라서 stable_sort 따로 써줘야함



#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;




int main() {

    int N;
    cin >> N;

    // C++에서 튜플은 pair<자료형, 자료형> 형태
    vector<pair<int, string >> members(N);

    // 입력 받기
    for(int i = 0; i < N; i++) {
        cin >> members[i].first >> members[i].second; // 데이터 개수 N을 미리 알 때는 이 방법이 효율적
        /*
        int age;
        string name;
        cin >> age >> name;
        members.push_back({age, name}); */
        // 개수를 모르면 편하게 이런 식으로 추가하기
    }

    // stable_sort, lambda 사용하기
    // [](매개변수){ return 조건; }
    // const, &는 속도 향상에 좋다고 함
    // return 조건문이 true면 a가 b보다 앞에 옴
    stable_sort(members.begin(), members.end(), [](const pair<int, string>& a, const pair<int, string>& b) {
        return a.first < b.first;
    });

    for(int i = 0; i < N; i++) {
        cout << members[i].first << " " << members[i].second << "\n";
    }


    return 0;
}