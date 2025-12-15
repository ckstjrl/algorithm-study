# BOJ10809. 알파벳 찾기 / D1
import sys
alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

arr = list(sys.stdin.readline())

for i in range(len(alpha)):
    if alpha[i] in arr:
        alpha[i] = arr.index(alpha[i])
    else:
        alpha[i] = -1

print(' '.join(map(str, alpha)))