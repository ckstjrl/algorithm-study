"""
1926. 간단한 369게임 D2

3 6 9 게임을 프로그램으로 제작중이다. 게임 규칙은 다음과 같다.
1. 숫자 1부터 순서대로 차례대로 말하되, “3” “6” “9” 가 들어가 있는 수는 말하지 않는다.
  1 2 3 4 5 6 7 8 9…

2. "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.  
예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
 

입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를
게임 규칙에 맞게 출력하는 프로그램을 작성하라.
박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
여기서 주의해야 할 것은 박수 한 번 칠 때는 - 이며, 박수를 두 번 칠 때는 - - 가 아닌 -- 이다. 
 
[제약사항]
N은 10이상 1,000이하의 정수이다. (10 ≤ N ≤ 1,000)

[입력]
입력으로 정수 N 이 주어진다.


"""
N = int(input())
arr = list(map(str, range(1, N+1))) # 1~N+1까지의 array

for item in arr : # array 내 item 순회
    count = 0 # '-'를 반복할 기본값
    for char in item : # item 내 char 순회
        if char in ['3', '6', '9'] : # 369 박수 횟수 업데이트
            count += 1         
    else :
        if count > 0 : # count가 있었으면 업데이트한 값만큼 print
            print('-'*count, end=' ')
        else :
            print(item, end=' ') # 없었으면 item 전체 반환






# for item in arr :
#     count = 0
#     for char in item :
#         if char in ['3', '6', '9'] : 
#             count += 1        
#         else :
#             print(char, end='')
#     else :
#         print('-' * count, end='')
#     print(end=' ')


# N = int(input())
# arr = list(map(str, range(1, N+1)))

# for item in arr :
#     count = 0
#     for char in item :
#         if char in ['3', '6', '9'] :
#             print('-', end='')
#         else :
#             print(char, end='')
#     print(end=' ')