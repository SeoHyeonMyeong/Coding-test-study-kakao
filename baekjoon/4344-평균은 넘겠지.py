#
import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    li = list(map(int, input().split()))
    N = li.pop(0)
    A = sum(li) / N
    ans = [1 for item in li if item > A]
    print(f"{sum(ans) / N * 100:.3f}%")
    