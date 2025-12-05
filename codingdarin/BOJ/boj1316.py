# BOJ 1316. 그룹 단어 체커 (D1 / S5)
# https://www.acmicpc.net/problem/1316


def is_group_word(word):
    seen = set()
    latest = ''
    
    for c in word:
        # 이미 본 문자라면
        if c in seen:
            # 연속으로 나온 게 아니라면 False 반환
            if latest != c:
                return False
        latest = c
        seen.add(c)
        
    return True

n = int(input())

# 입력 받고 트루 개수 세기
cnt = 0
for _ in range(n):
    word = input()
    if is_group_word(word):
        cnt += 1

print(cnt)
    

        
                
        
        