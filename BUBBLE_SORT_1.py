"""
def bubble(list1):
    end_point = len(list1)-1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(0, end_point):
            if list1[i]>list1[i+1]:
                sorted =False
                list1[i],list1[i + 1] = list1[i + 1],list1[i]
    return list1

print(bubble([12,44,23,12,55,34,33,1,0,13]))

"""


"""
def bubble(lis):
    end=len(lis)-1
    sorted = False

    while not sorted:
        sorted=True
        for i in range(0, end):
            if lis[i] > lis[i+1]:
                sorted = False
                lis[i], lis[i+1] = lis[i+1], lis[i]

    return lis

print(bubble([11,223,4,4,5,5,0,1,2,3,55,999,1000]))"""


"""
def bub(lis):
    end=len(lis)-1
    sorted = False

    while not sorted:
        sorted= True
        for i in range(0, end):
            if lis[i] > lis[i+1]:
                sorted  = False
                lis[i],lis[i+1] = lis[i+1],lis[i]
    return lis

print(bub([1,22,44,55,66,77,88,9,0,6,5,2,6,2,7,9,1,4]))
"""