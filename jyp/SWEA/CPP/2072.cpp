#include<iostream>


using namespace std;

int main(int argc, char* argv)
{
    int test_case;
    int T;

    cin>>T;

    for(test_case = 1; test_case <= T; ++test_case)
    {
        int i;
        int result = 0; 
        int num;

        for(i = 1; i <= 10; ++i)
        {
            cin >> num;
            if (num%2 == 1)
            {
                result += num;
            }
        }
        cout << "#" << test_case << " " << result << '\n';
    }
    return 0;//정상종료시 반드시 0을 리턴해야합니다.
}