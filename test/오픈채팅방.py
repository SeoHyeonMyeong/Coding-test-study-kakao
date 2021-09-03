user = {}
chat = []

user["uid0000"]="admin"

def in_user(id):
    if id in user.keys():
        return True
    return False


def solution(record):
    for r in record:
        command = r.split(' ')
        if command[0] == "Enter" or command[0] == "Leave":
            chat.append([command[0], command[1]])
        if command[0] == "Enter" or command[0] == "Change":
            user[command[1]] = command[2]
    
    ans = []
    for c in chat:
        nickname = user[c[1]]
        if c[0] == "Enter":
            ans.append("%s님이 들어왔습니다."%nickname)
        elif c[0] == "Leave":
            ans.append("%s님이 나갔습니다."%nickname)
    return ans

# record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
# print(solution(record))