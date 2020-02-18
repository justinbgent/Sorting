# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO

    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO

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