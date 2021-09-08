dict = {}

def solution(orders, course):
    result = []
    for order in orders:
        order = "".join(sorted(order))
        devide_menu("",order)
    for n in course:
        max = 0
        ans = []
        for key in dict.keys():
            if len(key) == n and dict[key] >= 2: 
                if dict[key] > max:
                    max = dict[key]
                    ans = []
                    ans.append(key)
                elif dict[key] == max:
                    ans.append(key)
        result += ans
    result.sort()
    return result

def devide_menu(menu,order):
    n = len(order)
    if n == 0:
        if not menu in dict.keys():
            dict[menu] = 1
        else:
            dict[menu] += 1
        return
    for i in range(n):
        new_menu = menu + order[i]
        if not new_menu in dict.keys():
            dict[new_menu] = 1
        else:
            dict[new_menu] +=1
        if not i==n-1:
            devide_menu(new_menu,order[i+1:])
    
orders = ["XYZ", "XWY", "WXA"]
course = [2,3,4]
print(solution(orders,course))