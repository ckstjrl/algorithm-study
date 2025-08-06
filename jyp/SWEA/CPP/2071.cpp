#include<iostream>
#include <cmath>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;
    
    
	cin>>T;
	for(test_case = 1; test_case <= T; ++test_case)
	{
        int i;
        float sum=0;
        float num;
        
        for(i=1; i<=10; ++i)
        {
            cin>>num;
            sum += num;
	    }
    
    
        float result = sum/10.;
        cout <<"#"<<test_case<<" "<<round(result)<<"\n";
    }
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}