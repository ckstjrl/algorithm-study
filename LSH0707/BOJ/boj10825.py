import sys
input = sys.stdin.readline
N = int(input())
alpha = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
    'a': 27, 'b': 28, 'c': 29, 'd': 30, 'e': 31, 'f': 32, 'g': 33, 'h': 34, 'i': 35, 'j': 36,
    'k': 37, 'l': 38, 'm': 39, 'n': 40, 'o': 41, 'p': 42, 'q': 43, 'r': 44, 's': 45, 't': 46,
    'u': 47, 'v': 48, 'w': 49, 'x': 50, 'y': 51, 'z': 52
}
arr = []
for _ in range(N):
    a, b, c, d = input().split()  # 이름, 국어, 영어, 수학
    e = []  # 알파벳 순서 리스트
    for i in a:
        e.append(alpha[i])
    arr.append((a, b, c, d, e))
arr.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[4]))  # 국어역순, 영어, 수학역순, 알파벳순서 정렬
for i in range(len(arr)):
    print(arr[i][0])