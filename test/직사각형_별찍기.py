n, m = map(int, input().strip().split(' '))
print(n,m)
for x in range(m):
    for y in range(n):
        print('*',end = '')
    print()