import sys
input = sys.stdin.readline

while True:
    sentence = list(map(str, input().split()))
    cnt = 0
    if sentence[0] == '#':
        break
    for i in sentence[1:]:
        for j in i:
            if sentence[0] == j or sentence[0] == j.lower():
                cnt += 1
    print(sentence[0], cnt)