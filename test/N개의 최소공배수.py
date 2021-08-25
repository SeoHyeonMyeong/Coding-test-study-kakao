array = [2,6,8,14]

def gcd(a, b):
	while(b!=0):
		r = a%b
		a = b
		b = r
	return a

def lcm(a, b):
    return a * b / gcd(a,b)

def solution(arr):
    answer = 1
    for a in arr:
        answer = lcm(answer,a)
    return answer

print(int(solution(array)))