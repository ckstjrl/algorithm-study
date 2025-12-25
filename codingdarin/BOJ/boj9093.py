# BOJ 9093. 단어 뒤집기 (D1 /B1)

T = int(input())

for tc in range(1, T+1):
    txt = list(input().split())
    
    for block in txt:
        print(block[::-1], end=' ')