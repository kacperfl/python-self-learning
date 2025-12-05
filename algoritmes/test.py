def search(lst, target):
    
    links = 0
    rechts = len(lst) - 1
    
    while links <= rechts:
        midden = (links + rechts) // 2

        if lst[midden] == target:
            return target
        elif lst[midden] < target:
            links = midden + 1
        elif lst[midden] > target:
            rechts = midden - 1
    return False


lijst = [27, 44, 31, 74, 47, 19, 59, 77, 61, 60, 66, 68, 63, 35, 8, 71, 1, 97, 62, 51, 69, 96, 40, 43,
       48, 33, 79, 32, 87, 45, 57, 11, 72, 49, 58, 37, 83, 15, 30, 13, 20, 18, 75, 23, 26, 17, 91,
       10, 100, 9, 28, 50, 81, 64, 5, 55, 89, 6, 90, 39, 25, 82, 36, 84, 73, 56, 88, 93, 12, 78,
       24, 54, 76, 65, 99, 3, 21, 34, 41, 53, 2, 92, 52, 22, 7, 42, 70, 86, 14, 4, 46, 85, 67,
       80, 16, 94, 95, 98, 29, 38]

lijst.sort()
print(search(lijst, 25))