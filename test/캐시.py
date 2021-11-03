def solution(cacheSize, cities):
    cache = []
    ans = 0
    hit = 1
    miss = 5
    if cacheSize == 0:
        return 5 * len(cities)
    for city in cities:
        city = city.lower()
        if city in cache:
            ans += hit
            cache.remove(city)
            cache.append(city)
        else:
            ans += miss
            if len(cache) == cacheSize:
                cache.pop(0)
            cache.append(city)
    return ans

# s = 3
# c = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
# print(solution(s,c))