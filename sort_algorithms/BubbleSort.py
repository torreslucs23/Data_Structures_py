def Bubble(l):
    for i in range(len(l)):
        for w in range(len(l)-1):
            if l[w] > l[w+1]:
                x = l[w + 1]
                l[w+1] = l[w]
                l[w] = x
    return l