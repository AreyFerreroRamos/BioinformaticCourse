lst = [ 14, 25, 32, 36, 43, 45, 48, 68, 69, 80 ]
x = 39

def search_sorted(lst, x):
    for i in range(len(lst)):
        if x <= lst[i]:
            return i
    return i + 1

print(search_sorted(lst, x))
