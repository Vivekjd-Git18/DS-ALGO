
"""
def insert(lis):
    for i in range(1,len(lis)):
        val_to_sort = lis[i]

        while lis[i-1] > val_to_sort and i>0:
            lis[i-1],lis[i] = lis[i], lis[i-1]
            i = i-1
    return lis

print(insert([22,5,7,8,9,0,1,2,3,5,]))

"""

def insert1(lis):
    for i in range(1,len(lis)):
        list_to_sort = lis[i]

        while lis[i-1] > list_to_sort and i>0:
            lis[i], lis[i-1] = lis[i-1], lis[i]
            i = i-1
    return lis

print(insert1([1,2,3,55,6,7,777,77,89,0,2445,55]))