def sortByHeight(a):
    return a + 1


first = [-1, 3, -1, 5, 2, -1]
new = list(map(sortByHeight, first))
print(new)