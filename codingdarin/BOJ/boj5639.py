# BOJ 5639 이진 검색 트리 (D3, G4)

import sys
sys.setrecursionlimit(20000)  # 재귀 한계 늘리기

def postorder(start, end):
   # 빈 구간이면 종료
   if start > end:
       return

   # 현재 구간의 루트는 첫 번째 원소
   root = arr[start]

   # 루트보다 큰 첫 번째 원소 찾기 (오른쪽 서브트리 시작점)
   i = start + 1
   while i <= end and arr[i] < root:
       i += 1
   
   # 후위 순회: 왼쪽 → 오른쪽 → 루트
   postorder(start+1, i-1)  # 왼쪽 서브트리 (루트보다 작은 값들)
   postorder(i, end)        # 오른쪽 서브트리 (루트보다 큰 값들)
   print(root)              # 루트 출력

# 전위 순회 결과 입력받기
arr = list(map(int, sys.stdin.read().strip().split('\n')))
N = len(arr)

# 전체 배열을 후위 순회로 출력
postorder(0, N-1)