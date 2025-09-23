# BOJ 1759. 암호 만들기 (D3, G5)


#--------------------------------2회차 풀이

L, C = map(int, input().split())
chars = list(input().split())
chars.sort()

path = []

def backtrack(start):
    # 종료 조건: L개 선택 완료
    if len(path) == L:
        # 모음 개수 체크
        vowels = 0
        for c in path:
            if c in 'aeiou':
                vowels += 1
        
        # 모음 1개 이상, 자음 2개 이상
        if vowels >= 1 and L - vowels >= 2:
            print(''.join(path))
        return
    
    # start부터 끝까지 선택 가능
    for i in range(start, C):
        path.append(chars[i])
        backtrack(i + 1)  # 다음 선택은 i+1부터
        path.pop()

backtrack(0)  # 0번 인덱스부터 시작

#--------------------------------1회차 풀이

L, C = map(int, input().split())
chars = list(input().split())
chars.sort()

path = [] 
ans = []

# n번째 글자 정하는 함수
def pick(n):
    global ans
    # 종료 조건: L글자일 때
    if n == L and len(path) == L:
        # 사전 순인지 검사
        if sorted(path) == path: 
            
            #모음 1 자음 2 이상인지 검사
            cnt = 0 
            for c in 'aeiou':
                cnt += path.count(c)

            if cnt >= 1 and L - cnt >= 2:             
                ans.append(''.join(path))
                return

    for i in range(n, len(chars)):
        if chars[i] not in path:
            path.append(chars[i])
            pick(n+1)
            # 백트랙
            path.pop()
        

pick(0)    #0번째 글자부터 정하기
print(*ans, sep='\n')    

