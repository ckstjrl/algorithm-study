#include<iostream>

using namespace std;

int main(int argc, char** argv)
{
    int T;
    

    cin >> T;
    for(int tc=1; tc <= T; ++tc)
    {
        int a;
        int b;
        string ro;
        cin >> a;
        cin >> b;


        if(a > b)
        {
            ro = '>';
        }
           
        else if(a == b)
        {
            ro = '=';
        }
        else
        {
            ro = '<';
        }

        cout << '#' << tc << ' ' << ro <<"\n";

    }


    return 0;
}