def solution(clothes):
    table = dict()

    for item in clothes:
        kind = item.pop()
        cloth = item.pop()

        if not kind in table:
            table[kind] = [cloth]
        else:
            table[kind].append(cloth)

    ans = 1
    for key in table.keys():
        ans *= len(table[key]) + 1

    return ans - 1

# c = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
# print(solution(c))
