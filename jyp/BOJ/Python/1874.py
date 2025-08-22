N = int(input())
if N == 1:
    print('+\n-')

else:
    arr = [int(input()) for _ in range(N)]

    stack = [i for i in range(1, arr[0]+1)]
    max_num = arr[0]
    result = ['+'] * arr[0]
    for i in arr:
        if stack and stack[-1] == i:
            result.append('-')
            stack.pop()
        else :
            if max_num < i:
                for j in range(max_num+1, i+1):
                    stack.append(j)
                    result.append('+')
                max_num = i
                stack.pop()
                result.append('-')
            else:
                result = ['NO']
                break
    for output in result:
        print(output)
