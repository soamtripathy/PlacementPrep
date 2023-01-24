def sortPeople(names, heights):
        l = []
        for i in range(len(heights)):
            l.append([heights[i],names[i]])
        l.sort(reverse=True)
        k=[]
        for i in l:
            k.append(i[1])
        return k
print(sortPeople(["Mary","John","Emma"],[180,165,170]))
print(sortPeople(["Alice","Bob","Bob"], [155,185,150]))