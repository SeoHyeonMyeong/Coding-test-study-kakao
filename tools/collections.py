from collections import (Counter,
                         namedtuple,
                         OrderedDict,
                         defaultdict,
                         deque)

# 카운터
def counter_test():
    a = "ccccddaaaaaaaaaabbb"
    my_counter = Counter(a)
    print(my_counter.items())
    print(my_counter.most_common(2))
    
    return

# 구조화된 튜플
def namedtuple_test():
    Position = namedtuple('Position', 'x,y')
    p = Position(1, 3)
    print(p)
    
    return
    
# 순차 딕셔너리
def ordereddict_test():
    dict = OrderedDict()
    dict['a'] = 1
    dict['b'] = 5
    dict['c'] = 3
    dict['d'] = 4
    print(dict)
    
    return

# 기본값 딕셔너리
def defaultdict_test():
    dict = defaultdict(list)
    dict['a'].append(1)
    dict['b'].append(2)
    print(dict)
    
    return

# 덱
def deque_test():
    d = deque([3, 4, 5])
    d.append(6)
    d.appendleft(2)
    d.pop()
    d.popleft()
    
    d.extend([1,2,3])
    d.extendleft([1,2,3])
    print(d)
    
    return

if __name__ == "__main__":
    # counter_test()
    # namedtuple_test()
    # ordereddict_test()
    # defaultdict_test()
    deque_test()