# A+B - 7
import sys

input = sys.stdin.readline
T = int(input())

for i in range(1, T+1):
    a,b = [int(num) for num in input().split()]
    print(f"Case #{i}: {a} + {b} = {a + b}")