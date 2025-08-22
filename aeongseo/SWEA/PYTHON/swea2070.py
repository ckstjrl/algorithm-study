'''
2070. 큰 놈, 작은 놈, 같은 놈
'''

T = int(input())

for tc in range(1, T+1):
    a, b = map(int, input().split())

    if a < b:
        oper = '<'
    elif a == b:
        oper = '='
    else:
        oper = '>'
    
    print(f'#{tc} {oper}')