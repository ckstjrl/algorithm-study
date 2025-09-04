import sys
reminder = []
for _ in range(10):
    N = int(sys.stdin.readline())
    reminder.append(N % 42)
print(len(set(reminder)))