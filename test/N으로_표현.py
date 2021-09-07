dict = {}

def solution(N, number):
    init(N)
    step(N)
    step(N)
    step(N)
    step(N)
    step(N)
    step(N)
    step(N)
    ans = dict.get(number)
    if ans == None:
        return -1
    return ans

def init(N):
    dict[N] = 1
    m = N
    for i in range(4):
        m = m*10 + N
        dict[m] = i+2

def step(N):
    keys = list(dict.keys())
    for key in keys:
        if not dict[key] == 8:
            for other in keys:
                if dict[key] + dict[other] <=8:
                    #plus
                    new_key = key + other
                    new_value = dict[key] + dict[other]
                    if (not new_key in keys) or new_value < dict[new_key]:
                        dict[new_key] = new_value
                    #minus
                    if key > other:
                        new_key = key - other
                        new_value = dict[key] + dict[other]
                        if (not new_key in keys) or new_value < dict[new_key]:
                            dict[new_key] = new_value
                    #multiply
                    new_key = key * other
                    new_value = dict[key] + dict[other]
                    if (not new_key in keys) or new_value < dict[new_key]:
                        dict[new_key] = new_value
                    #divide
                    if not other == 0:
                        new_key = int(key / other)
                        new_value = dict[key] + dict[other]
                        if (not new_key in keys) or new_value < dict[new_key]:
                            dict[new_key] = new_value

print(solution(5,31168))