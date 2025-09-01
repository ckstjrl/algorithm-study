# 초심자의 회문 검사
 
T = int(input())
 
for tc in range(1,T+1):
    arr = input()
    if arr == arr[::-1]:
        result = 1
    else:
        result = 0
 
    print(f'#{tc} {result}')