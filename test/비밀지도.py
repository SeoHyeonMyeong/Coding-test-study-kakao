def solution(n, arr1, arr2):
    ans = []
    for i in range(n):
        line = arr1[i] | arr2[i]
        line = str(bin(line))[2:]
        while len(line)<n:
            line = "0"+line
        code = ""
        for c in line:
            if c == "1":
                code +="#"
            else:
                code +=" "
        ans.append(code)
    return ans