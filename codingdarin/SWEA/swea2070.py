T = int(input())

for tc in range(1,T+1):
    a, b = map(int, input().split())
    c=''
    if a < b: c = '<'
    elif a > b: c = '>' 
    else: c = '='
    
    print(f'#{tc} {c}')