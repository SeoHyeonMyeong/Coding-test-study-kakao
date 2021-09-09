def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(reverse=True,key=lambda x:(x*4))
    # numbers.sort(reverse=True)
    ans = ""
    if numbers[0] == "0":
        return "0"
    for num in numbers:
        ans += num
    return ans

numbers = [0,0]
print(solution(numbers))