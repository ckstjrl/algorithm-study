/*
BOJ10799 : 쇠막대기 (S2)

해결 방법 : 레이저가 나오면, 파이프만큼 개수를 늘리고, 파이프가 끝나면 파이프 개수를 줄이는 방식으로 해결.

*/

#include<iostream>
#include<stack>
#include<string.h>
using namespace std;
int main()
{
	stack<int> stick;
	string str;
	
	int cnt = 0;
	cin >> str;
	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] == '(' && str[i+1] == ')')
		{
			cnt += stick.size();
			i++;
		}
		else if (str[i] == '(')
		{
			stick.push(i);
		}
		else if (str[i] == ')')
		{
			cnt++;
			stick.pop();
		}
	}
	cout << cnt;
}