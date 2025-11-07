// BOJ9070 : 장보기 (B2)
// 해결 방법 : 중량 당 가격을 조사해서, 더 많은 중량을 살 수 있게 하기 

#include <iostream>
using namespace std;

int main() {
    int tc;
    cin >> tc;

    while (tc--) {
        int n; 
        cin >> n;

        double max_ratio = -1.0; 
        int best_price = 0;      

        for (int i = 0; i < n; ++i) {
            int weight, cost; 
            cin >> weight >> cost;
            double current_ratio = (double)weight / cost;

            if (current_ratio > max_ratio) {
                max_ratio = current_ratio;
                best_price = cost;
            } else if (current_ratio == max_ratio) {
                if (cost < best_price) {
                    best_price = cost;
                }
            }
        }
        cout << best_price << "\n";
    }

    return 0;
}