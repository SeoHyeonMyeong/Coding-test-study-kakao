#
import sys

input = sys.stdin.readline
n, x = [int(num) for num in input().split()]
li = [int(num) for num in input().split()]

ans = [str(num) for num in li if num < x]
print(" ".join(ans))