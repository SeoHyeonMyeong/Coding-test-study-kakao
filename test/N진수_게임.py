num = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

def give_n(n,m):
    if m == 0:
        return '0' 
    count = n
    last_count = 0
    i = 1

    while m>=count:
        i += 1
        last_count = count
        count += (n**i - n**(i-1)) * i
    
    my_count = m - last_count
    if i==1:
        value = my_count
        value = make_str(value,n)
        last = 0
    else:
        value = n**(i-1) + int(my_count/i)
        value = make_str(value,n)
        last = my_count % i

    ans = value[last]

    return ans 

def make_str(value, n):
    if value/n == 0:
        return ""
    return make_str(int(value/n),n) + num[value%n]

def solution(n, t, m, p):
    ans = ''
    for i in range(t):
        ans += give_n(n,m * i + (p-1))
    return ans

print(solution(16,16,2,1))
# print(give_n(2,2))
# print(make_str(1333,16))
# 0 1 1 0 1 1 1 0 0 1 0 1 1 1 0 1 1 1