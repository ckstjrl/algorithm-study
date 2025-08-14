#include<iostream>
#include<vector>
#include<string>
#include <algorithm>

using namespace std;

int main(int argc, char** argv)
{
	int test_case;
	int T;


	cin>>T;


	for(test_case = 1; test_case <= T; ++test_case)
	{
        string ymd;
        string year;
        string month;
        string day;
        vector<int> v_1;
        vector<int> v_2;
        
        v_1.push_back(1);
        v_1.push_back(3);
        v_1.push_back(5);
        v_1.push_back(7);
        v_1.push_back(8);
        v_1.push_back(10);
        v_1.push_back(12);


        v_2.push_back(4);
        v_2.push_back(6);
        v_2.push_back(9);
        v_2.push_back(11);
        

        cin >> ymd;

        year = ymd.substr(0,4);
        month = ymd.substr(4,2);
        day = ymd.substr(6,2);

        string result;
        result = year+'/'+month+'/'+day;

        int day1 = stoi(day);
        int month1 = stoi(month);
        int year1 = stoi(year);








        if(month1 > 13 || month1 < 1)
        {

            result = "-1";
        }
        else if(find(v_1.begin(), v_1.end(), month1) != v_1.end())
        {

            if(day1 > 31)
            {
                result = "-1";
            }
                
        }
        else if(find(v_2.begin(), v_2.end(), month1) != v_2.end())
        {

            if(day1 > 30)
            {
                result = "-1";
            }
                
        }

        else if(month1=2)
        {

            if(day1 > 28)
                
            {
                result = "-1";
            }
        }



    cout << '#' << test_case << ' ' << result <<"\n";


	}
	return 0;//정상종료시 반드시 0을 리턴해야합니다.
}