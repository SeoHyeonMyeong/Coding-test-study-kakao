allow = []
for alpha in range(ord('a'),ord('z')+1):
    allow.append(chr(alpha))

for num in range(10):
    allow.append(str(num))
allow.append('-')
allow.append('_')
allow.append('.')

def delete_not_allowed(id):
    temp = ""
    for char in id:
        if char in allow:
            temp += char
    return temp

def delete_duplicated_point(id):
    temp = ""
    for i in range(len(id)):
        if i == len(id)-1:
            temp += id[i]
        elif id[i] =='.' and id[i+1] ==".":
            continue
        else:
            temp += id[i]
    return temp

def delete_edge_point(id):
    if id == ".":
        return ""
    if id[0] == ".":
        id = id[1:]
    if id[-1] == ".":
        id = id[:-1]
    return id

def process_null(id):
    if len(id) == 0:
        id = "a"
    return id

def process_overhead(id):
    if len(id) >= 16:
        id = id[:15]
    return id

def process_short(id):
    while len(id) < 3:
        id += id[len(id)-1]
    return id

def solution(new_id):
    new_id = new_id.lower()
    new_id = delete_not_allowed(new_id)
    new_id = delete_duplicated_point(new_id)
    new_id = delete_edge_point(new_id)
    new_id = process_null(new_id)
    new_id = process_overhead(new_id)
    new_id = delete_edge_point(new_id)
    new_id = process_short(new_id)

    return new_id

id = "=.="
print(solution(id))