// 2068 최대수 구하기

#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
    int T;
    cin >> T;
    for(int tc=1; tc <= T; ++tc)
    {
        int num;
        int max_num=0;
        for(int i=0; i < 10; ++i)
        {
            
            
            cin >> num;
            
            if(max_num < num)
            {
                max_num = num;
            }
        }

        cout << '#' << tc << ' ' << max_num <<"\n";
    }
    return 0;
}