/* boj12605 - 단어순서 뒤집기
스페이스로 띄어쓰기 된 단어들의 리스트가 주어질때, 단어들을 반대 순서로 뒤집어라. 
각 라인은 w개의 영단어로 이루어져 있으며, 총 L개의 알파벳을 가진다. 
각 행은 알파벳과 스페이스로만 이루어져 있다. 
단어 사이에는 하나의 스페이스만 들어간다.
*/

// 스페이스바를 기준으로 뒤집기..?
// 스택에 넣었다가 빼면 될듯

#include <iostream>
#include <string>
#include <vector>
#include <sstream> // 파이썬의 split() 대체제.

using namespace std;

int main() {
    // 입출력 속도 향상
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    // cin >> N은 숫자를 입력받고 나서, 엔터(\n) 키 입력을 버퍼에 남겨둠
    // getline을 쓰면, getline은 버퍼에 남아있던 엔터를 보고 빈 줄 읽고 넘어가버림
    // 따라서 cin 다음에 getline을 쓸 때는 cin.ignore(); 써주기
    cin.ignore();

    for (int i = 0; i < N; i++) {
        string line;
        // 공백 포함된 한 줄 통째로 읽기
        // 예시 : "this is a test"가 메모리에 저장됨
        getline(cin, line);

        // line을 감싸고 첫 번째 위치에서 대기
        stringstream ss(line);
        string word;
        vector<string> arr;

        // ss에서 단어를 하나씩 꺼내 word에 담음 (공백은 자동 분리)
        // 공백이 나올 때까지 읽음.
        while (ss >> word){
            arr.push_back(word);
        }
        
        cout << "Case #" << i + 1 << ": ";

        for (int j = arr.size() - 1; j >= 0; j--) {
            cout << arr[j];

            if (j > 0) {
                // 마지막 단어 아니면 공백 출력하기
                cout << " ";
            }
        }

        cout << "\n";

    }
    return 0;
}