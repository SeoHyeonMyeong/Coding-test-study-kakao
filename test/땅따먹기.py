
def solution(land):
    memo = []
    memo.append(land[0])
    temp = []
    count = 0

    for row_index in range(1,len(land)):
        last_memo = memo[row_index-1]
        new_memo = []
        row = land[row_index]

        for i in range(len(row)):
            temp = last_memo.copy()
            temp.pop(i)
            new_memo.append(row[i]+max(temp))
        memo.append(new_memo)
    ans = memo[len(land)-1]
    ans = max(ans)
    return ans
        
def max(arr):
    max_num = arr[0]
    for i in arr:
        if i >= max_num:
            max_num = i
    return max_num
        


my_land = [[1,1,1,1],[2,2,2,3],[3,3,3,6],[4,4,4,7]]
my_land_2 = [[1,2,3,5],[5,6,7,8],[4,3,2,1]]
print(solution(my_land_2))