def solution(skill, skill_trees):
    ans = len(skill_trees)
    for skill_tree in skill_trees:
        current = -1
        for item in skill_tree:
            if item in skill:
                now = skill.index(item)
                print(skill[now])
                if now - current == 1:
                    current = now
                else:
                    ans -= 1
                    break
    return ans

skill = "CBD"
st = ["BACDE","CBADF","AECB","BDA"]
print(solution(skill,st))