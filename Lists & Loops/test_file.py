
def freq(lst):
    freqs = dict()
    
    for x in lst:
        if x in freqs:
            freqs[x] += 1
        else:
            freqs[x] = 1
    return freqs


lijst = [4,4,2,4,5,6,3,2,1,3,2,5,6,7,4,2,1,5,8]
print(freq(lijst))