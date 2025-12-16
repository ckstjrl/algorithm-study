# BOJ20971: No Time to Paint
import sys
input = sys.stdin.readline

def get_counts(s):
    n = len(s)
    counts = [0] * N
    stack = []
    c_count = 0

    for i in range(n):
        char = s[i]

        while stack and stack[-1] > char:
            stack.pop()
        
        if stack and stack[-1] == char:
            pass

        else:
            stack.append(char)
            c_count += 1
        
        counts[i] = c_count
    
    return counts

N, Q = map(int, input().split())
colors = input().strip()

prefix = get_counts(colors)
suffix = get_counts(colors[::-1])[::-1]

for _ in range(Q):
    a, b = map(int, input().split())

    l_cost = 0
    r_cost = 0

    if a > 1:
        l_cost = prefix[a-2]
    if b < N:
        r_cost = suffix[b]
    
    print(l_cost + r_cost)