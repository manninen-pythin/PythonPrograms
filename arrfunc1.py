def firstDuplicate(a):
    i = 0
    match = -1
    lowestind = len(a) + 1
    while i != len(a):
        if a[i] in a[i+1:] and a[i+1:].index(a[i]) < lowestind:
            lowestind = a[i+1:].index(a[i])
            match = a[i]
        i += 1
    return match


arr =  [1, 2, 1, 8, 9, 9, 9, 0, 1, 8]
print(firstDuplicate(arr))
