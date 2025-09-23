import sys
input = sys.stdin.readline
letter_to_number = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15, 'F': 16, 'G': 17, 'H': 18, 'I': 19, 'J': 20, 'K': 21,
                    'L': 22, 'M': 23, 'N': 24, 'O': 25,'P': 26, 'Q': 27, 'R': 28, 'S': 29, 'T': 30, 'U': 31, 'V': 32,
                    'W': 33, 'X': 34, 'Y': 35, 'Z': 36}
N = int(input())
arr = [input().strip() for _ in range(N)]
arr_1 = [[] for _ in range(N)]
for i in range(len(arr)):
    a = len(arr[i])  # 단어길이
    b = 0  # 숫자의 합
    c = []  # 문자 순서
    for j in arr[i]:
        if j.isdigit():
            c.append(int(j))
            b = b + int(j)
        else:
            c.append(letter_to_number[j])
    arr_1[i] = [arr[i], a, b, c]
arr_1.sort(key = lambda x : (x[1], x[2], x[3]))  # sort
for i in range(len(arr_1)):
    print(arr_1[i][0])