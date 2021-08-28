def fibonachi(n):
    list = [];
    list.append(0)
    list.append(1)
    list.append(1)
    for i in range(3,n+1):
        list.append(list[i-1] % 1234567 + list[i-2] % 1234567)
    return list[n] % 1234567

print(fibonachi(3))