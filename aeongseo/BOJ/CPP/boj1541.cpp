/*** 1541. 잃어버린 괄호 ***/

#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
	string txt;
	cin >> txt;
	string temp1;
	temp1.clear();
	vector<int> num;
	vector<string> oper;

	for (int i = 0; i < txt.size(); i++) {
		if (txt[i] == '-' || txt[i] == '+') {	// 연산자를 만나면 연산자는 oper 배열에, 숫자는 num 배열에 저장
			num.push_back(stoi(temp1));
			temp1.clear();
			if (txt[i] == '-') {
				oper.push_back("-");
			}
			else {
				oper.push_back("+");
			}
		}
		else {
			temp1.push_back(txt[i]);
		}
		if (i == txt.size() - 1) {	// 마지막 숫자이면 num배열에 저장
			num.push_back(stoi(temp1));
		}
	}
	while (find(oper.begin(), oper.end(), "+") != oper.end()) {	// + 연산자가 있으면 반복
		for (int j = 0; j < oper.size(); j++) {
			if (oper[j] == "+") {	// oper에서 + 삭제, num에서 해당 인덱스와 +1 인덱스 요소 더한 후 삭제, 더한 값 해당 인덱스에 추가
				oper.erase(oper.begin()+j);
				int temp2 = num[j] + num[j + 1];
				num.erase(num.begin() + j);
				num.erase(num.begin() + j);
				num.insert(num.begin() + j, temp2);
			}
		}
	}
	int k = 0;
	while (num.size() > 1) {
		oper.erase(oper.begin());	// 연산자에 -만 남았으므로 oper 삭제와 num값 계산, 삭제, 추가 반복
		int temp3 = num[0] - num[1];
		num.erase(num.begin());
		num.erase(num.begin());
		num.insert(num.begin(), temp3);
	}
	cout << num[0];


	return 0;
}