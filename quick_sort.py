"""
def quick(lis):
    length = len(lis)
    if length <=1:
        return lis
    else:
        pivot = lis.pop()

    items_greater = []
    items_lower = []

    for item in lis:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick(items_lower) + [pivot] + quick(items_greater)

print(quick([1,44,6,8,9,3,4,6,2,90,99]))
"""

def quick(lis):
    length = len(lis)
    if length<=1:
        return lis
    else:
        pivot = lis.pop()

    high = []
    low = []

    for item in lis:
        if item > pivot:
            high.append(item)
        else:
            low.append(item)
    return quick(low) + [pivot] + quick(high)

print(quick([1,5,7,8,9,0,66,44,22,56,788,8,9,0]))