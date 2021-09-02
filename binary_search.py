"""
def binary_search(list, n):
    start = 0
    end = len(list) - 1

    while start <= end:
        midpoint = start + (end-start) // 2
        midpoint_val = list[midpoint]
        if midpoint_val == n:
            return midpoint+1
        elif n < midpoint_val:
            end = midpoint-1

        else: start = midpoint+1

    return None

list = [1,2,3,4,5,6,7,8,9]
n= 9
print(binary_search(list,n))
"""


"""
def bin(arr,n):
    low=0
    high=len(arr)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<n:
            low=mid+1
        elif arr[mid]>n:
            high=mid-1
        else:
            return mid
    return -1

arr = [1,2,5,7,9,11,14,15,18,20]
n= 5

result = bin(arr,n)

if result != -1:
    print(f"element found at index {result+1} .")
else:
    print("there is not such element")"""






# ITERATIVE TECHNIQUE

def fun(list_1,x):
    low=0
    high=len(list_1)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if list_1[mid]>x:
            high=mid-1
        elif list_1[mid]<x:
            low=mid+1
        else:return mid+1

    return -1

list_1 = [ 1, 13, 33, 37, 55, 59, 62, 88, 99 ]
x = int(input("enter number to be searched"))
result = fun(list_1,x)

if result!=-1:
    print(f"succecc at {result}")
else:print("not found sorry")


