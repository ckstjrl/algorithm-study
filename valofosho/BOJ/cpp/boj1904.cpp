#include <iostream>
#include <vector>

using namespace std;

int n;
vector<int> dp;

int main(){
	ios::sync_with_stdio(false);
	cin.tie(NULL);
	
	cin >> n;
	dp.assign(n+1, 0);
	for (int i = 1; i < n+1; i++){
		cin >> dp[i];
	}
	dp[0] = 0;
	dp[1] = 1;
	dp[2] = 2;
    for (int i = 3; i < n+1; i++){
		dp[i] = (dp[i-1] + dp[i-2])%15746;
	}
	cout << dp[n];
    return 0;

}