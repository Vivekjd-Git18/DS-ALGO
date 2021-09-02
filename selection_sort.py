"""
def select(lis):
    end = range(0, len(lis)-1)

    for i in end:
        min_value = i


        for j in range(i+1, len(lis)):
            if lis[j] < lis[min_value]:
                min_value = j

        if min_value != i:
            lis[min_value], lis[i] = lis[i], lis[min_value]

    return lis

print (select([1,33,66,77,88,2,3,4,5,6,0]))
"""

def fun(lis):
    for i in range(0, len(lis)-1):
        min_val = i
        for j in range(i+1,len(lis)):
            if lis[j] < lis[min_val]:
                min_val = j
        if min_val!=i:
            lis[min_val], lis[i] =  lis[i], lis[min_val]
    return lis

print(fun([1,22,33,4,2,1,3,7,9,0,9,8,0,0,9,7,5,3,333,999,9]))