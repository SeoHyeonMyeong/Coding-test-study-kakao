available = []
for i in range(ord("A"), ord("Z")+1):
    available.append(chr(i))
print(available)

def solution(str1, str2):
    dict1 = multidict(str1)
    dict2 = multidict(str2)
    inter,union = find_inter_union(dict1,dict2)
    j = jaccard(inter,union)
    print([inter,union])
    return int(j * 65536) 

def multidict(str):
    str = str.upper()
    new_set = dict()
    for i in range(1,len(str)):
        if not(str[i-1] in available and str[i] in available):
            continue
        key = str[i-1:i+1]
        if key in new_set:
            new_set[key] +=1
        else:
            new_set[key] = 1
    return new_set

def find_inter_union(dict1,dict2):
    inter = dict()
    union = dict()
    all_key = set(list(dict1.keys()) + list(dict2.keys()))
    for key in all_key:
        if key in dict1 and key in dict2:
            inter[key] = min(dict1[key],dict2[key])
            union[key] = max(dict1[key],dict2[key])
        elif key in dict1:
            union[key] = dict1[key]
        elif key in dict2:
            union[key] = dict2[key]
    return inter,union

def jaccard(inter,union):
    inter_sum = sum([inter[i] for i in inter.keys()])
    union_sum = sum([union[i] for i in union.keys()])
    if union_sum == 0:
        return 1
    return inter_sum / union_sum



str1 = "handshake"
str2 = "shake hands"
print(solution(str1,str2))