# from math import comb
def solution(n):
    return fibo(n)
    # ans = 0
    # # 모두 세로로 하는 경우
    # # n개의 1 타일 사용
    # start = n
    # # 모두 가로로 하는 경우
    # # n/2 개의 2타일 사용
    # # n%2 개의 1타일 사용
    # end = n//2 + n%2

    # tile1 = start
    # tile2 = 0
    # while True:
    #     tile = tile1 + tile2
    #     large = max(tile1,tile2)
    #     tmp = tile - large
    #     ans += comb(tile,large)

    #     tile1 -= 2
    #     tile2 += 1
    #     if tile1 < 0:
    #         break
    # return ans% 1000000007

def fibo(n):
    a = 1
    b = 1
    if n <= 1:
        return 1
    n -= 1
    for i in range(n):
        ab = (a+b) % 1000000007
        a = b
        b = ab
    return b

n = 10000
print(solution(n))

