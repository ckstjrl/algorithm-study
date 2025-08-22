#swea 1989. 초심자의 회문 검사 (D2)

#-----------------------------------2회차 풀이 

T = int(input())

for tc in range(1, T+1):
    txt = input()

ans = 1 if txt == txt[::-1] else 0



#-----------------------------------1회차 풀이 

# T = int(input())

# for tc in range(1, T+1):
#     txt = input()
#     ans = 1

#     if txt != txt[::-1]:
#         ans = 0
    
#     print(f"#{tc} {ans}")