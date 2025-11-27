/* boj27160 - 할리갈리
《할리갈리》는 단추가 달린 종 하나와 과일이 그려진 카드들로 구성된 보드게임입니다.

카드에는 총 
$4$종류의 과일이 최대 
$5$개까지 그려져 있습니다. 
그려진 과일의 종류는 딸기, 바나나, 라임, 그리고 자두입니다.

게임을 시작할 때 플레이어들은 카드 뭉치를 공평하게 나눠가지며 자신이 가진 카드를 전부 소모하면 패배합니다.

게임은 시작 플레이어가 본인의 카드 뭉치에서 카드 한 장을 공개하는 것으로 시작합니다. 
이후 반시계 방향으로 돌아가며 본인의 카드를 한 장씩 공개합니다.

펼쳐진 카드들 중 한 종류 이상의 과일이 정확히 
$5$개 있는 경우 종을 눌러야 하며 
가장 먼저 종을 누른 플레이어가 모든 카드를 모아 자신의 카드 뭉치 아래에 놓습니다. 
종을 잘못 누른 경우 다른 모든 플레이어에게 카드를 한 장씩 나누어줘야 합니다.

《할리갈리》를 처음 해보는 한별이는 할리갈리 고수인 히나에게 이기기 위해 여러분에게 도움을 청했습니다. 
한별이를 도와 펼쳐진 카드들의 목록이 주어졌을 때, 한별이가 종을 쳐야 하는지 알려주세요.
*/

#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    int strawberry = 0, banana = 0, lime = 0, plum = 0;

    for (int i = 0; i < N; i++) {
        string fruit;
        int cnt = 0;

        cin >> fruit >> cnt;

        if (fruit == "STRAWBERRY") {
            strawberry += cnt;
        }
        else if (fruit == "BANANA") {
            banana += cnt;
        }
        else if (fruit == "PLUM") {
            plum += cnt;
        }
        else if (fruit == "LIME") {
            lime += cnt;
        }
    }
    if (strawberry == 5 or banana == 5 or lime == 5 or plum == 5) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }
    


    return 0;
}