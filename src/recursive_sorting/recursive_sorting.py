# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    aIndex = 0
    bIndex = 0
    for i in range(0, elements):
        if (arrA[aIndex] < arrB[bIndex]):
            merged_arr[i] = arrA[aIndex]
            if (aIndex + 1 != len(arrA)):
                aIndex += 1
            else:
                for j in range((i + 1), elements):
                    merged_arr[j] = arrB[bIndex]
                    bIndex += 1
                    #if (bIndex == len(arrB)):
                        #break   don't need this because arrB can't run out of index's before loop finishes
                break
        else:
            merged_arr[i] = arrB[bIndex]
            if (bIndex + 1 != len(arrB)):
                bIndex += 1
            else:
                for j in range((i + 1), elements):
                    merged_arr[j] = arrA[aIndex]
                    aIndex += 1
                break
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    halfSize = int(len(arr) / 2)
    arr1 = merge_sort(arr[0:halfSize])
    arr2 = merge_sort(arr[halfSize:])

    arr = merge(arr1, arr2)
    
    return arr


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


# Not Part of Assignment just Fibonacci playing around
# Breaks when I put anything lower than 2 inside, if
# statements could solve that. 'n' is for how many
# numbers in the sequence you want
def fib_seq(n):
    arr = [0] * n
    if(n == 2):
        arr = [0, 1]
        return arr
    n -= 1
    prev_arr = fib_seq(n)
    for i in range(0, len(prev_arr)):
        arr[i] = prev_arr[i]
    arr[-1] = prev_arr[n-1] + prev_arr[n-2]
    return arr

stuff = fib_seq(10)

print(stuff)