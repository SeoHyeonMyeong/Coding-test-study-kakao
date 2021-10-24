def solution(price, money, count):
    total = price * sum(range(count+1))
    if money > total:
        return 0
    return total - money