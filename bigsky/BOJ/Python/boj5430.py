# BOJ5430(D3): AC
import sys
input = sys.stdin.readline

def control(c):
    global is_reversed, start, end
    if c == 'R':
        is_reversed = not is_reversed
    else:
        if start == end:
            return True

        if is_reversed:
            end -= 1
        else:
            start += 1
    return False

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    raw_input = input().strip('[]\n')
    arr = raw_input.split(',') if raw_input else []

    is_reversed = False
    start = 0
    end = len(arr)

    for c in p:
        is_error = control(c)
        if is_error:
            break

    if is_error:
        print('error')
        continue
    else:
        n_arr = arr[start:end]
        if is_reversed:
            n_arr = reversed(n_arr)
    print('[' + ','.join(n_arr) + ']')
