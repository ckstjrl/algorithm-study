from collections import deque

T = int(input())

for tc in range(1, T+1):
    AC = input()
    n = int(input())
    
    string = input().rstrip(']')
    string = string.lstrip('[')
    if n==0:
        arr = deque()
    else:
        arr = deque(string.split(','))

    r_cnt = 0
    flag = 0
    for ac in AC:
        if ac == 'R':
            r_cnt +=1
        elif ac == 'D' and arr:
            if r_cnt % 2 == 0:
                arr.popleft()
            else:
                arr.pop()
        else:
            flag=1
            break

    if flag == 1:
        print('error')
    elif r_cnt % 2 == 0:
        print('['+','.join(arr)+']')
        
    else:
        arr.reverse()
        print('['+','.join(arr)+']')

        
            

