#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
	vector<string> a(5);
	for (int i = 0; i < 5; i++)
		cin >> a[i];

	for (int col = 0; col < 15; col++) {
		for (int row = 0; row < 5; row++) {
			if (col < (int)a[row].size())
				cout << a[row][col];
		}
	}
	return 0;
}