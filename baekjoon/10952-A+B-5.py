#
import sys

input = sys.stdin.readline


while True:
    a,b = [int(num) for num in input().split()]
    if a == 0 and b == 0:
        break
    print(a+b)
