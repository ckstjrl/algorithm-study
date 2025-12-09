#include <iostream>
#include <cmath>

using namespace std;

using ll = long long;
int n;


void hanoi(int n, int start, int mid, int goal){
	// 가장 큰 한 원만 남았을 때가 탈출 조건
    if (n == 1){
		cout << start << ' ' << goal << '\n';
		return;
	}else{
        // 큰 칸을 옮기기 위해 n-1개를 mid로 옮겨준다
		hanoi(n-1, start, goal, mid);
		cout << start << ' ' << goal << '\n';
		// mid에 옮긴 애들을 다시 최종 목적지로 옮기기
        hanoi(n-1, mid, start, goal);
	}
}



int main(){
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	
	cin >> n;
	ll temp = pow(2,n)-1;
	cout << temp << '\n';
	
	hanoi(n, 1, 2, 3);
    
    return 0;

}