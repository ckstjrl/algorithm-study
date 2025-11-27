#swea 5432. 쇠막대기 자르기 (D4)

# ----------------------------------------------3회차 풀이
    
T = int(input())
for tc in range(1, T+1):
    arr = input()
        
    start_bar = 0
    bar_count = 0
    
    for i in range(len(arr)):
        if arr[i] == '(':
            start_bar += 1
            
        else:  # arr[i] == ')'
            start_bar -= 1
            if arr[i-1] == '(':  # 레이저인 경우
                bar_count += start_bar
            else:  # 막대 끝인 경우
                bar_count += 1
    
    print(f"#{tc} {bar_count}")


# ----------------------------------------------2회차 풀이

# T = int(input())
# for tc in range(1, T+1):
#     arr = input()
        
#     arr = arr.replace('()','0') # 레이저 0으로 구분
    
#     start_bar = 0  # 현재 진행중인 막대 개수
#     bar_count = 0  # 총 막대 개수
    
#     for i in range(len(arr)):
#         if arr[i] == '(':
#             start_bar += 1
            
#         elif arr[i] == ')':
#             start_bar -= 1
#             bar_count += 1
            
#         elif arr[i] == '0':
#             bar_count += start_bar # 진행중 막대 2분할
    
#     print(f"#{tc} {bar_count}")
    
    
# ----------------------------------------------1회차 풀이
    
# T = int(input())
# for tc in range(1, T+1):
#     arr = input()
     
#     count_L = 1
#     count_R = 0
    
#     start_bar = 0
#     bar_count = 0
    
#     for i in range(1, len(arr)):
#         if arr[i] == '(':
#             count_L += 1
            
#         else:
#             count_R += 1
#             if arr[i-1] == '(':
#                 start_bar = count_L - count_R
#                 bar_count += start_bar
#             else:
#                 start_bar -= 1
#                 bar_count += 1
    
#     print(f"#{tc} {bar_count}")
    