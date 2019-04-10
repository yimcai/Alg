class Heap(object):
    """
    takes a input of 
    """
    def __init__(self,):
        return 

def less(node_i, node_j, arr):
    return arr[node_i] < arr[node_j]

def exchange(root_index, child_index, arr):
    arr[root_index], arr[child_index] = arr[child_index], arr[root_index]

def max_heapify(arr, heap_size=None):
    heap_size = heap_size if heap_size is not None else len(arr)
    i = heap_size//2 -1 
    while i >=0:  # index of the last parent root
        sink(i, arr, heap_size)
        i += -1

def swim(i, arr, heap_size=None):
    heap_size = len(arr) if heap_size is None else heap_size
    parent_index = (i-1)//2
    if (i <= 0) | (less(i, parent_index, arr)):
        return 

    exchange(i, parent_index, arr)
    i = parent_index
    swim(i, arr, heap_size)
        
def _find_max(left_val, right_val):
    if right_val is None:
        return left_val
    return left_val if left_val >= right_val else right_val

def sink(i, arr, heap_size=None):
    heap_size = len(arr) if heap_size is None else heap_size 
    left_index = 2*i+1
    right_index = 2*i+2
    if i >= heap_size//2:  # node i is not the leaves
        return 
    # check if right node exist 
    if right_index <= heap_size - 1:
        left, right = arr[left_index], arr[right_index]
    else:
        left, right = arr[left_index], None
    max_val = _find_max(left, right)
    max_index = left_index if max_val == left else right_index
    if arr[max_index] > arr[i]:
        exchange(i, max_index, arr)
        sink(max_index, arr, heap_size)
    else:
        return
    
    

def heap_sort(arr):
    #max-heapify
    heap_size = len(arr)
    max_heapify(arr, heap_size=heap_size)
    while heap_size > 0:
        # exchange
        exchange(0, heap_size-1, arr)
        heap_size += -1
        sink(0, arr, heap_size)
    return arr




















