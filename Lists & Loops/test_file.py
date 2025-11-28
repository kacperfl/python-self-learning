def search(lijst, target):

    links = 0
    rechts = len(lijst) - 1

    while links <= rechts:
        mid = (rechts + links) // 2

        if lijst[mid] == target:
            return mid
        elif lijst[mid] < target:
            links = mid + 1
        elif lijst[mid] > target:
            rechts = mid - 1
    return -1


def merge(lijst):

    if len(lijst) <= 1:
        return lijst

    mid = len(lijst) // 2
    right = lijst[mid:]
    links = lijst[:mid]

    links_sorted = merge(links)
    right_sorted = merge(right)
    i = 0
    j = 0
    x = []

    while i < len(links_sorted) and j < len(right_sorted):
        if links_sorted[i] <= right_sorted[j]:
            x.append(links_sorted[i])
            i += 1
        else:
            x.append(right_sorted[j])
            j += 1
    while i < len(links_sorted):
        x.append(links_sorted[i])
        i += 1
    while j < len(right_sorted):
        x.append(right_sorted[j])
        j += 1

    return x


lst = [
    27,
    44,
    31,
    74,
    47,
    19,
    59,
    77,
    61,
    60,
    66,
    68,
    63,
    35,
    8,
    71,
    1,
    97,
    62,
    51,
    69,
    96,
    40,
    43,
    48,
    33,
    79,
    32,
    87,
    45,
    57,
    11,
    72,
    49,
    58,
    37,
    83,
    15,
    30,
    13,
    20,
    18,
    75,
    23,
    26,
    17,
    91,
    10,
    100,
    9,
    28,
    50,
    81,
    64,
    5,
    55,
    89,
    6,
    90,
    39,
    25,
    82,
    36,
    84,
    73,
    56,
    88,
    93,
    12,
    78,
    24,
    54,
    76,
    65,
    99,
    3,
    21,
    34,
    41,
    53,
    2,
    92,
    52,
    22,
    7,
    42,
    70,
    86,
    14,
    4,
    46,
    85,
    67,
    80,
    16,
    94,
    95,
    98,
    29,
    38,
]

sorted_lijst = merge(lst)

print(search(sorted_lijst, 89))
