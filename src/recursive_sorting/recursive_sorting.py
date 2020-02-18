# TO-DO: complete the helpe function below to merge 2 sorted arrays
import math

def merge( arrA, arrB ):
    mergedArr = []

    while arrA != [] and arrB != []:
        if arrA[0] > arrB[0]:
            mergedArr.append(arrB[0])
            arrB.pop(0)
        else:
            mergedArr.append(arrA[0])
            arrA.pop(0)

    while arrA != []:
        mergedArr.append(arrA[0])
        arrA.pop(0)
    while arrB != []:
        mergedArr.append(arrB[0])
        arrB.pop(0)

    return mergedArr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    if len(arr) <= 1 :
        return arr

    # TO-DO
    median = math.floor(len(arr) / 2)
    arrA = arr[0:median]
    arrB = arr[median:]
    
    arrA = merge_sort(arrA)
    arrB = merge_sort(arrB)

    return merge(arrA, arrB)

print(merge_sort([9,8,7,6,5,46,3,2,1]))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
