import sys
sys.setrecursionlimit(10 ** 6) # recussionerror 피하기
node = [int(readline.rstrip()) for readline in sys.stdin]
# 더 빠르게 받기 -> 그런데 파이썬으로 할때만 됨...

def post_order(root_idx, last_idx):
    if root_idx > last_idx:
        return
    
    root = node[root_idx]
    
    # 오른쪽은 root보다 큼
    right_start_idx = root_idx + 1

    while right_start_idx <= last_idx: 
        if node[right_start_idx] > root:
            break
        right_start_idx += 1
    
    # 왼쪽 채우기 (root보다 작은 애들만)
    post_order(root_idx + 1, right_start_idx - 1)
    
    # 오른쪽 채우기 (root보다 큰 애들만)
    post_order(right_start_idx, last_idx)

    print(root)


post_order(0, len(node) - 1) 