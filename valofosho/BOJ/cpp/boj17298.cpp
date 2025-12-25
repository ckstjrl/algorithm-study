#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int n;
vector<int> arr;
vector<int> nge;
vector<int> st;

int main(){

    ios::sync_with_stdio(false);
	cin.tie(NULL);
	cin >> n;
	// 사이즈 정해주기 + nge는 -1을 초기값으로
	arr.assign(n,0);
	nge.assign(n, -1);
	for (int i = 0; i < n; i++){
		cin >> arr[i];
	}
	for (int i = 0; i < n-1; i++){
		if (arr[i] < arr[i+1]){
			nge[i] = arr[i+1];
			if (!st.empty()){
				while (arr[i+1] >  arr[st.back()]){
					nge[st.back()] = arr[i+1];
					st.pop_back();
					if (!st.size()){
						break;
					}
				}
			}
		}
		else {
			st.push_back(i);
		}
	}
	for (int i = 0; i < n; i++){
		cout << nge[i] << ' ';
	}
    return 0;

}
