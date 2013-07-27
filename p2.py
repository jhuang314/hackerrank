from itertools import chain, combinations

n = int(raw_input())
array = [long(x) for x in raw_input().split(' ')]
total = 0
def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

for s in powerset(array):

    g = []
    for v in s:
        sub = set(i for i,x in enumerate(bin(v)[::-1]) if x == '1')
        if len(sub) > 1:
            # flag = False
            # for j, subset in enumerate(g):
            #     subInt = subset.intersection(sub)
                
            #     if len(subInt) > 0:
            #         if flag:
            #             g
            #         else:
            #             g[j] = subset.union(sub)
            #             flag = True
            # if not flag:
            #     g.append(sub)
            g.append(sub)
    
    
    newG = []
    while len(g) > 0:
        last = g[0]
        mark = [0]
        for i in xrange(1,len(g)):
            if len(g[i].intersection(last)) > 0:
                last = last.union(g[i])
                mark.insert(0, i)
    
        for m in mark:
            del g[m]
        insert = False
        for ind, i in enumerate(newG):
            if len(i.intersection(last)) > 0:
                newG[ind] = i.union(last)
                insert = True
        if not insert:
            newG.append(last)
    
    
    used = 64 - len([x for s in newG for x in s])
    total += used + len(newG)
print total
