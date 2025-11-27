# 1989. 최심자의 회문 / D2
T = int(input())
for tc in range(1, T+1):
    str_arr = input() 
    if str_arr == str_arr[::-1]:  # 받은 문자열과 거꾸로 한 문자열이 같은지 확인
        print('#'+str(tc), 1)
    else:
        print('#'+str(tc), 0)