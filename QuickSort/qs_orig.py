def quicksort(arr_to_sort, start, end):
    if end <= start:
        return 

    p = partition(arr_to_sort, start, end)  # pivot index
    print(p)
    quicksort(arr_to_sort, start, p-1)
    quicksort(arr_to_sort, p+1, end)

def partition(arr_to_sort, start, end):
    pivot = arr_to_sort[end]
    i = 0
    for j, val in enumerate(arr_to_sort[start:end]):
        if val < pivot:
            arr_to_sort[i], arr_to_sort[j] = arr_to_sort[j], arr_to_sort[i]
            i += 1
    arr_to_sort[i], arr_to_sort[end] = arr_to_sort[end], arr_to_sort[i]
    return i


if __name__ == "__main__":
    arr = [3, 1, 34, 12, 15]
    print("array before being sorted: ", arr)
    quicksort(arr, 0, 4)
    print("array after being sorted: ", arr )
"""
algorithm partition(A, lo, hi) is
    pivot := A[hi]
    i := lo
    for j := lo to hi - 1 do
        if A[j] < pivot then
            swap A[i] with A[j]
            i := i + 1
    swap A[i] with A[hi]
    return i
"""
