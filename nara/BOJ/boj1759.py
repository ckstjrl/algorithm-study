import sys
input = sys.stdin.readline

L, C = map(int, input().split())
word = input().split()
word.sort()


def is_crypto(string):
    c_cnt, v_cnt = 0, 0
    for i in range(L):
        if string[i] in 'aeiou':
            v_cnt += 1
        else:
            c_cnt += 1
    if v_cnt < 1 or c_cnt < 2:
        return 0
    return 1


def backtracking(arr):
    if len(arr) == L:
        if is_crypto(arr):
            print(''.join(arr))
            return

    for i in range(len(arr), C):
        if arr[-1] < word[i]:
            arr.append(word[i])
            backtracking(arr)
            arr.pop()


for i in range(C - L + 1):
    a = [word[i]]
    backtracking(a)