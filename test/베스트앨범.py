def solution(genres, plays):
    data = dict()
    count = dict()
    for i in range(len(plays)):
        play = plays[i]
        genre = genres[i]
        if genre in data:
            data[genre].append([i,play])
            count[genre] += play
        else:
            data[genre] = [[i,play]]
            count[genre] = play
    
    ans = []
    count = sorted(count.keys(),key=count.get,reverse=True)
    for genre in count:
        a = data[genre]
        a.sort(reverse=True,key=lambda x: x[1])
        ans.append(a[0][0])
        if len(a)>1:
            ans.append(a[1][0])

    return ans

# g = ["classic", "pop", "classic", "classic", "pop"]
# p = [500, 600, 150, 800, 2500]
# print(solution(g,p))
