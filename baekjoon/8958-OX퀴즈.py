#
import sys

input = sys.stdin.readline

def point(x):
    return int(x * (x + 1) / 2)

n = int(input())
for i in range(n):
    score = input().rstrip().split("X")
    result = [point(len(item)) for item in score]
    print(sum(result))