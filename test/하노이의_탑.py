lst = [1,2,3]

# n번째 하노이탑
def solution(n):
    return hanoi(n,1,2,3)

def hanoi(n,start,mid,end):
    ans = []
    if n == 1:
        return [[start,end]]
    # n-1 하노이탑을 start -> mid 로 이동
    ans = ans + hanoi(n-1,start,end,mid)
    # n 번째 블록을 start -> end 로 이동
    ans = ans + [[start,end]]
    # n-1 하노이탑을 mid -> end 로 이동   
    ans = ans + hanoi(n-1,mid,start,end)
    return ans

n=3
print(solution(n))

# n번째 하노이탑 1 -> 3
# n-1 하노이탑을 1 -> 2
# n번째 블록을 1 -> 3
# n-1 하노이탑을 2 -> 3