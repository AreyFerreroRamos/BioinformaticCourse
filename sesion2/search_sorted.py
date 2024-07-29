def search_sorted(lst, x):
    for i in range(len(lst)):
        if x <= lst[i]:
            return i
    return i + 1

if __name__ == "__main__":
    lst = [ 14, 25, 32, 36, 43, 45, 48, 68, 69, 80 ]
    x = 39
    
    print("The value " + str(x) + " has the insertion position " + str(search_sorted(lst, x)) + " in the list.")
