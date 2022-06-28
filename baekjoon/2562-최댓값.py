#
import sys

input = sys.stdin.readline

li = []
for i in range(9):
    li.append(int(input()))

ans = max(li)
print(ans)
print(li.index(ans) + 1)