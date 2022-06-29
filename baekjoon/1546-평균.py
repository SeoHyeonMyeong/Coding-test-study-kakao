#
import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))
M = max(li)
ans = [num / M * 100 for num in li]
print(sum(ans) / n)