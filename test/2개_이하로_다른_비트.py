def solution(numbers):
    ans = []
    for num in numbers:
        binary = format(num,'b')
        print(binary[-1])
        if binary[-1] == "0":
            ans.append(num+1)
        else:
            i = len(binary) - 1
            last = binary[i]
            while True:
                i -= 1
                if i <= 0:
                    diff = len(binary) - 1
                    ans.append(num + 2**diff)
                    break
                if last == "1" and binary[i] == "0":
                    diff = len(binary) - i - 2
                    ans.append(num + 2**diff)
                    break
                last = binary[i]
    return ans

n = [1,2,3,4,5,6,7,8,9,10]
print(solution(n))
print(2**0)
