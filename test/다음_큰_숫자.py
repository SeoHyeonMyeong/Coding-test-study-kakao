def solution(n):
    if n == 1:
        return 2
    b = bin(n)[2:]
    temp = b[-2:]
    i = len(b)-3
    while not (temp[0] == '0' and temp[1] == '1'):
        if i== -1:
            temp = '0' + temp
        else: 
            temp = b[i] + temp
        i -= 1
    
    num_one = 0
    for char in temp:
        if char == '1':
            num_one += 1
    num_zero = len(temp) - num_one
    temp = '1' + '0' * num_zero + '1' * (num_one - 1)

    ans = b[:-len(temp)] + temp
    ans = int('0b' + ans,2)
    return ans

print(solution(7))
