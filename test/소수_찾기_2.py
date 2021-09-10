import numpy as np

prime = dict()
prime_number = []

def eratos(n):
    global prime_number
    limit = int(np.sqrt(n)+1)
    prime_number = [True] * (n+1)
    prime_number[0] = False
    prime_number[1] = False
    
    for num in range(2,limit):
        if prime_number[num]:
            delete_multi(num,n)

def delete_multi(num,n):
    global prime_number
    i = 2
    while i * num < n:
        prime_number[i*num] = False
        i += 1

def solution(n):
    global prime_number
    global prime
    limit = 10**len(n)-1
    eratos(limit)

    combine("",n)
    return len(prime.keys())

def combine(num,s):
    global prime
    if num == "":
        pass
    elif not int(num) in prime:
        if prime_number[int(num)]:
            prime[int(num)] = 1
    for i in range(len(s)):
        combine(num+s[i],s[:i] + s[i+1:])

# print(solution("01333"))
# print(prime)