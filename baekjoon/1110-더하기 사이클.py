#
import sys

input = sys.stdin.readline
n = int(input())
target = n
count = 0

while True:
    a = n // 10
    b = n % 10
    c = (a + b) % 10
    n = int(str(b) + str(c))
    count += 1
    
    if target == n:
        break
print(count)