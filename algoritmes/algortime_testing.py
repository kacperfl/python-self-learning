def search(lst, target):
    links = 0
    rechts = len(lst) - 1
    
    while links <= rechts:
        mid = (rechts + links) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            links = mid + 1
        elif lst[mid] > target:
            rechts = mid - 1
    return -1

def sorting(lijst):

    if len(lijst) <= 1:
        return lijst

    middle = len(lijst) // 2
    links = lijst[:middle]
    rechts = lijst[middle:]

    links_sorted = sorting(links)
    rechts_sorted = sorting(rechts)

    index_links = 0
    index_rechts = 0
    resultaat = []

    while index_links < len(links_sorted) and index_rechts < len(rechts_sorted):

        if links_sorted[index_links] <= rechts_sorted[index_rechts]:
            resultaat.append(links_sorted[index_links])
            index_links += 1
        else:
            resultaat.append(rechts_sorted[index_rechts])
            index_rechts += 1

    while index_links < len(links_sorted):
        resultaat.append(links_sorted[index_links])
        index_links += 1

    while index_rechts < len(rechts_sorted):
        resultaat.append(rechts_sorted[index_rechts])
        index_rechts += 1
    return resultaat


def bubble(lst):
    
    while True:
        verwisseld = False
        for i in range(len(lst) - 1):
            buur = i + 1
            
            if lst[i] > lst[buur]:
                verwisseld = True
                lst[i], lst[buur] = lst[buur], lst[i]
                
        if verwisseld == False:
            break
    return lst
        
        


arr = [3, 5, 7, 2, 9, 1, 6, 2, 8, 9, 0, 5, 6, 51, 12, 34, 19, 34]

sorted_list = sorting(arr)

print(bubble(arr))
print(search(sorted_list, 19))
