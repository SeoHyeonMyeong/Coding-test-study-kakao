import numpy as np

prime_number = []

def eratos(n):
    global prime_number
    if n<=2:
        prime_number = [False]*2 + [True]
        return
    limit = int(np.sqrt(n))
    prime_number = [True] * (n+1)
    prime_number[0] = False
    prime_number[1] = False
    
    for num in range(2,limit+1):
        if prime_number[num]:
            delete_multi(num,n)
def delete_multi(num,n):
    global prime_number
    i = 2
    while i * num <= n:
        prime_number[i*num] = False
        i += 1

def is_prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def solution(n, k):
    global prime_number
    global prime
    
    ans = 0
    s = transform(n,k)
    li = s.split("0")
    li = list(filter(('').__ne__,li))

    for i in range(len(li)):
        li[i] = int(li[i])


    eratos(100000)
    
    for item in li:
        if item >= 100000:
            if is_prime(item):
                ans += 1
        elif prime_number[item]:
            ans += 1
    return ans

def transform(n,k):
    ans = ""
    while n > 0:
        ans = str(n % k) + ans
        n = int(n/k)
    return ans

# print(solution(110011,10))

# for i in range(3,100000):
#     print(i)
#     eratos(i)
#     prime_number = []