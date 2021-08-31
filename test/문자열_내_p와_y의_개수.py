def solution(s):
    num_p = 0
    num_y = 0

    for char in s:
        if char == "p" or char == "P":
            num_p += 1
        if char == "y" or char == "Y":
            num_y += 1
    if num_p == num_y:
        return True
    return False

print(solution("Pyy"))