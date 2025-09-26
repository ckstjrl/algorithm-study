import sys
input = sys.stdin.readline
L, C = map(int, input().split())  # 암호길이 L(최소 모음1개, 자음2개) >= 3
arr = list(input().split())
arr.sort()  # 알파벳 정렬
ans = []
def check(char):
    v = 0
    c = 0
    for i in char:
        if i in 'aeiou':
            v = v + 1
        else:
            c = c + 1
    if v >= 1 and c >= 2:  # 최소 자음 모음 갯수 확인
        return True
    
def p(char,cnt,start):
    if cnt == L:
        if check(char):  # 조건 충족 하면 출력리스트에 append
            ans.append(char)
        return    
    for i in range(start, len(arr)):  # 중복 x 
        p(char+arr[i], cnt+1, i+1)

p('', 0, 0)
print('\n'.join(ans))